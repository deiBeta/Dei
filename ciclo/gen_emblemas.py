import random, json, math
C="#f4e6d6"; G="#e3c08f"
def stars(seed,n=26):
    r=random.Random(seed); o=[]
    for _ in range(n):
        x,y=r.uniform(20,180),r.uniform(20,180)
        if (x-100)**2+(y-100)**2>86**2: continue
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r.choice([.6,.9,1.3])}" fill="{C}" opacity="{r.uniform(.3,.8):.2f}"/>')
    for _ in range(3):
        x,y=r.uniform(40,160),r.uniform(30,60)
        o.append(f'<path d="M{x} {y-5}L{x+1.2} {y-1.2}L{x+5} {y}L{x+1.2} {y+1.2}L{x} {y+5}L{x-1.2} {y+1.2}L{x-5} {y}L{x-1.2} {y-1.2}Z" fill="{G}"/>')
    return "".join(o)
M={
# Bruja: sombrero de bruja sobre caldero humeante
"invierno":f'''<path d="M100 30 L78 88 L122 88 Z" fill="{C}"/><path d="M100 30 C112 44 118 40 126 50" fill="none" stroke="{C}" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="100" cy="90" rx="40" ry="8" fill="{C}"/><rect x="80" y="80" width="40" height="6" fill="#741420"/>
<g fill="none" stroke="{G}" stroke-width="2" stroke-linecap="round"><path d="M88 120c-4-6 4-9 0-15"/><path d="M100 118c-4-7 5-10 0-17"/><path d="M112 120c-4-6 4-9 0-15"/></g>
<path d="M64 124h72" stroke="{C}" stroke-width="4" stroke-linecap="round"/><path d="M68 126c0 22 13 32 32 32s32-10 32-32z" fill="{C}"/>
<path d="M76 158l-7 10M124 158l7 10" stroke="{C}" stroke-width="4" stroke-linecap="round"/>''',
# Doncella: flor abierta con tallo y hojas
"primavera":f'''<path d="M56 108 Q100 46 144 108" fill="none" stroke="{C}" stroke-width="2.5"/><ellipse cx="62" cy="92" rx="6" ry="3" transform="rotate(-60 62 92)" fill="{C}" opacity=".85"/><ellipse cx="76" cy="77" rx="6" ry="3" transform="rotate(-35 76 77)" fill="{C}" opacity=".85"/><ellipse cx="92" cy="69" rx="6" ry="3" transform="rotate(-12 92 69)" fill="{C}" opacity=".85"/><ellipse cx="108" cy="69" rx="6" ry="3" transform="rotate(12 108 69)" fill="{C}" opacity=".85"/><ellipse cx="124" cy="77" rx="6" ry="3" transform="rotate(35 124 77)" fill="{C}" opacity=".85"/><ellipse cx="138" cy="92" rx="6" ry="3" transform="rotate(60 138 92)" fill="{C}" opacity=".85"/><circle cx="64.0" cy="104.0" r="5.4" fill="{G}"/><circle cx="59.9" cy="109.7" r="5.4" fill="{G}"/><circle cx="53.1" cy="107.5" r="5.4" fill="{G}"/><circle cx="53.1" cy="100.5" r="5.4" fill="{G}"/><circle cx="59.9" cy="98.3" r="5.4" fill="{G}"/><circle cx="58" cy="104" r="3" fill="#741420"/><circle cx="74.0" cy="84.0" r="5.4" fill="{C}"/><circle cx="69.9" cy="89.7" r="5.4" fill="{C}"/><circle cx="63.1" cy="87.5" r="5.4" fill="{C}"/><circle cx="63.1" cy="80.5" r="5.4" fill="{C}"/><circle cx="69.9" cy="78.3" r="5.4" fill="{C}"/><circle cx="68" cy="84" r="3" fill="#741420"/><circle cx="90.0" cy="72.0" r="5.4" fill="{G}"/><circle cx="85.9" cy="77.7" r="5.4" fill="{G}"/><circle cx="79.1" cy="75.5" r="5.4" fill="{G}"/><circle cx="79.1" cy="68.5" r="5.4" fill="{G}"/><circle cx="85.9" cy="66.3" r="5.4" fill="{G}"/><circle cx="84" cy="72" r="3" fill="#741420"/><circle cx="106.0" cy="68.0" r="5.4" fill="{C}"/><circle cx="101.9" cy="73.7" r="5.4" fill="{C}"/><circle cx="95.1" cy="71.5" r="5.4" fill="{C}"/><circle cx="95.1" cy="64.5" r="5.4" fill="{C}"/><circle cx="101.9" cy="62.3" r="5.4" fill="{C}"/><circle cx="100" cy="68" r="3" fill="#741420"/><circle cx="122.0" cy="72.0" r="5.4" fill="{G}"/><circle cx="117.9" cy="77.7" r="5.4" fill="{G}"/><circle cx="111.1" cy="75.5" r="5.4" fill="{G}"/><circle cx="111.1" cy="68.5" r="5.4" fill="{G}"/><circle cx="117.9" cy="66.3" r="5.4" fill="{G}"/><circle cx="116" cy="72" r="3" fill="#741420"/><circle cx="138.0" cy="84.0" r="5.4" fill="{C}"/><circle cx="133.9" cy="89.7" r="5.4" fill="{C}"/><circle cx="127.1" cy="87.5" r="5.4" fill="{C}"/><circle cx="127.1" cy="80.5" r="5.4" fill="{C}"/><circle cx="133.9" cy="78.3" r="5.4" fill="{C}"/><circle cx="132" cy="84" r="3" fill="#741420"/><circle cx="148.0" cy="104.0" r="5.4" fill="{G}"/><circle cx="143.9" cy="109.7" r="5.4" fill="{G}"/><circle cx="137.1" cy="107.5" r="5.4" fill="{G}"/><circle cx="137.1" cy="100.5" r="5.4" fill="{G}"/><circle cx="143.9" cy="98.3" r="5.4" fill="{G}"/><circle cx="142" cy="104" r="3" fill="#741420"/>
<path d="M60 110c-4 18 2 34 8 46M140 110c4 18-2 34-8 46" fill="none" stroke="{G}" stroke-width="2" stroke-linecap="round"/>
<path d="M68 156l-4 8M132 156l4 8" stroke="{G}" stroke-width="2" stroke-linecap="round"/>''',
# Madre: sol radiante con corazón
"verano":f'''<path d="M100 172V112" stroke="{C}" stroke-width="3" stroke-linecap="round"/>
<path d="M100 150c-16 0-26-10-28-22 14-2 26 6 28 22z" fill="{G}"/><path d="M100 136c16 0 26-10 28-22-14-2-26 6-28 22z" fill="{G}"/>
<path d="M60 74c0-22 18-38 40-38s40 16 40 38c0 24-18 40-40 40S60 98 60 74z" fill="{C}"/>
<g fill="none" stroke="#741420" stroke-width="2.6" stroke-linecap="round" opacity=".85">
<path d="M100 54c10 0 16 7 14 15s-11 11-17 8-7-11-1-14 10 1 9 6"/>
<path d="M78 66c2 16 12 26 22 26s20-8 22-24"/>
<path d="M68 82c6 14 18 22 32 22s26-8 32-22"/>
<path d="M82 46c-6 6-8 14-6 22M118 46c6 6 8 14 6 22"/></g>
<g fill="{G}"><circle cx="54" cy="56" r="2.2"/><circle cx="148" cy="60" r="2.2"/></g>
''',
# Hechicera: hojas de otoño cayendo + espiral
"otono":f'''<circle cx="100" cy="88" r="36" fill="{C}" opacity=".95"/>
<circle cx="100" cy="88" r="36" fill="none" stroke="{G}" stroke-width="1.5"/>
<path d="M84 72a20 20 0 0 1 14-8" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".9"/>
<g fill="#741420"><path d="M106 84 l2 5 5 2 -5 2 -2 5 -2 -5 -5 -2 5 -2z"/><circle cx="92" cy="98" r="2"/><circle cx="114" cy="102" r="1.4"/><path d="M96 82a8 8 0 1 0 8 10 6 6 0 1 1-8-10z"/></g>
<path d="M74 132c4-8 14-10 26-10s22 2 26 10l6 18H68z" fill="{C}"/>
<path d="M62 150h76" stroke="{C}" stroke-width="5" stroke-linecap="round"/>
<g fill="none" stroke="{G}" stroke-width="1.6" stroke-linecap="round"><path d="M80 138h40"/></g>''',
}
out={}
for k,m in M.items():
    out[k]=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" role="img"><defs><radialGradient id="g{k}" cx="50%" cy="38%" r="70%"><stop offset="0" stop-color="#8a2433"/><stop offset=".55" stop-color="#5a1220"/><stop offset="1" stop-color="#2a0810"/></radialGradient></defs><circle cx="100" cy="100" r="96" fill="url(#g{k})"/><circle cx="100" cy="100" r="91" fill="none" stroke="{G}" stroke-width=".8" opacity=".6"/>{stars(k)}{m}</svg>'''
    open(f"emblemas/{k}.svg","w").write(out[k])
json.dump(out,open("emblemas/emblemas.json","w"))
