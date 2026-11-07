import random, html
def stars(seed):
    r=random.Random(seed)
    return "".join(f'<circle cx="{r.uniform(0,1080):.0f}" cy="{r.uniform(0,1350):.0f}" r="{r.choice([.7,1,1.4])}" fill="#f4e6d6" opacity="{r.uniform(.15,.55):.2f}"/>' for _ in range(100))
HEAD='''<!doctype html><html lang="es"><head><meta charset="utf-8"><style>
@font-face{font-family:"PenGram";src:url(../../brand/fonts/BNPenAndGram-Light.otf);font-weight:300}
@font-face{font-family:"PenGram";src:url(../../brand/fonts/BNPenAndGram-Bold.otf);font-weight:700}
@font-face{font-family:"Aire";src:url(../../brand/fonts/Aire-Bold-Italic-Pro.ttf)}
@font-face{font-family:"Emilia";src:url(../../brand/fonts/Emilia-Romagna.otf)}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden;position:relative;color:#f4e6d6;font-family:"PenGram",sans-serif;font-weight:300;background:radial-gradient(ellipse at 45% 40%,#7a1d2c 0,#4a0e19 50%,#22060c 100%)}
.st{position:absolute;inset:0}
.top{position:absolute;left:60px;right:60px;top:48px;display:flex;justify-content:space-between;align-items:center}
.top img{height:70px} .top span{font-family:"Emilia";color:#e3c08f;font-size:34px}
.k{position:absolute;left:60px;top:150px;font-weight:700;letter-spacing:.32em;text-transform:uppercase;font-size:17px;color:#e3c08f}
h1{position:absolute;left:56px;top:180px;font-family:"Aire";font-weight:400;font-size:72px;line-height:1}
.sub{position:absolute;left:60px;top:268px;font-size:22px;color:#e9d6c4}
.lbl text{font-family:"PenGram";fill:#f4e6d6}
.lbl .t{font-weight:700;font-size:21px;fill:#e3c08f}
.lbl .d{font-size:16.5px}
.lbl line,.lbl polyline{stroke:#e3c08f;stroke-width:1.4;fill:none}
.lbl circle{fill:#e3c08f}
.facts{position:absolute;left:60px;right:60px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.f{border:1px solid rgba(227,192,143,.4);border-radius:18px;padding:16px 18px;background:rgba(34,6,12,.4)}
.f b{display:block;font-family:"Aire";font-weight:400;font-size:38px;color:#e3c08f;line-height:1.05}
.f p{font-size:15.5px;line-height:1.36;color:#e9d6c4;margin-top:4px}
.foot{position:absolute;left:60px;right:60px;bottom:36px;display:flex;justify-content:space-between;align-items:flex-end;font-size:14.5px;color:#d9c3b0}
.foot .s{font-family:"Aire";font-size:30px;color:#e3c08f}
</style></head><body>'''
def label(x,y,tx,ty,t,d,anchor="start"):
    lines="".join(f'<tspan x="{tx}" dy="{0 if i==0 else 20}">{html.escape(s)}</tspan>' for i,s in enumerate(d))
    mid=(tx-8 if anchor=="start" else tx+8)
    return f'<g class="lbl"><circle cx="{x}" cy="{y}" r="4"/><polyline points="{x},{y} {mid},{ty-6} {tx-(4 if anchor=="start" else -4)},{ty-6}"/><text class="t" x="{tx}" y="{ty}" text-anchor="{anchor}">{html.escape(t)}</text><text class="d" x="{tx}" y="{ty+22}" text-anchor="{anchor}">{lines}</text></g>'

