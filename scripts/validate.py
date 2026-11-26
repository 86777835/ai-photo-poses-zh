#!/usr/bin/env python3
"""Check the repo before publishing: every image path in data/*.json and every
local link or image in the README files and style pages exists; ids are unique;
each photo pose has a photo, a white model and both prompts. Exits 1 on any problem."""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
problems = []

def exists(p, where):
    if not os.path.exists(p):
        problems.append(f'{where}: missing {p}')

pp = json.load(open('data/photo-poses.json', encoding='utf-8'))
ids = [r['id'] for r in pp]
if len(ids) != len(set(ids)):
    problems.append('data/photo-poses.json: duplicate ids')
for r in pp:
    for k in ('photo', 'pose', 'photo_thumb', 'pose_thumb'):
        exists(r[k], f"photo-poses {r['id']}.{k}")
    for k in ('prompt', 'prompt_with_your_photo', 'pose_text'):
        if not r.get(k):
            problems.append(f"photo-poses {r['id']}: empty {k}")
    if not (r['name'].get('en') and r['name'].get('zh')):
        problems.append(f"photo-poses {r['id']}: needs English and Chinese names")

for path in glob.glob('data/*.json'):
    for p in set(re.findall(r'"((?:images|thumbs)/[^"]+)"', open(path, encoding='utf-8').read())):
        exists(p, path)

pages = ['README.md', 'README.zh-CN.md'] + glob.glob('styles/*.md')
for md in pages:
    base = os.path.dirname(md)
    for p in re.findall(r'(?:src="|\]\()([^")#]+)', open(md, encoding='utf-8').read()):
        if not p.startswith('http'):
            exists(os.path.normpath(os.path.join(base, p)), md)

if problems:
    print('\n'.join(problems[:50]))
    print(f'{len(problems)} problem(s)')
    sys.exit(1)
print(f'ok: {len(pp)} photo poses, {len(pages)} pages checked')
