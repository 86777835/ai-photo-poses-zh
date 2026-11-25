#!/usr/bin/env python3
"""Assemble portrait-photo prompts from the component library.

  python3 scripts/assemble.py --list
  python3 scripts/assemble.py tokyo-rain-night            # all 9 shots, fictional model
  python3 scripts/assemble.py tokyo-rain-night --shot 3   # one shot
  python3 scripts/assemble.py tokyo-rain-night --with-photo   # "the person in image 1"
  python3 scripts/assemble.py --recipe my-recipe.json     # your own recipe

A recipe only references component ids from data/components.json; see
data/portrait-recipes.json for the format. Unknown ids are errors.
For each shot the script prints the prompt and the reference images to attach,
in order (your photo first when --with-photo, then the white-model pose image).
"""
import argparse, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = json.load(open(os.path.join(ROOT, 'data', 'components.json'), encoding='utf-8'))
BY = {slot: {v['id']: v for v in vals} for slot, vals in C.items()}


def get(slot, vid):
    if vid not in BY[slot]:
        sys.exit(f'unknown {slot} id: {vid} (see data/components.json)')
    return BY[slot][vid]


def text(slot, vid):
    return get(slot, vid)['text']


def shot_prompt(recipe, shot, with_photo):
    s = recipe['set']
    pose = get('pose', shot['pose'])
    refs = []
    if with_photo:
        who = ('the person in image 1 (keep their exact face, facial features, skin tone and '
               'hairstyle; do not beautify or swap the face)')
        refs.append('your photo')
    else:
        who = recipe['subject']
    if pose['pose_ref']:
        refs.append(pose['image'])
    lines = [f"A real photograph: {text('look', s['look'])}. {text('skin', s['skin'])}."]
    lines.append(f"Subject: {who}. Wearing {text('outfit', s['outfit'])}. "
                 f"Hair: {text('hair', s['hair'])}. Makeup: {text('makeup', s['makeup'])}.")
    lines.append(f"Scene: {text('scene', s['scene'])}.")
    body = f"Pose: {pose['text']}."
    if pose['pose_ref']:
        body += (f" Image {len(refs)} is a faceless grey mannequin that shows only this body pose: "
                 "copy it exactly (head, torso, arms, hands, legs, feet, which hand does what), "
                 "but do not copy the mannequin itself: no grey skin, no bald head, no joints.")
    if shot.get('action'):
        body += f" Action: {text('action', shot['action'])}."
    if s.get('motion'):
        body += f" {text('motion', s['motion'])}."
    if s['props']:
        body += ' Props: ' + '; '.join(text('props', p) for p in s['props']) + '.'
    lines.append(body)
    lines.append(f"Expression: {text('expression', shot['expression'])}.")
    comp = [text('shot_size', shot['shot_size']), text('angle', shot['angle'])]
    if shot.get('placement'):
        comp.append(text('placement', shot['placement']))
    if shot.get('foreground'):
        comp.append(text('foreground', shot['foreground']))
    lines.append('Composition: ' + '; '.join(comp) + f". Camera: {text('camera', shot['camera'])}.")
    light = f"Lighting: {text('light', s['light'])}."
    if s['light_mod']:
        light += ' Light details: ' + '; '.join(text('light_mod', m) for m in s['light_mod']) + '.'
    lines.append(light)
    lines.append('Avoid: ' + '; '.join(text('negative', x) for x in s['negative']) + '. Portrait 3:4.')
    return '\n'.join(lines), refs


def main():
    ap = argparse.ArgumentParser(description='Assemble portrait prompts from components.')
    ap.add_argument('id', nargs='?', help='recipe id from data/portrait-recipes.json')
    ap.add_argument('--recipe', help='path to your own recipe JSON (same format)')
    ap.add_argument('--shot', type=int, help='only this shot (1-based)')
    ap.add_argument('--with-photo', action='store_true', help='use your photo as the person')
    ap.add_argument('--list', action='store_true', help='list built-in recipes')
    a = ap.parse_args()
    recipes = json.load(open(os.path.join(ROOT, 'data', 'portrait-recipes.json'), encoding='utf-8'))
    if a.list:
        for r in recipes:
            print(f"{r['id']:32} {r['name']['zh']}")
        return
    if a.recipe:
        recipe = json.load(open(a.recipe, encoding='utf-8'))
    elif a.id:
        found = [r for r in recipes if r['id'] == a.id]
        if not found:
            sys.exit(f'no recipe {a.id}; try --list')
        recipe = found[0]
    else:
        ap.error('give a recipe id, --recipe or --list')
    shots = recipe['shots']
    picks = range(1, len(shots) + 1) if a.shot is None else [a.shot]
    for n in picks:
        if not 1 <= n <= len(shots):
            sys.exit(f'shot {n} out of range 1..{len(shots)}')
        prompt, refs = shot_prompt(recipe, shots[n - 1], a.with_photo)
        print(f"=== shot {n}" + (f"  refs: {' + '.join(refs)}" if refs else ''))
        print(prompt + '\n')


main()