# ---------- 1. Clítoris ----------
cl=f'''<svg style="position:absolute;left:0;top:300px" width="1080" height="760" viewBox="0 0 1080 760">
<defs>
<linearGradient id="er" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f3b9bc"/><stop offset=".55" stop-color="#d6727c"/><stop offset="1" stop-color="#9c3442"/></linearGradient>
<linearGradient id="bu" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9a1a8"/><stop offset="1" stop-color="#a94352"/></linearGradient>
<radialGradient id="gl" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#ffd9da"/><stop offset=".6" stop-color="#e88a93"/><stop offset="1" stop-color="#b2495a"/></radialGradient>
<filter id="sh"><feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#000" flood-opacity=".35"/></filter>
</defs>
<g filter="url(#sh)">
<!-- pilares / crura -->
<path d="M540 150 C500 175 450 230 400 330 C360 410 320 520 290 640 C286 652 300 660 306 648 C344 540 392 430 438 350 C480 280 520 220 556 186 Z" fill="url(#er)"/>
<path d="M540 150 C580 175 630 230 680 330 C720 410 760 520 790 640 C794 652 780 660 774 648 C736 540 688 430 642 350 C600 280 560 220 524 186 Z" fill="url(#er)"/>
<!-- bulbos -->
<path d="M528 210 C500 250 470 330 452 420 C436 500 450 590 482 610 C512 628 528 580 524 500 C520 420 526 320 540 240 Z" fill="url(#bu)"/>
<path d="M552 210 C580 250 610 330 628 420 C644 500 630 590 598 610 C568 628 552 580 556 500 C560 420 554 320 540 240 Z" fill="url(#bu)"/>
<!-- cuerpo -->
<path d="M512 70 C510 110 518 150 540 172 C562 150 570 110 568 70 C560 52 520 52 512 70 Z" fill="url(#er)"/>
</g>
<!-- glande y capuchón -->
<path d="M506 66 C510 30 570 30 574 66 C566 56 514 56 506 66 Z" fill="#f4e6d6" opacity=".85"/>
<ellipse cx="540" cy="74" rx="20" ry="16" fill="url(#gl)"/>
<ellipse cx="534" cy="69" rx="6" ry="4" fill="#fff" opacity=".6"/>
{label(574,52,760,52,"Capuchón",["Pliegue de piel que protege el glande"])}
{label(558,80,760,112,"Glande",["La única parte visible:","mide de 0,5 a 1 cm"])}
{label(560,130,760,200,"Cuerpo",["2 a 4 cm; se dobla hacia","atrás bajo el pubis"])}
{label(700,380,800,330,"Pilares o raíces",["5 a 9 cm cada uno;","abrazan la vagina"])}
{label(610,520,800,470,"Bulbos vestibulares",["3 a 7 cm; rodean la","entrada de la vagina"])}
<g class="lbl"><text class="t" x="330" y="52" text-anchor="end">Vista frontal</text><text class="d" x="330" y="76" text-anchor="end"><tspan x="330">Así es el clítoris completo:</tspan><tspan x="330" dy="20">casi todo está dentro del cuerpo</tspan></text></g>
<g class="lbl"><text class="d" x="540" y="700" text-anchor="middle" fill-opacity=".8">Ilustración orientativa · las medidas varían en cada mujer</text></g>
</svg>'''
facts=[("9 a 11 cm","Es lo que mide el clítoris completo, sumando glande, cuerpo, pilares y bulbos."),
("+ de 10.000","Fibras nerviosas, según un estudio de 2022. Antes se hablaba de unas 8.000."),
("Solo placer","Es el único órgano del cuerpo humano cuya única función es el placer."),
("Tejido eréctil","Con la excitación se llena de sangre y crece, igual que el pene."),
("Mismo origen","En el embrión, el clítoris y el pene se forman del mismo tejido."),
("1998","La uróloga Helen O'Connell describió por primera vez su anatomía completa.")]
fh="".join(f'<div class="f"><b>{a}</b><p>{html.escape(b)}</p></div>' for a,b in facts)
doc1=HEAD+f'''<svg class="st" viewBox="0 0 1080 1350">{stars(1)}</svg>
<div class="top"><img src="../../brand/logos/logo-crema.png" alt="Alma Sana"><span>by Dei</span></div>
<p class="k">Taller Mujeres salvajes</p><h1>El clítoris completo</h1>
<p class="sub">Lo que vemos es solo la punta: el resto vive dentro de tu cuerpo</p>
{cl}
<div class="facts" style="top:1010px">{fh}</div>
<div class="foot"><div>@almasana111</div><div class="s">Con amor, Dei</div></div></body></html>'''
open("clitoris.html","w").write(doc1)

