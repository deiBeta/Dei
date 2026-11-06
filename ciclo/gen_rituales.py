import json, html
E=json.load(open("emblemas/emblemas.json"))
R = [
 dict(slug="invierno", arq="La Bruja", fase="Fase menstrual", est="Invierno interior", dias="Días 1 a 5 aprox.",
  intro="Es la sabia que vive en ti. Tu energía va hacia dentro y tu intuición está más despierta que nunca. Es tiempo de soltar, descansar y escucharte.",
  beb=("Infusión de jengibre y canela","Hierve agua con 3 rodajas de jengibre y una rama de canela durante 5 minutos. Bébela despacio, con las dos manos alrededor de la taza, sintiendo el calor en tu vientre."),
  ali=("Comida que abriga","Sopas y caldos, lentejas, frijoles, espinaca y remolacha para reponer hierro. Un pedacito de chocolate oscuro también vale."),
  mov=("Movimiento muy suave","Diez minutos de estiramientos en el piso: postura del niño, rodillas al pecho y círculos de cadera acostada. Nada de exigirte."),
  mom=("Tu momento","Con tu bebida en la mano, escribe qué quieres soltar del mes que termina. Agradécelo y date permiso para descansar un poco más hoy."),
  afir="Me permito descansar. Al soltar, hago espacio para lo nuevo.",
  preg=["¿Qué me pide hoy mi cuerpo?","¿Qué cargué este mes que ya no quiero llevar?","¿Qué me está diciendo mi intuición?"]),
 dict(slug="primavera", arq="La Doncella", fase="Fase folicular", est="Primavera interior", dias="Días 6 a 12 aprox.",
  intro="Es la joven curiosa que vive en ti. Tu energía empieza a subir y vuelven las ganas, las ideas y las ganas de empezar.",
  beb=("Agua tibia con limón y hierbabuena","Al despertar, un vaso de agua tibia con medio limón y unas hojas de hierbabuena. Tómala mirando por la ventana y pensando en una intención para hoy."),
  ali=("Comida fresca y viva","Frutas, ensaladas, semillas, avena y alimentos de colores. Prueba una receta nueva esta semana."),
  mov=("Movimiento con alegría","Pon tu canción favorita y baila libremente, o sal a caminar a paso rápido. Tu cuerpo agradece moverse con energía."),
  mom=("Tu momento","Escribe tres intenciones sencillas para este ciclo, en presente: «Yo elijo…». Ponlas en un lugar donde las veas todos los días."),
  afir="Me abro a lo nuevo. Confío en lo que está naciendo en mí.",
  preg=["¿Qué me gustaría empezar este mes?","¿Qué me da curiosidad ahora mismo?","¿Qué pequeño paso puedo dar hoy?"]),
 dict(slug="verano", arq="La Madre", fase="Fase ovulatoria", est="Verano interior", dias="Días 13 a 16 aprox.",
  intro="Es la mujer que da y florece en ti. Tu energía está en su punto más alto: te sientes radiante, comunicativa y con más deseo.",
  beb=("Agua de frutas o agua de coco","Hidrátate mucho estos días. Prepara una jarra con agua, frutos rojos y rodajas de pepino, o toma agua de coco fresca."),
  ali=("Comida ligera y nutritiva","Verduras crudas, pescado o proteínas ligeras, frutas y semillas de girasol. Comida que te mantenga liviana y con energía."),
  mov=("Movimiento intenso","Es tu mejor momento para el ejercicio fuerte: una clase de baile, correr, nadar o entrenar. Tu cuerpo responde con fuerza."),
  mom=("Tu momento","Mírate al espejo y dite tres cosas que admiras de ti. Elige una conversación, un proyecto o un encuentro al que quieras darle esta energía."),
  afir="Me muestro como soy. Mi energía es un regalo para mí y para el mundo.",
  preg=["¿Qué quiero expresar o comunicar?","¿Con quién quiero compartir mi energía?","¿Cómo celebro mi cuerpo hoy?"]),
 dict(slug="otono", arq="La Hechicera", fase="Fase lútea", est="Otoño interior", dias="Del día 17 hasta tu menstruación",
  intro="Es la mujer intensa y honesta que vive en ti. Tu energía baja poco a poco, tu sensibilidad sube y ves con claridad lo que ya no te sirve.",
  beb=("Chocolate caliente o manzanilla","Un chocolate caliente con cacao puro (rico en magnesio) o una manzanilla antes de dormir para calmar el cuerpo y la mente."),
  ali=("Comida que calma","Banano, aguacate, frutos secos, avena y cacao. Reduce el azúcar, la cafeína, la sal y el alcohol los días antes de menstruar."),
  mov=("Movimiento que suelta","Yoga suave, pilates o una caminata tranquila al atardecer. Si sientes rabia o tensión, sacúdete el cuerpo durante dos minutos."),
  mom=("Tu momento","Escribe todo lo que te molesta, sin juzgarte. Subraya lo que de verdad necesita atención y elige un límite amoroso para esta semana."),
  afir="Mi sensibilidad es sabiduría. Escucho lo que me pide mi cuerpo.",
  preg=["¿Qué me está molestando y qué me quiere decir?","¿Qué límite necesito poner?","¿Qué puedo soltar antes de que llegue mi menstruación?"]),
]
json.dump(R, open("rituales.json","w"), ensure_ascii=False)
for r in R:
    secs="".join(f"<div class='sec'><h2>{t}</h2><h3>{html.escape(a)}</h3><p>{html.escape(b)}</p></div>" for t,(a,b) in [("Tu bebida",r["beb"]),("Tu alimentación",r["ali"]),("Tu movimiento",r["mov"]),(r["mom"][0],(r["arq"]+" en ti",r["mom"][1]))])
    pq = "".join(f"<li>{html.escape(x)}<span class='ln'></span></li>" for x in r["preg"])
    doc = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><style>
