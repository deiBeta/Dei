import random, html
P=[("1","Excitación","Aumenta el flujo de sangre a los genitales y el corazón se acelera.","Lubricación, el clítoris y los labios se inflaman, la vagina se expande.","Erección del pene y los testículos se elevan."),
("2","Meseta","La excitación se sostiene en un nivel alto; la respiración y el pulso suben.","El tercio externo de la vagina se estrecha y el clítoris se retrae bajo su capuchón.","El glande se agranda y puede aparecer líquido preseminal."),
("3","Orgasmo","El punto máximo del placer: contracciones rítmicas y liberación de la tensión.","Contracciones del útero, la vagina y el suelo pélvico. Puede repetirse.","Contracciones y eyaculación. Suele ser un solo orgasmo."),
("4","Resolución","El cuerpo vuelve poco a poco a su estado de reposo.","Puede volver a excitarse enseguida y tener orgasmos múltiples.","Periodo refractario: necesita un tiempo antes de una nueva erección.")]
r=random.Random(3)
stars="".join(f'<circle cx="{r.uniform(0,1080):.0f}" cy="{r.uniform(0,1350):.0f}" r="{r.choice([.7,1,1.4])}" fill="#f4e6d6" opacity="{r.uniform(.15,.6):.2f}"/>' for _ in range(110))
cards="".join(f'''<div class="c"><div class="h"><span class="n">{n}</span><h3>{t}</h3></div><p>{html.escape(g)}</p><p class="w"><b>Ella:</b> {html.escape(f)}</p><p class="w"><b>Él:</b> {html.escape(m)}</p></div>''' for n,t,g,f,m in P)
# chart: x 0-900, y 0-300 (300 = bottom)
W,Hc=900,300
fem="M20 280 C120 270 150 150 250 120 C330 98 400 96 470 92 C500 30 520 30 540 80 C555 110 570 110 585 70 C600 28 620 28 640 80 C680 170 760 250 880 280"
mal="M20 280 C110 262 150 160 250 125 C330 104 400 104 470 98 C495 30 515 30 535 90 C560 200 600 262 700 270 L880 278"
svgc=f'''<svg class="ch" viewBox="0 0 {W} 340">
<g stroke="#e3c08f" stroke-opacity=".35" stroke-width="1"><path d="M20 290H880"/>{''.join(f'<path d="M{x} 20V290" stroke-dasharray="4 6"/>' for x in (250,470,640))}</g>
<g font-family="PenGram" font-size="17" font-weight="700" fill="#e3c08f" text-anchor="middle" letter-spacing="2"><text x="135" y="318">EXCITACIÓN</text><text x="360" y="318">MESETA</text><text x="555" y="318">ORGASMO</text><text x="760" y="318">RESOLUCIÓN</text></g>
<path d="{mal}" fill="none" stroke="#f4e6d6" stroke-width="3.5" stroke-dasharray="10 7"/>
<path d="{fem}" fill="none" stroke="#e3c08f" stroke-width="4.5"/>
<text x="760" y="252" font-family="PenGram" font-size="15" fill="#f4e6d6" text-anchor="middle">periodo refractario</text>
<text x="600" y="22" font-family="PenGram" font-size="15" fill="#e3c08f" text-anchor="middle">orgasmos múltiples</text>
</svg>'''
doc=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><style>
@font-face{{font-family:"PenGram";src:url(../../brand/fonts/BNPenAndGram-Light.otf);font-weight:300}}
@font-face{{font-family:"PenGram";src:url(../../brand/fonts/BNPenAndGram-Bold.otf);font-weight:700}}
@font-face{{font-family:"Aire";src:url(../../brand/fonts/Aire-Bold-Italic-Pro.ttf)}}
@font-face{{font-family:"Emilia";src:url(../../brand/fonts/Emilia-Romagna.otf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;color:#f4e6d6;font-family:"PenGram",sans-serif;font-weight:300;background:radial-gradient(ellipse at 50% 30%,#7a1d2c 0,#4a0e19 50%,#22060c 100%)}}
.st{{position:absolute;inset:0}}
.top{{position:absolute;left:60px;right:60px;top:48px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:70px}} .top span{{font-family:"Emilia";color:#e3c08f;font-size:34px}}
.k{{position:absolute;left:60px;top:150px;font-weight:700;letter-spacing:.32em;text-transform:uppercase;font-size:17px;color:#e3c08f}}
h1{{position:absolute;left:56px;top:178px;font-family:"Aire";font-weight:400;font-size:76px;line-height:1}}
.sub{{position:absolute;left:60px;top:270px;font-size:23px;color:#e9d6c4}}
.ch{{position:absolute;left:90px;top:330px;width:900px;height:340px}}
.lg{{position:absolute;left:100px;top:672px;display:flex;gap:34px;font-size:17px}}
.lg span{{display:inline-block;width:38px;height:0;border-top:4px solid #e3c08f;vertical-align:middle;margin-right:10px}}
.lg span.m{{border-top:3px dashed #f4e6d6}}
.grid{{position:absolute;left:60px;right:60px;top:720px;display:grid;grid-template-columns:1fr 1fr;gap:18px}}
.c{{border:1px solid rgba(227,192,143,.4);border-radius:18px;padding:18px 22px;background:rgba(34,6,12,.35);display:grid;gap:7px}}
.h{{display:flex;align-items:center;gap:12px}}
.n{{width:34px;height:34px;border-radius:50%;background:#e3c08f;color:#3a0f19;font-weight:700;display:grid;place-items:center;font-size:17px}}
h3{{font-family:"Aire";font-weight:400;font-size:34px;line-height:1}}
.c p{{font-size:16px;line-height:1.38;color:#e9d6c4}}
.c p.w b{{color:#e3c08f;font-weight:700}}
.note{{position:absolute;left:60px;right:60px;bottom:96px;font-size:15.5px;line-height:1.4;color:#e9d6c4}}
.note b{{color:#e3c08f}}
.foot{{position:absolute;left:60px;right:60px;bottom:36px;display:flex;justify-content:space-between;align-items:flex-end;font-size:15px;color:#d9c3b0}}
.foot .s{{font-family:"Aire";font-size:30px;color:#e3c08f}}
</style></head><body>
<svg class="st" viewBox="0 0 1080 1350">{stars}</svg>
<div class="top"><img src="../../brand/logos/logo-crema.png" alt="Alma Sana"><span>by Dei</span></div>
<p class="k">Taller Mujeres salvajes</p>
<h1>El ciclo de respuesta sexual</h1>
<p class="sub">Las cuatro fases del encuentro sexual según Masters y Johnson</p>
{svgc}
<div class="lg"><div><span></span>Respuesta femenina</div><div><span class="m"></span>Respuesta masculina</div></div>
<div class="grid">{cards}</div>
<p class="note"><b>Para tener en cuenta:</b> más tarde, Helen Kaplan sumó el <b>deseo</b> como primera fase, y Rosemary Basson mostró que en muchas mujeres el deseo aparece después de la excitación, cuando hay intimidad y conexión. Cada mujer vive su ciclo a su manera.</p>
<div class="foot"><div>@almasana111</div><div class="s">Con amor, Dei</div></div>
</body></html>'''
open("ciclo-respuesta.html","w").write(doc)