# ---------- 2. Corte lateral pelvis ----------
pel=f'''<svg style="position:absolute;left:0;top:310px" width="1080" height="900" viewBox="0 0 1080 900">
<defs>
<radialGradient id="ut" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#f6c2c4"/><stop offset=".55" stop-color="#d9727d"/><stop offset="1" stop-color="#8f2c3b"/></radialGradient>
<radialGradient id="ve" cx="40%" cy="35%" r="75%"><stop offset="0" stop-color="#fbe9c8"/><stop offset=".6" stop-color="#e8c27f"/><stop offset="1" stop-color="#a87a35"/></radialGradient>
<linearGradient id="va" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#eaa0a8"/><stop offset="1" stop-color="#a7414f"/></linearGradient>
<radialGradient id="bo" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#fff6ea"/><stop offset="1" stop-color="#cdb8a2"/></radialGradient>
<radialGradient id="ov" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#fbe2d6"/><stop offset="1" stop-color="#c98a7c"/></radialGradient>
<radialGradient id="cl" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#ffd2d5"/><stop offset="1" stop-color="#c0414f"/></radialGradient>
<filter id="sh"><feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000" flood-opacity=".4"/></filter>
</defs>
<!-- silueta del cuerpo -->
<path d="M300 40 C250 200 236 360 262 520 C276 600 300 680 380 760 M780 40 C820 220 820 420 760 560 C720 650 640 720 520 780" fill="none" stroke="#f4e6d6" stroke-opacity=".25" stroke-width="2" stroke-dasharray="6 8"/>
<!-- recto -->
<path d="M660 300 C690 420 672 560 610 700 C604 714 636 724 642 710 C706 566 724 420 696 296 C690 282 656 286 660 300 Z" fill="#a46a6a" opacity=".5"/>
<g filter="url(#sh)">
<!-- hueso púbico -->
<ellipse cx="330" cy="520" rx="34" ry="56" transform="rotate(-25 330 520)" fill="url(#bo)"/>
<!-- vejiga -->
<path d="M318 430 C316 386 372 366 424 380 C470 392 482 440 466 478 C450 516 384 524 348 504 C328 492 320 462 318 430 Z" fill="url(#ve)"/>
<!-- uretra -->
<path d="M404 518 C402 580 396 640 392 690" stroke="#e8c27f" stroke-width="8" fill="none" stroke-linecap="round"/>
<!-- útero -->
<g transform="rotate(-38 530 440)"><path d="M440 250 C446 186 520 160 574 196 C620 228 612 300 580 348 C562 376 552 410 550 440 L512 446 C508 410 496 380 476 356 C446 322 436 290 440 250 Z" fill="url(#ut)"/><ellipse cx="500" cy="240" rx="26" ry="16" fill="#fff" opacity=".18"/></g>
<!-- trompa y ovario -->
<path d="M500 250 C540 210 600 220 620 262" stroke="#e7a3a8" stroke-width="7" fill="none" stroke-linecap="round"/>
<ellipse cx="618" cy="282" rx="22" ry="15" fill="url(#ov)"/>
<!-- vagina -->
<path d="M514 444 C508 520 484 600 450 700 C446 714 478 722 482 708 C512 612 536 528 554 452 C548 436 520 432 514 444 Z" fill="url(#va)"/>
<!-- clítoris -->
<path d="M352 560 C340 600 330 640 344 668 C354 686 370 676 368 656 C366 630 372 600 384 576 Z" fill="url(#cl)"/>
<path d="M380 580 C410 610 430 650 432 700" stroke="#c96370" stroke-width="12" fill="none" stroke-linecap="round" opacity=".85"/>
<ellipse cx="342" cy="676" rx="11" ry="9" fill="#ffc9cd"/>
</g>
<!-- vulva -->
<path d="M330 700 C350 730 380 750 420 752 C450 752 470 740 486 724" fill="none" stroke="#f3b9bc" stroke-width="10" stroke-linecap="round"/>
<path d="M346 704 C366 726 392 738 420 738 C444 738 460 728 470 716" fill="none" stroke="#c96370" stroke-width="6" stroke-linecap="round"/>
{label(470,330,820,110,"Útero",["Del tamaño de una pera;","aquí se forma tu menstruación"])}
{label(618,282,820,215,"Ovario y trompa",["Liberan el óvulo cada ciclo"])}
{label(400,440,250,330,"Vejiga",["Guarda la orina;","está delante del útero"],"end")}
{label(520,560,820,520,"Vagina",["Canal elástico de 7 a 10 cm","que se alarga al excitarse"])}
{label(690,450,820,400,"Recto",["Detrás de la vagina"])}
{label(330,520,250,470,"Hueso púbico",["Protege la vejiga"],"end")}
{label(356,610,250,600,"Clítoris",["El glande asoma fuera;","su cuerpo se esconde dentro"],"end")}
{label(396,640,250,700,"Uretra",["Por aquí sale la orina"],"end")}
{label(440,748,820,700,"Vulva",["Todo lo externo: labios,","entrada de la vagina y glande"])}
<g class="lbl"><text class="d" x="540" y="860" text-anchor="middle">Corte lateral de la pelvis · ilustración orientativa</text></g>
</svg>'''
doc2=HEAD+f'''<svg class="st" viewBox="0 0 1080 1350">{stars(2)}</svg>
<div class="top"><img src="../../brand/logos/logo-crema.png" alt="Alma Sana"><span>by Dei</span></div>
<p class="k">Taller Mujeres salvajes</p><h1>Tu pelvis por dentro</h1>
<p class="sub">Clítoris, vagina, útero, vejiga y vulva: así se ubican en tu cuerpo</p>
{pel}
<div class="foot"><div>Conocer tu cuerpo es el primer acto de amor propio. · @almasana111</div><div class="s">Con amor, Dei</div></div></body></html>'''
open("pelvis.html","w").write(doc2)