@font-face{{font-family:"PenGram";src:url(../../brand/fonts/BNPenAndGram-Light.otf);font-weight:300}}
@font-face{{font-family:"PenGram";src:url(../../brand/fonts/BNPenAndGram-Bold.otf);font-weight:700}}
@font-face{{font-family:"Aire";src:url(../../brand/fonts/Aire-Bold-Italic-Pro.ttf)}}
@font-face{{font-family:"Emilia";src:url(../../brand/fonts/Emilia-Romagna.otf)}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:8.5in;height:11in;background:#f7f1ea;color:#3b1d20;font-family:"PenGram",sans-serif;font-weight:300;position:relative;overflow:hidden}}
.pg{{position:relative;padding:.55in .7in .45in;display:flex;flex-direction:column;height:100%}}
.top{{display:flex;justify-content:space-between;align-items:center}}
.top img{{height:.5in}}
.top .by{{font-family:"Emilia";color:#741420;font-size:19pt}}
.hero{{display:grid;grid-template-columns:2.15in 1fr;gap:.35in;align-items:center;margin-top:.25in}}
.hero svg{{width:2.15in;height:2.15in;display:block}}
.k{{font-weight:700;letter-spacing:.3em;text-transform:uppercase;font-size:9pt;color:#9a8270}}
h1{{font-family:"Aire";font-weight:400;font-size:40pt;color:#741420;line-height:1.02;margin-top:.04in}}
.d{{font-size:10pt;color:#7a6457;margin-top:.04in;font-weight:700;letter-spacing:.06em}}
.intro{{font-size:11.5pt;line-height:1.45;margin-top:.12in}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:.2in .35in;margin-top:.3in}}
.sec h2{{font-weight:700;font-size:9pt;letter-spacing:.22em;text-transform:uppercase;color:#741420}}
.sec h3{{font-family:"Aire";font-weight:400;font-size:15.5pt;color:#3b1d20;margin:.03in 0 .04in}}
.sec p{{font-size:10.8pt;line-height:1.42}}
.af{{margin-top:.28in;background:#5a1220;color:#f7f1ea;border-radius:.18in;padding:.2in .3in;text-align:center}}
.af p{{font-family:"Aire";font-size:18pt;line-height:1.25}}
.af span{{display:block;font-weight:700;letter-spacing:.25em;font-size:8.5pt;text-transform:uppercase;color:#e3c08f;margin-bottom:.05in}}
.j{{margin-top:.24in}}
.j h2{{font-weight:700;font-size:9pt;letter-spacing:.22em;text-transform:uppercase;color:#741420;margin-bottom:.08in}}
.j ul{{list-style:none;display:grid;gap:.08in}}
.j li{{font-size:11pt}}
.ln{{display:block;border-bottom:1px solid #cdb8a6;height:.26in}}
.foot{{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;font-size:8.5pt;color:#7a6457}}
.foot .s{{font-family:"Aire";font-size:21pt;color:#741420}}
</style></head><body><div class="pg">
 <div class="top"><img src="../../brand/logos/logo-vino.png" alt="Alma Sana"><span class="by">by Dei</span></div>
 <div class="hero">{E[r['slug']]}<div>
  <p class="k">Ritual · {html.escape(r['fase'])}</p>
  <h1>{html.escape(r['arq'])}</h1>
  <p class="d">{html.escape(r['est'])} · {html.escape(r['dias'])}</p>
  <p class="intro">{html.escape(r['intro'])}</p></div></div>
 <div class="grid">{secs}</div>
 <div class="af"><span>Tu afirmación</span><p>{html.escape(r['afir'])}</p></div>
 <div class="j"><h2>Para tu journal</h2><ul>{pq}</ul></div>
 <div class="foot"><div>Este ritual es una práctica de autocuidado y no sustituye la atención médica.<br>@almasana111 · WhatsApp +57 301 338 8823</div><div class="s">Con amor, Dei</div></div>
</div></body></html>"""
    open(f"rituales/{r['slug']}.html","w").write(doc)
print("ok")
