from pathlib import Path
from html import escape as e
import json

ROOT = Path(__file__).resolve().parents[1]
d = json.loads((ROOT / 'site.json').read_text(encoding='utf-8'))
pages = [('about', 'About', ''), ('research', 'Research', 'research'), ('cv', 'CV', 'cv'), ('publications', 'Publications', 'publications'), ('projects', 'Projects', 'projects')]

def education():
    rows = []
    for x in d['education']:
        rows.append(f'<article class="entry"><h3>{e(x["degree"])}</h3><p class="institution">{e(x["institution"])} <span class="date">{e(x["period"])}</span></p><p class="secondary">{e(x.get("details", ""))}</p></article>')
    return '<section id="education"><h2>Education</h2>'+''.join(rows)+'</section>'

def publications():
    rows=[]
    for x in d['publications']:
        title=e(x['title'])
        if x.get('url'): title=f'<a href="{e(x["url"], quote=True)}">{title}</a>'
        rows.append(f'<article class="entry publication"><h3>{title}</h3><p>{e(x["authors"])}</p><p class="publication-status">{e(x["status"])}</p></article>')
    return ''.join(rows)

def section(k):
    return '<section id="'+k+'">'+d['sections'][k]+'</section>'

for key, title, folder in pages:
    prefix='../' if folder else './'
    downloads=f'<div class="downloads"><a href="{prefix}files/Junwen_Lou_CV_EN.pdf" download>Download CV · English <span>↓</span></a><a href="{prefix}files/Junwen_Lou_CV_ZH.pdf" download>Download CV · Chinese <span>↓</span></a></div>'
    if key=='about':
        content='<h1>About me</h1>'+''.join('<p class="bio">'+e(x)+'</p>' for x in d['bio'])
        content+='<section class="explore"><h2>Explore</h2><div class="explore-grid">'
        for slug,label,description in [('research','Research','Current research questions and projects.'),('cv','Curriculum vitae','Education, experience, and academic background.'),('publications','Publications','Manuscripts and scholarly work.'),('projects','Projects','Selected software and data applications.')]:
            content+=f'<a class="explore-link" href="{prefix}{slug}/"><strong>{label}<span>↗</span></strong><p>{description}</p></a>'
        content+='</div></section>'
    elif key=='cv':
        content='<h1>Curriculum vitae</h1>'+downloads+'<p class="updated">Last updated '+e(d['updated'])+'</p>'
        content+='<nav class="page-index" aria-label="CV sections"><a href="#education">Education</a><a href="#experience">Experience</a><a href="#manuscripts">Manuscripts</a><a href="#awards">Awards</a><a href="#skills">Skills</a></nav>'
        content+=education()+section('experience')+'<section id="manuscripts"><h2>Manuscripts</h2>'+publications()+'</section>'+section('awards')+section('skills')
        for k,label in [('teaching','Teaching'),('service','Academic service')]:
            if d.get(k): content+=f'<section id="{k}"><h2>{label}</h2><ul>'+''.join('<li>'+e(x)+'</li>' for x in d[k])+'</ul></section>'
    elif key=='publications':
        content='<h1>Publications &amp; manuscripts</h1>'+publications()
    else:
        content=section(key).replace('<h2>', '<h1>', 1).replace('</h2>', '</h1>', 1)
    nav=''.join(f'<a href="{prefix}{slug+"/" if slug else ""}"'+(' aria-current="page"' if k==key else '')+'>'+label+'</a>' for k,label,slug in pages)
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | {e(d['name'])}</title><meta name="description" content="{e(d['name'])}. {e(d['tagline'])}. {e(title)}."><link rel="icon" href="{prefix}assets/favicon.svg"><link rel="stylesheet" href="{prefix}assets/style.css"></head>
<body><a class="skip" href="#main">Skip to content</a><header class="masthead"><div class="header-inner"><a class="brand" href="{prefix}">{e(d['name'])}</a><nav aria-label="Main navigation">{nav}</nav></div></header>
<div class="layout"><aside class="profile"><a href="{prefix}" aria-label="Junwen Lou home"><img class="portrait" src="{prefix}assets/portrait.jpg" width="283" height="378" alt="Portrait of Junwen Lou"></a><h2>{e(d['name'])}</h2><p class="tagline">{e(d['tagline'])}</p><p class="location">{e(d['location'])}</p><div class="profile-links"><a href="mailto:{e(d['email'])}">Email ↗</a><a href="{e(d['github'])}" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="{prefix}files/Junwen_Lou_CV_EN.pdf" download>CV · English ↓</a><a href="{prefix}files/Junwen_Lou_CV_ZH.pdf" download>CV · Chinese ↓</a></div></aside>
<main id="main">{content}</main></div><footer><span>© 2026 {e(d['name'])}</span><span>Updated {e(d['updated'])}</span></footer></body></html>'''
    target=ROOT/folder if folder else ROOT
    target.mkdir(exist_ok=True)
    (target/'index.html').write_text(html,encoding='utf-8')
(ROOT/'assets/style.css').write_text((ROOT/'tools/site.css').read_text(encoding='utf-8'),encoding='utf-8')
print('Built five pages from site.json.')
