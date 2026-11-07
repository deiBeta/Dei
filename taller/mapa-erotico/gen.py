import math, html, random
def smooth(pts, closed=True):
    n=len(pts); d=f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    rng = range(n) if closed else range(n-1)
    for i in rng:
        p0=pts[(i-1)%n]; p1=pts[i]; p2=pts[(i+1)%n]; p3=pts[(i+2)%n]
        c1=(p1[0]+(p2[0]-p0[0])/6, p1[1]+(p2[1]-p0[1])/6)
        c2=(p2[0]-(p3[0]-p1[0])/6, p2[1]-(p3[1]-p1[1])/6)
        d+=f" C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}"
    return d+(" Z" if closed else "")
def body(right):
    left=[(300-x,y) for x,y in reversed(right)]
    return smooth(right[:-1]+left[1:-1]) if False else smooth(right+left[1:-1])
F=[(162,100),(170,122),(206,138),(218,180),(224,252),(232,350),(240,392),(230,404),(220,396),(212,352),(202,262),(194,200),(184,240),(178,272),(198,318),(210,362),(208,440),(196,540),(198,612),(184,702),(198,730),(168,732),(166,702),(168,612),(168,540),(166,460),(150,420)]
M=[(163,100),(172,124),(218,140),(232,184),(238,256),(244,350),(250,394),(238,406),(228,396),(222,352),(214,262),(204,196),(196,250),(188,300),(196,350),(200,440),(194,540),(198,612),(184,702),(198,730),(168,732),(166,702),(168,612),(168,540),(166,462),(150,422)]
def figure(kind):
    pts=F if kind=="f" else M
    head='<ellipse cx="150" cy="58" rx="33" ry="41"/>'
    hair=('<path d="M117 52c0-30 18-46 33-46s34 16 34 46c0 30 6 50 14 64-12-4-22-10-26-20M117 52c0 30-6 50-14 64 12-4 22-10 26-20" fill="none"/>' if kind=="f"
          else '<path d="M118 46c2-24 16-36 32-36s30 12 32 36c-10-10-22-14-32-14s-22 4-32 14z" fill="none"/>')
    det=('<path d="M118 200c4 22 30 26 30 4M182 200c-4 22-30 26-30 4" fill="none"/><circle cx="150" cy="290" r="2.5" class="fill"/><path d="M134 404c6 6 26 6 32 0" fill="none" opacity=".6"/>' if kind=="f"
         else '<path d="M112 190c12 14 30 14 36 2M188 190c-12 14-30 14-36 2" fill="none"/><path d="M150 230v70" fill="none" opacity=".35"/><circle cx="150" cy="300" r="2.5" class="fill"/><path d="M122 350c10 24 18 40 28 52M178 350c-10 24-18 40-28 52" fill="none" opacity=".5"/>')
    return f'<g class="fig">{head}{hair}<path d="{body(pts)}"/>{det}</g>'
Z={
"f":dict(title="Mapa erótico femenino",sub="Tu cuerpo entero es territorio de placer",
 zones=[(150,22,"Cuero cabelludo","Las caricias lentas en el cabello relajan y despiertan la piel."),
 (117,62,"Orejas y lóbulos","El aliento, los susurros y los besos suaves encienden el deseo."),
 (150,84,"Labios y boca","Tienen miles de terminaciones nerviosas: el beso es la puerta."),
 (166,112,"Cuello y nuca","Zona muy sensible a besos, respiración y caricias con las yemas."),
 (232,330,"Manos y muñecas","Palmas, dedos y la cara interna de la muñeca responden al roce."),
 (130,214,"Senos y pezones","Muy sensibles, sobre todo cerca de la ovulación y antes de menstruar."),
 (150,272,"Vientre y ombligo","El abdomen bajo conecta con el útero y la energía sexual."),
 (196,236,"Espalda y columna","Recorrerla de arriba abajo despierta todo el cuerpo.",True),
 (204,348,"Espalda baja y sacro","Centro de energía de la pelvis; ama el calor y la presión suave.",True),
 (150,410,"Vulva y clítoris","El clítoris tiene unas 8.000 terminaciones nerviosas y existe solo para el placer."),
 (178,470,"Cara interna de los muslos","Piel fina y muy reactiva; alarga la anticipación."),
 (188,540,"Detrás de las rodillas","Una zona olvidada y sorprendentemente sensible.",True),
 (176,716,"Pies y dedos","Llenos de terminaciones nerviosas; el masaje relaja y excita.")]),
"m":dict(title="Mapa erótico masculino",sub="El placer del hombre va mucho más allá de los genitales",
 zones=[(150,20,"Cuero cabelludo","Las caricias en la cabeza bajan la guardia y relajan."),
 (117,62,"Orejas y lóbulos","Susurros, aliento y besos despiertan el deseo."),
 (150,84,"Labios y boca","El beso lento conecta el placer con la emoción."),
 (166,112,"Cuello y nuca","Muy sensible a besos y a caricias con las uñas suaves."),
 (238,330,"Manos y dedos","Las palmas y la cara interna de la muñeca responden al roce."),
 (124,196,"Pezones y pecho","Muchos hombres los tienen muy sensibles, aunque no lo exploren."),
 (150,300,"Abdomen y línea del vientre","El camino desde el ombligo hacia abajo aumenta la anticipación."),
 (204,236,"Espalda y columna","Recorrerla despierta todo el cuerpo.",True),
 (150,400,"Pene y glande","El glande y el frenillo concentran la mayor sensibilidad."),
 (166,430,"Testículos","Piel muy fina y sensible: siempre con suavidad."),
 (134,440,"Perineo","Entre testículos y ano; su presión suave estimula la próstata desde fuera.",False),
 (196,348,"Glúteos y sacro","Zona de mucha tensión acumulada y de gran placer al soltarla.",True),
 (178,470,"Cara interna de los muslos","Piel fina y reactiva que alarga el deseo."),
 (178,716,"Pies","El masaje de pies relaja y despierta la sensibilidad de todo el cuerpo.")])}
