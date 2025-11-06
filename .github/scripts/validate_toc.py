import yaml, pathlib, sys

p = pathlib.Path('_toc.yml')
if not p.exists():
    print('_toc.yml not found')
    sys.exit(1)

toc = yaml.safe_load(p.read_text())
missing = []

def check_entry(e):
    if isinstance(e, dict) and 'file' in e:
        fp = pathlib.Path(e['file'])
        if fp.exists():
            if fp.is_dir():
                missing.append((e['file'], 'is_directory'))
        elif (fp.with_suffix('.md')).exists() or (fp.with_suffix('.ipynb')).exists():
            return
        else:
            missing.append((e['file'], 'not_found'))
    elif isinstance(e, dict):
        for v in e.values():
            if isinstance(v, list):
                for it in v:
                    check_entry(it)

for part in toc.get('parts', []):
    for ch in part.get('chapters', []):
        check_entry(ch)

if missing:
    print('TOC references problems:')
    for m in missing:
        print(m)
    sys.exit(1)
else:
    print('TOC validation OK')
