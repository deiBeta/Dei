import random, json, html
E=json.load(open('../../ciclo/emblemas/emblemas.json'))
r=random.Random(9)
stars="".join(f'<circle cx="{r.uniform(0,1080):.0f}" cy="{r.uniform(0,1350):.0f}" r="{r.choice([.7,1,1.4])}" fill="#f4e6d6" opacity="{r.uniform(.15,.6):.2f}"/>' for _ in range(120))
sci=[("Células madre","Desde 2007 se estudian las células madre endometriales que viajan en la sangre menstrual, capaces de regenerar tejidos."),
("Citoquinas y factores de crecimiento","Proteínas mensajeras que regulan la inflamación y la renovación del endometrio cada mes."),
("Hierro y nutrientes","Hierro, nitrógeno, fósforo y potasio: los mismos nutrientes que alimentan a las plantas.")]
trad=[("Ofrenda a la Madre Tierra","Muchas culturas ancestrales devolvían la sangre a la tierra como gesto de gratitud y fertilidad."),
("La red viva bajo tus pies","Bajo el suelo, los hongos tejen una red que comunica a las plantas, a la que algunos llaman el sistema nervioso de la Tierra. Para la tradición, al ofrendar tu sangre te unes a esa red."),
("Reconciliación con tu cuerpo","Mirar tu sangre como medicina, y no como algo sucio, sana la relación con tu ciclo y tu linaje.")]
steps=["Recoge tu sangre con copa menstrual o toallas de tela.","Dilúyela en agua: una parte de sangre en unas diez de agua.","Elige una planta o un rincón de tierra al aire libre.","Riega con intención y di: «Te devuelvo la vida que me das».","Agradece y escribe lo que sentiste."]
def items(L): return "".join(f'<li><b>{html.escape(a)}</b><p>{html.escape(b)}</p></li>' for a,b in L)
doc=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><style>
@font-face{{font-family:"PenGram";src:url(../../brand/fonts/BNPenAndGram-Light.otf);font-weight:300}}
@font-face{{font-family:"PenGram";src:url(../../brand/fonts/BNPenAndGram-Bold.otf);font-weight:700}}
@font-face{{font-family:"Aire";src:url(../../brand/fonts/Aire-Bold-Italic-Pro.ttf)}}
@font-face{{font-family:"Emilia";src:url(../../brand/fonts/Emilia-Romagna.otf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;color:#f4e6d6;font-family:"PenGram",sans-serif;font-weight:300;background:radial-gradient(ellipse at 50% 25%,#7a1d2c 0,#4a0e19 50%,#22060c 100%)}}
.st{{position:absolute;inset:0}}
.top{{position:absolute;left:60px;right:60px;top:48px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:70px}} .top span{{font-family:"Emilia";color:#e3c08f;font-size:34px}}
.emb{{position:absolute;right:70px;top:150px;width:170px}} .emb svg{{width:100%;display:block}}
.k{{position:absolute;left:60px;top:150px;font-weight:700;letter-spacing:.32em;text-transform:uppercase;font-size:17px;color:#e3c08f}}
h1{{position:absolute;left:56px;top:180px;font-family:"Aire";font-weight:400;font-size:78px;line-height:1}}
.sub{{position:absolute;left:60px;top:272px;font-size:23px;color:#e9d6c4;width:740px}}
.main{{position:absolute;left:60px;right:60px;top:350px;bottom:96px;display:flex;flex-direction:column;justify-content:space-between}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:22px}}
.col{{border:1px solid rgba(227,192,143,.4);border-radius:20px;padding:22px 24px;background:rgba(34,6,12,.35)}}
.col h2{{font-weight:700;font-size:15px;letter-spacing:.26em;text-transform:uppercase;color:#e3c08f;margin-bottom:4px}}
.col h3{{font-family:"Aire";font-weight:400;font-size:38px;margin-bottom:14px}}
.col ul{{list-style:none;display:grid;gap:18px}}
.col b{{font-weight:700;font-size:21px}} .col p{{font-size:18px;line-height:1.38;color:#e9d6c4;margin-top:2px}}
.rit{{border-radius:20px;padding:22px 26px;background:linear-gradient(135deg,#741420,#3a0a14);border:1px solid rgba(227,192,143,.5)}}
.rit h2{{font-family:"Aire";font-weight:400;font-size:42px}}
.rit ol{{margin-top:10px;padding-left:24px;display:grid;grid-template-columns:1fr 1fr;gap:10px 30px;font-size:19px;line-height:1.38}}
.rit ol li::marker{{color:#e3c08f;font-weight:700}}
.af{{text-align:center;font-family:"Aire";font-size:40px;line-height:1.2;color:#f4e6d6}}
.af small{{display:block;font-family:"PenGram";font-weight:700;font-size:14px;letter-spacing:.3em;text-transform:uppercase;color:#e3c08f;margin-bottom:8px}}
.note{{font-size:16.5px;line-height:1.42;color:#e9d6c4}}
.note b{{color:#e3c08f}}
.foot{{position:absolute;left:60px;right:60px;bottom:36px;display:flex;justify-content:space-between;align-items:flex-end;font-size:15px;color:#d9c3b0}}
.foot .s{{font-family:"Aire";font-size:30px;color:#e3c08f}}
</style></head><body>
<svg class="st" viewBox="0 0 1080 1350">{stars}</svg>
<div class="top"><img src="../../brand/logos/logo-crema.png" alt="Alma Sana"><span>by Dei</span></div>
<div class="emb">{E["invierno"]}</div>
<p class="k">Taller Mujeres salvajes</p>
<h1>Tu sangre es medicina</h1>
<p class="sub">La siembra de luna: devolver tu sangre menstrual a la tierra como ofrenda</p>
<div class="main"><div class="cols">
 <div class="col"><h2>Lo que dice la ciencia</h2><h3>¿Qué lleva tu sangre?</h3><ul>{items(sci)}</ul></div>
 <div class="col"><h2>Lo que dice la tradición</h2><h3>Un acto sagrado</h3><ul>{items(trad)}</ul></div>
</div>
<div class="rit"><h2>Cómo hacer tu siembra de luna</h2><ol>{"".join(f"<li>{html.escape(s)}</li>" for s in steps)}</ol></div>
<p class="af"><small>Palabras para tu ofrenda</small>«Lo que sale de mí vuelve a ti como vida.<br>Madre Tierra, recibe mi sangre sagrada.»</p>
<p class="note"><b>Con honestidad:</b> la ciencia ha estudiado los componentes de la sangre menstrual, pero no su efecto energético ni su conexión con la Tierra; eso pertenece a la experiencia espiritual de cada mujer. Ofrece solo tu propia sangre, siempre diluida, en plantas de exterior y nunca en huertas de alimentos que se coman crudos.</p></div>
<div class="foot"><div>@almasana111</div><div class="s">Con amor, Dei</div></div>
</body></html>'''
open("siembra-de-luna.html","w").write(doc)