def stars(seed):
    r=random.Random(seed)
    return "".join(f'<circle cx="{r.uniform(0,1080):.0f}" cy="{r.uniform(0,1350):.0f}" r="{r.choice([.7,1,1.4])}" fill="#f4e6d6" opacity="{r.uniform(.15,.6):.2f}"/>' for _ in range(110))
for k,d in Z.items():
    marks=""; leg=""
    for i,z in enumerate(d["zones"],1):
        x,y,name,desc=z[:4]; back=len(z)>4 and z[4]
        marks+=f'<g class="mk{" back" if back else ""}"><circle cx="{x}" cy="{y}" r="11"/><text x="{x}" y="{y+4}">{i}</text></g>'
        leg+=f'<li><span class="n{" back" if back else ""}">{i}</span><div><b>{html.escape(name)}{" <i>· por detrás</i>" if back else ""}</b><p>{html.escape(desc)}</p></div></li>'
    doc=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><style>
@font-face{{font-family:"PenGram";src:url(../../brand/fonts/BNPenAndGram-Light.otf);font-weight:300}}
@font-face{{font-family:"PenGram";src:url(../../brand/fonts/BNPenAndGram-Bold.otf);font-weight:700}}
@font-face{{font-family:"Aire";src:url(../../brand/fonts/Aire-Bold-Italic-Pro.ttf)}}
@font-face{{font-family:"Emilia";src:url(../../brand/fonts/Emilia-Romagna.otf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;color:#f4e6d6;font-family:"PenGram",sans-serif;font-weight:300;
 background:radial-gradient(ellipse at 30% 35%,#7a1d2c 0,#4a0e19 50%,#22060c 100%)}}
.st{{position:absolute;inset:0}}
.top{{position:absolute;left:60px;right:60px;top:48px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:70px}} .top span{{font-family:"Emilia";color:#e3c08f;font-size:34px}}
.k{{position:absolute;left:60px;top:150px;font-weight:700;letter-spacing:.32em;text-transform:uppercase;font-size:17px;color:#e3c08f}}
h1{{position:absolute;left:56px;top:178px;font-family:"Aire";font-weight:400;font-size:84px;line-height:1}}
.sub{{position:absolute;left:60px;top:278px;font-size:23px;color:#e9d6c4}}
svg.f{{position:absolute;left:40px;top:330px;width:410px;height:900px}}
.fig *{{fill:none;stroke:#f4e6d6;stroke-width:2.2;stroke-linejoin:round;stroke-linecap:round}}
.fig .fill{{fill:#f4e6d6;stroke:none}}
.mk circle{{fill:#e3c08f;stroke:#2a0810;stroke-width:1.5}}
.mk text{{font:700 12px "PenGram";fill:#3a0f19;text-anchor:middle}}
.mk.back circle{{fill:#741420;stroke:#e3c08f;stroke-width:2}}
.mk.back text{{fill:#f4e6d6}}
ol{{position:absolute;left:470px;right:56px;top:350px;list-style:none;display:grid;gap:{14 if len(d["zones"])>13 else 17}px}}
li{{display:flex;gap:14px;align-items:flex-start}}
.n{{flex:none;width:30px;height:30px;border-radius:50%;background:#e3c08f;color:#3a0f19;font-weight:700;font-size:15px;display:grid;place-items:center;margin-top:2px}}
.n.back{{background:#741420;color:#f4e6d6;border:2px solid #e3c08f}}
li b{{font-weight:700;font-size:19px;letter-spacing:.02em}} li i{{font-style:normal;font-weight:300;color:#e3c08f;font-size:15px}}
li p{{font-size:16px;line-height:1.35;color:#e9d6c4;margin-top:2px}}
.foot{{position:absolute;left:60px;right:60px;bottom:40px;display:flex;justify-content:space-between;align-items:flex-end;font-size:15px;color:#d9c3b0}}
.foot .s{{font-family:"Aire";font-size:30px;color:#e3c08f}}
</style></head><body>
<svg class="st" viewBox="0 0 1080 1350">{stars(k)}</svg>
<div class="top"><img src="../../brand/logos/logo-crema.png" alt="Alma Sana"><span>by Dei</span></div>
<p class="k">Taller Mujeres salvajes</p>
<h1>{d["title"]}</h1>
<p class="sub">{d["sub"]}</p>
<svg class="f" viewBox="0 -6 300 750">{figure(k)}{marks}</svg>
<ol>{leg}</ol>
<div class="foot"><div>Cada cuerpo es único: explora con curiosidad, consentimiento y sin prisa.<br>@almasana111</div><div class="s">Con amor, Dei</div></div>
</body></html>'''
    open(f"mapa-{k}.html","w").write(doc)
print("ok")
