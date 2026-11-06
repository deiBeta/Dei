import json, html
E=json.load(open("emblemas/emblemas.json"))
R=[
dict(slug="invierno",arq="La Bruja",fase="Fase menstrual",est="Invierno interior",dias="Días 1 a 5 aprox.",
 sub="La sabia del umbral",
 intro="La Bruja es la mujer que camina entre mundos. En tu menstruación el velo entre lo visible y lo invisible se vuelve delgado: tu intuición habla más fuerte, tus sueños traen mensajes y tu cuerpo te invita a morir un poco para renacer. Este es tu tiempo sagrado de silencio.",
 corr=[("Elemento","Agua"),("Luna","Luna nueva"),("Dirección","Norte"),("Cristal","Piedra de luna o granate"),("Colores","Rojo profundo y negro"),("Plantas","Rosa, canela y jengibre")],
 inv="Abuela Luna, sabias que caminaron antes que yo: hoy me retiro a mi cueva. Suelto lo que ya cumplió su ciclo y escucho la voz que vive en mi sangre. Mi útero es mi oráculo.",
 nombre="El caldero de lo que suelto",
 pasos=['Siéntate con tus manos sobre el vientre y respira nueve veces, imaginando una luz roja y cálida en tu útero.', 'Di tu invocación en voz alta, despacio.', 'Escribe en un papel lo que quieres soltar y ponlo en un recipiente con agua: tu caldero.', 'Mientras se moja, repite: «Lo que ya no es mío vuelve a la tierra». Luego entiérralo en una maceta.', 'Opcional: si usas copa o toallas de tela, ofrece unas gotas de tu sangre diluida en agua a una planta. Es la siembra de luna.'],
 beb=("Elixir de la Bruja","Infusión de jengibre, canela y pétalos de rosa (si son comestibles). Sopla tres veces sobre la taza antes de beber, poniendo una intención en cada soplo."),
 ali=("Comida que abriga la raíz","Sopas, caldos de huesos o de verduras, lentejas, remolacha y chocolate oscuro. Come despacio, como quien recibe una medicina."),
 mov=("Movimiento de la cueva","Postura del niño, rodillas al pecho y círculos lentos de cadera acostada. Muévete como si estuvieras dentro de una cueva cálida."),
 afir="Me permito morir a lo viejo. En mi silencio, renazco.",
 preg=["¿Qué me mostró mi intuición o mis sueños estos días?","¿Qué estoy lista para dejar morir?","¿Qué semilla quiero guardar para la próxima primavera?"]),
dict(slug="primavera",arq="La Doncella",fase="Fase folicular",est="Primavera interior",dias="Días 6 a 12 aprox.",
 sub="La que vuelve a nacer",
 intro="La Doncella es la energía de lo que despierta. Después de la cueva, sales a la luz con ojos nuevos: vuelve la curiosidad, la ligereza y el deseo de crear. Todo lo que siembres en estos días tiene la fuerza de la primavera.",
 corr=[("Elemento","Aire"),("Luna","Luna creciente"),("Dirección","Este"),("Cristal","Cuarzo rosa o aventurina"),("Colores","Verde tierno y rosa"),("Plantas","Hierbabuena, limón y flores frescas")],
 inv="Doncella que vive en mí, despierta. Abro mis ojos al mundo como si fuera la primera vez. Me doy permiso de jugar, de soñar y de empezar de nuevo.",
 nombre="La semilla de mi intención",
 pasos=['Sal al aire libre o abre una ventana y respira profundo.', 'Di tu invocación en voz alta.', 'Sostén una semilla junto a tu corazón y dile qué quieres hacer nacer este ciclo.', 'Siémbrala en una maceta y riégala diciendo: «Te riego con mi alegría».', 'Riégala cada día de esta fase repitiendo tu intención.'],
 beb=("Agua de la Doncella","Agua tibia con limón, hierbabuena y una cucharadita de miel. Tómala al despertar, mirando el cielo, y pide un deseo para tu día."),
 ali=("Comida viva","Frutas, ensaladas, germinados, semillas, avena y huevos. Prueba algo que nunca hayas comido: tu Doncella ama lo nuevo."),
 mov=("Danza de la Doncella","Pon tu canción favorita y baila descalza, saltando, girando y riendo. Luego camina rápido al aire libre."),
 afir="Soy nueva cada día. Lo que siembro hoy florece en mí.",
 preg=["¿Qué me da curiosidad ahora mismo?","¿Qué quiero hacer nacer este ciclo?","¿Cómo puedo jugar más esta semana?"]),
dict(slug="verano",arq="La Madre",fase="Fase ovulatoria",est="Verano interior",dias="Días 13 a 16 aprox.",
 sub="La que florece y da",
 intro="La Madre es la energía de la plenitud. Tu cuerpo está en su punto más fértil y luminoso: magnética, generosa, abierta al encuentro. No se trata solo de dar vida a un bebé: es tu capacidad de crear, nutrir, amar y brillar.",
 corr=[("Elemento","Fuego"),("Luna","Luna llena"),("Dirección","Sur"),("Cristal","Cornalina o citrino"),("Colores","Dorado y naranja"),("Plantas","Rosa, miel y frutos rojos")],
 inv="Madre que vive en mí, florece. Mi cuerpo es abundante, mi placer es sagrado y mi luz es un regalo. Me abro a dar y a recibir.",
 nombre="La bendición del espejo y la miel",
 pasos=['Ponte frente al espejo con algo que te haga sentir hermosa y mírate a los ojos.', 'Di tu invocación en voz alta.', 'Pon una gota de miel en tus labios: «Me endulzo la vida. Merezco el placer».', 'Con un aceite, masajea tu cuello, pechos, vientre y caderas, bendiciendo cada parte.', 'Dile al espejo tres cosas que admiras de ti.'],
 beb=("Néctar de la Madre","Agua de coco o agua con frutos rojos, pepino y hojas de albahaca. Brinda contigo misma antes de beber."),
 ali=("Comida que irradia","Verduras de colores, pescado, frutas, aguacate y semillas de girasol. Sirve tu plato bonito, como una ofrenda para ti."),
 mov=("Movimiento de fuego","Baile sensual, cardio, natación o un entrenamiento fuerte. Tu cuerpo tiene energía para brillar."),
 afir="Soy abundante. Mi luz, mi placer y mi amor son sagrados.",
 preg=["¿Qué estoy creando y nutriendo en mi vida?","¿Dónde quiero poner mi luz este mes?","¿Cómo puedo recibir más placer?"]),
dict(slug="otono",arq="La Hechicera",fase="Fase lútea",est="Otoño interior",dias="Del día 17 hasta tu menstruación",
 sub="La que ve la verdad",
 intro="La Hechicera es la mujer salvaje y honesta. Cuando tu energía baja, cae también el velo de la complacencia: ves con claridad lo que no funciona, lo que te duele y lo que ya no vas a tolerar. Su poder no es la dulzura, es la verdad.",
 corr=[("Elemento","Tierra"),("Luna","Luna menguante"),("Dirección","Oeste"),("Cristal","Amatista u obsidiana"),("Colores","Morado y vino"),("Plantas","Manzanilla, cacao y lavanda")],
 inv="Hechicera que vive en mí, te honro. No temo a mi sombra ni a mi rabia: son mi brújula. Corto lo que me drena y protejo mi energía.",
 nombre="Corte de lazos con sal y agua",
 pasos=['Pon tus pies o tus manos en agua tibia con un puñado de sal y respira.', 'Di tu invocación en voz alta, con fuerza.', 'Escribe sin filtro lo que te molesta: tu enojo es información.', 'Ata un hilo a tu muñeca, nombra lo que quieres soltar y córtalo: «Te devuelvo lo que no es mío. Recupero mi energía».', 'Bota el agua con sal fuera de casa y elige un límite amoroso para esta semana.'],
 beb=("Poción de la Hechicera","Chocolate caliente con cacao puro, canela y una pizca de sal, o una manzanilla con lavanda antes de dormir para calmar el cuerpo."),
 ali=("Comida que calma la tormenta","Banano, aguacate, frutos secos, avena y cacao, ricos en magnesio. Reduce el azúcar, la cafeína, la sal y el alcohol antes de menstruar."),
 mov=("Movimiento de la tierra","Yoga suave, caminatas al atardecer o pisar la tierra descalza. Si sientes rabia, sacude todo tu cuerpo durante dos minutos y suelta un sonido fuerte."),
 afir="Mi sensibilidad es sabiduría. Digo mi verdad y protejo mi energía.",
 preg=["¿Qué me está molestando y qué me quiere enseñar?","¿Qué límite necesito poner?","¿Qué verdad me estoy callando?"]),
]
json.dump(R,open("rituales.json","w"),ensure_ascii=False)
CSS='''@font-face{font-family:"PenGram";src:url(../../brand/fonts/BNPenAndGram-Light.otf);font-weight:300}
@font-face{font-family:"PenGram";src:url(../../brand/fonts/BNPenAndGram-Bold.otf);font-weight:700}
@font-face{font-family:"Aire";src:url(../../brand/fonts/Aire-Bold-Italic-Pro.ttf)}
@font-face{font-family:"Emilia";src:url(../../brand/fonts/Emilia-Romagna.otf)}
@page{size:8.5in 11in;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"PenGram",sans-serif;font-weight:300;color:#3b1d20}
.p{width:8.5in;height:11in;position:relative;overflow:hidden;break-after:page;display:flex;flex-direction:column;padding:.55in .7in .45in}
.dark{background:radial-gradient(ellipse at 50% 22%,#7a1d2c 0,#4a0e19 45%,#22060c 100%);color:#f4e6d6}
.light{background:#f7f1ea}
.stars{position:absolute;inset:0;pointer-events:none}
.top{display:flex;justify-content:space-between;align-items:center;position:relative}
.top img{height:.5in}
.top .by{font-family:"Emilia";font-size:19pt}
.dark .by{color:#e3c08f}.light .by{color:#741420}
.emb{width:2.6in;margin:.25in auto 0;position:relative}
.emb svg{width:100%;display:block}
.k{text-align:center;font-weight:700;letter-spacing:.32em;text-transform:uppercase;font-size:9pt;color:#e3c08f;margin-top:.22in}
h1{text-align:center;font-family:"Aire";font-weight:400;font-size:52pt;line-height:1;margin-top:.04in}
.sub{text-align:center;font-family:"Aire";font-size:18pt;color:#e3c08f}
.d{text-align:center;font-size:9.5pt;letter-spacing:.12em;margin-top:.06in;opacity:.8}
.intro{font-size:12pt;line-height:1.55;text-align:center;max-width:6.2in;margin:.22in auto 0}
.corr{display:grid;grid-template-columns:repeat(3,1fr);gap:.12in .2in;margin-top:.28in;border-top:1px solid rgba(227,192,143,.45);border-bottom:1px solid rgba(227,192,143,.45);padding:.16in 0}
.corr div{text-align:center}
.corr b{display:block;font-weight:700;font-size:7.5pt;letter-spacing:.24em;text-transform:uppercase;color:#e3c08f}
.corr span{font-size:11pt}
.inv{margin-top:.26in;text-align:center}
.inv b{display:block;font-weight:700;font-size:8pt;letter-spacing:.28em;text-transform:uppercase;color:#e3c08f;margin-bottom:.08in}
.inv p{font-family:"Aire";font-size:17pt;line-height:1.35;max-width:6.3in;margin:0 auto}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;font-size:8.5pt;position:relative}
.dark .foot{color:#d9c3b0}.light .foot{color:#7a6457}
.foot .s{font-family:"Aire";font-size:21pt}
.dark .foot .s{color:#e3c08f}.light .foot .s{color:#741420}
.lk{font-weight:700;letter-spacing:.3em;text-transform:uppercase;font-size:9pt;color:#9a8270;margin-top:.28in}
h2{font-family:"Aire";font-weight:400;font-size:30pt;color:#741420;line-height:1.05}
ol{margin-top:.14in;padding-left:.28in;display:grid;gap:.07in;font-size:11pt;line-height:1.45}
ol li::marker{font-family:"Aire";color:#741420;font-size:13pt}
.trio{display:grid;grid-template-columns:repeat(3,1fr);gap:.22in;margin-top:.26in}
.trio h3{font-weight:700;font-size:8pt;letter-spacing:.22em;text-transform:uppercase;color:#741420}
.trio h4{font-family:"Aire";font-weight:400;font-size:14pt;margin:.03in 0}
.trio p{font-size:10pt;line-height:1.42}
.af{margin-top:.24in;background:linear-gradient(135deg,#5a1220,#2a0810);color:#f7f1ea;border-radius:.18in;padding:.18in .3in;text-align:center}
.af span{display:block;font-weight:700;letter-spacing:.25em;font-size:8pt;text-transform:uppercase;color:#e3c08f;margin-bottom:.04in}
.af p{font-family:"Aire";font-size:18pt;line-height:1.25}
.j{margin-top:.2in}
.j h3{font-weight:700;font-size:8pt;letter-spacing:.22em;text-transform:uppercase;color:#741420;margin-bottom:.06in}
.j ul{list-style:none;display:grid;gap:.04in}
.j li{font-size:10.5pt}
.ln{display:block;border-bottom:1px solid #cdb8a6;height:.24in}
'''
import random
def stars(seed):
    r=random.Random(seed);s=[]
    for _ in range(90):
        s.append(f'<circle cx="{r.uniform(0,816):.0f}" cy="{r.uniform(0,1056):.0f}" r="{r.choice([.6,.9,1.2,1.6])}" fill="#f4e6d6" opacity="{r.uniform(.2,.8):.2f}"/>')
    return f'<svg class="stars" viewBox="0 0 816 1056" preserveAspectRatio="none">{"".join(s)}</svg>'
