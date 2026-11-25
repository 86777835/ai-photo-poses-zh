#!/usr/bin/env python3
"""Pick candidate poses from the photo-pose library and build ready-to-use
prompts for "the user's photo + a white-model pose".

  python3 recommend.py --list-styles
  python3 recommend.py --style street,hkretro --group stand,lean --limit 6
  python3 recommend.py --style gothic --framing half --keep-outfit
  python3 recommend.py --id sp101 --keep-outfit          # one pose, full detail
  python3 recommend.py --style y2k --remote               # no clone: read from GitHub

The agent looks at the user's photo and decides the filters; this script only
filters the data and assembles prompts. Image 1 is always the user's photo,
image 2 the white model. Unknown styles, groups or ids are errors.
Standard library only.
"""
import argparse, json, os, sys, urllib.request

RAW = 'https://raw.githubusercontent.com/86777835/ai-photo-poses-zh/main/'
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GROUPS = ['stand', 'sit', 'lean', 'walk', 'look', 'crouch', 'lie', 'upper', 'move']


def load(remote):
    if remote:
        with urllib.request.urlopen(RAW + 'data/photo-poses.json', timeout=60) as r:
            return json.load(r)
    path = os.path.join(ROOT, 'data', 'photo-poses.json')
    if not os.path.exists(path):
        sys.exit(f'{path} not found: run from a clone of ai-photo-poses-zh, or pass --remote')
    return json.load(open(path, encoding='utf-8'))


def csv(value, allowed, what):
    if not value:
        return None
    items = [v.strip() for v in value.split(',') if v.strip()]
    bad = [v for v in items if v not in allowed]
    if bad:
        sys.exit(f'unknown {what}: {", ".join(bad)}; allowed: {", ".join(sorted(allowed))}')
    return set(items)


def with_photo_prompt(rec, keep_outfit):
    prompt = rec['prompt_with_your_photo']
    if keep_outfit:
        start = prompt.index('), wearing ') + len('), ')
        end = prompt.index('. Pose: ')
        prompt = prompt[:start] + 'wearing the same clothes as in image 1' + prompt[end:]
    return prompt


def image(rec, key, remote):
    return RAW + rec[key] if remote else os.path.join(ROOT, rec[key])


def main():
    ap = argparse.ArgumentParser(description='Recommend photo poses for a user photo.')
    ap.add_argument('--style', help='comma-separated style ids (see --list-styles)')
    ap.add_argument('--group', help='comma-separated: ' + ','.join(GROUPS))
    ap.add_argument('--framing', choices=['full', 'half'], help='full body or waist-up')
    ap.add_argument('--id', help='one pose id, e.g. sp101')
    ap.add_argument('--keep-outfit', action='store_true',
                    help="keep the user's own clothes instead of the style's outfit")
    ap.add_argument('--limit', type=int, default=8)
    ap.add_argument('--remote', action='store_true', help='read data and images from GitHub')
    ap.add_argument('--list-styles', action='store_true')
    a = ap.parse_args()
    data = load(a.remote)
    styles = {}
    for r in data:
        styles.setdefault(r['style'], r['style_name'])
    if a.list_styles:
        for sid, name in styles.items():
            n = sum(r['style'] == sid for r in data)
            print(f"{sid:10} {name['zh']} / {name['en']} ({n})")
        return
    if a.id:
        picks = [r for r in data if r['id'] == a.id]
        if not picks:
            sys.exit(f'no pose {a.id}')
    else:
        want_style = csv(a.style, set(styles), 'style')
        want_group = csv(a.group, set(GROUPS), 'group')
        picks = [r for r in data
                 if (not want_style or r['style'] in want_style)
                 and (not want_group or r['group'] in want_group)
                 and (not a.framing or r['framing'] == a.framing)]
        if not picks:
            sys.exit('no pose matches these filters; loosen --group or --framing')
        picks = picks[:a.limit]
    out = [{
        'id': r['id'],
        'name': r['name']['zh'],
        'style': f"{r['style_name']['zh']} ({r['style']})",
        'group': r['group_name']['zh'],
        'framing': r['framing'],
        'pose': r['pose_text'],
        'sample_photo': image(r, 'photo', a.remote),
        'white_model': image(r, 'pose', a.remote),
        'page': r['url'],
        'refs': ['image 1: the user photo', 'image 2: ' + image(r, 'pose', a.remote)],
        'prompt': with_photo_prompt(r, a.keep_outfit),
    } for r in picks]
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    print()


if __name__ == '__main__':
    main()