for r in R:
    e=html.escape
    corr="".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a,b in r["corr"])
    ol="".join(f"<li>{e(x)}</li>" for x in r["pasos"])
    trio="".join(f"<div><h3>{t}</h3><h4>{e(a)}</h4><p>{e(b)}</p></div>" for t,(a,b) in [("Bebida sagrada",r["beb"]),("Alimento sagrado",r["ali"]),("Movimiento sagrado",r["mov"])])
    pq="".join(f"<li>{e(x)}<span class='ln'></span></li>" for x in r["preg"])
    doc=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<section class="p dark">{stars(r["slug"])}
 <div class="top"><img src="../../brand/logos/logo-crema.png" alt="Alma Sana"><span class="by">by Dei</span></div>
 <div class="emb">{E[r["slug"]]}</div>
 <p class="k">Ritual · {e(r["fase"])}</p>
 <h1>{e(r["arq"])}</h1>
 <p class="sub">{e(r["sub"])}</p>
 <p class="d">{e(r["est"])} · {e(r["dias"])}</p>
 <p class="intro">{e(r["intro"])}</p>
 <div class="corr">{corr}</div>
 <div class="inv"><b>Invocación · dila en voz alta</b><p>«{e(r["inv"])}»</p></div>
 <div class="foot"><div>@almasana111</div><div class="s">Con amor, Dei</div></div>
</section>
<section class="p light">
 <div class="top"><img src="../../brand/logos/logo-vino.png" alt="Alma Sana"><span class="by">by Dei</span></div>
 <p class="lk">Ritual central</p>
 <h2>{e(r["nombre"])}</h2>
 <ol>{ol}</ol>
 <div class="trio">{trio}</div>
 <div class="af"><span>Tu afirmación</span><p>{e(r["afir"])}</p></div>
 <div class="j"><h3>Para tu journal</h3><ul>{pq}</ul></div>
 <div class="foot"><div>Este ritual es una práctica de autocuidado y no sustituye la atención médica.<br>@almasana111 · WhatsApp +57 301 338 8823</div><div class="s">Con amor, Dei</div></div>
</section></body></html>'''
    open(f"rituales/{r['slug']}.html","w").write(doc)
print("ok")
