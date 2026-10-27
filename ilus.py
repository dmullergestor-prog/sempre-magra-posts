# Ilustrações vetoriais originais do ebook "Shape no Bolso"
G = "#1f6f4a"; G2 = "#2f8f5f"; LIME = "#d4ea6b"; CORAL = "#f0694a"; INK = "#1d2a24"
CREAM = "#faf6ee"; SAND = "#efe6d4"; YEL = "#f6c945"; BROWN = "#8a5a3b"; MUTED = "#5d6b63"


def svg(w, h, body, vb=None, cls="ilus"):
    vb = vb or f"0 0 {w} {h}"
    return f'<svg class="{cls}" viewBox="{vb}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">{body}</svg>'


# ---------- alimentos (viewBox 100x100) ----------
def _egg():
    return (f'<ellipse cx="50" cy="56" rx="26" ry="32" fill="#fff6e6" stroke="{INK}" stroke-width="3"/>'
            f'<ellipse cx="41" cy="44" rx="6" ry="9" fill="#fff" opacity=".9"/>')

def _fried_egg():
    return (f'<path d="M20 52 C14 30 40 22 52 28 C70 20 88 36 82 54 C88 72 66 84 50 78 C32 86 12 72 20 52Z" fill="#fff" stroke="{INK}" stroke-width="3"/>'
            f'<circle cx="52" cy="52" r="14" fill="{YEL}" stroke="{INK}" stroke-width="3"/><circle cx="47" cy="47" r="4" fill="#fff" opacity=".7"/>')

def _banana():
    return (f'<path d="M18 30 C22 70 60 86 86 62 C88 58 84 56 80 58 C58 72 34 60 28 30 C27 24 19 24 18 30Z" fill="{YEL}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
            f'<path d="M20 28 L18 18 L26 20 Z" fill="{BROWN}" stroke="{INK}" stroke-width="2.5"/>'
            f'<path d="M30 40 C36 58 52 66 70 64" fill="none" stroke="#e0ad2c" stroke-width="3"/>')

def _drumstick():
    return (f'<path d="M30 30 C46 10 80 22 74 46 C70 62 52 64 44 58 L30 72 C34 80 26 86 20 80 C14 84 8 76 14 72 C8 66 16 58 22 64 L36 50 C26 44 24 36 30 30Z" fill="#c9743f" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
            f'<path d="M24 66 L36 54" stroke="#fff6e6" stroke-width="7" stroke-linecap="round"/>'
            f'<path d="M48 26 C58 22 68 28 68 38" fill="none" stroke="#e59a63" stroke-width="4" stroke-linecap="round"/>')

def _bowl(fill_body, top):
    return (top + f'<path d="M14 50 L86 50 C86 72 70 86 50 86 C30 86 14 72 14 50Z" fill="{fill_body}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
            f'<path d="M22 58 C30 70 44 74 56 74" fill="none" stroke="#fff" stroke-width="3" opacity=".5"/>')

def _beans():
    dots = "".join(f'<ellipse cx="{x}" cy="{y}" rx="6" ry="4.2" fill="#6b3b24" stroke="{INK}" stroke-width="1.6" transform="rotate({r} {x} {y})"/>'
                   for x, y, r in [(30,46,20),(42,40,-10),(55,44,30),(68,46,-20),(36,50,0),(50,49,10),(62,50,-30),(46,36,40),(58,37,0)])
    top = f'<ellipse cx="50" cy="48" rx="36" ry="10" fill="#7d4a2e" stroke="{INK}" stroke-width="3"/>' + dots
    return _bowl("#e9a26b", top)

def _rice():
    grains = "".join(f'<ellipse cx="{x}" cy="{y}" rx="3.2" ry="1.6" fill="#fff" stroke="#c9c2b2" stroke-width=".8" transform="rotate({r} {x} {y})"/>'
                     for x, y, r in [(30,42,10),(38,36,-20),(48,32,30),(58,35,-10),(66,40,20),(42,44,0),(54,42,40),(62,46,-30),(34,48,20),(50,38,-40),(70,47,0),(46,48,10)])
    top = f'<path d="M18 50 C20 30 80 30 82 50 Z" fill="#fbf7ee" stroke="{INK}" stroke-width="3"/>' + grains
    return _bowl("#7fb7d6", top)

def _oats():
    return (f'<rect x="26" y="26" width="48" height="62" rx="8" fill="#f3e3c1" stroke="{INK}" stroke-width="3"/>'
            f'<rect x="22" y="16" width="56" height="14" rx="4" fill="{G2}" stroke="{INK}" stroke-width="3"/>'
            f'<rect x="32" y="46" width="36" height="22" rx="3" fill="#fff" stroke="{INK}" stroke-width="2"/>'
            f'<text x="50" y="61" font-family="Poppins" font-weight="700" font-size="10" text-anchor="middle" fill="{INK}">AVEIA</text>'
            + "".join(f'<ellipse cx="{x}" cy="{y}" rx="3" ry="2" fill="#d9bf86"/>' for x, y in [(34,78),(44,80),(56,77),(66,80),(38,36),(62,38)]))

def _milk():
    return (f'<path d="M30 34 L50 16 L70 34 L70 88 L30 88 Z" fill="#fff" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
            f'<path d="M30 34 L70 34" stroke="{INK}" stroke-width="3"/>'
            f'<rect x="30" y="50" width="40" height="22" fill="#7fb7d6" stroke="{INK}" stroke-width="2"/>'
            f'<text x="50" y="65" font-family="Poppins" font-weight="700" font-size="9.5" text-anchor="middle" fill="#fff">LEITE</text>')

def _sweet_potato():
    return (f'<path d="M14 58 C10 40 36 30 56 32 C76 34 92 44 86 60 C80 74 52 78 34 74 C22 72 16 66 14 58Z" fill="#a0567a" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M86 52 L95 50" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
            + "".join(f'<path d="M{x} {y} q3 2 6 0" fill="none" stroke="#7a3b5a" stroke-width="2.5" stroke-linecap="round"/>' for x, y in [(30,50),(48,44),(62,58),(40,64),(70,48)]))

def _liver():
    return (f'<path d="M14 50 C14 32 44 26 60 30 C78 34 90 40 86 54 C82 68 60 64 50 72 C38 80 14 70 14 50Z" fill="#8c2f2f" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M26 44 C34 38 48 36 56 40" fill="none" stroke="#c25a5a" stroke-width="4" stroke-linecap="round"/>')

def _sardine():
    return (f'<path d="M10 50 C24 34 58 32 76 50 C58 66 24 66 10 50Z" fill="#b8c6cf" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M74 50 L92 36 L90 64 Z" fill="#9aaab4" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
            f'<circle cx="24" cy="48" r="3.5" fill="{INK}"/><path d="M34 42 C38 48 38 54 34 58" fill="none" stroke="{INK}" stroke-width="2"/>'
            f'<path d="M20 54 C40 60 58 58 70 52" fill="none" stroke="#e8eef2" stroke-width="3"/>')

def _pts():
    return (f'<path d="M24 22 L76 22 L82 88 L18 88 Z" fill="#e7cf98" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
            f'<path d="M24 22 L30 14 L70 14 L76 22" fill="#d4b874" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
            f'<circle cx="50" cy="52" r="17" fill="{G2}" stroke="{INK}" stroke-width="2.5"/>'
            f'<text x="50" y="57" font-family="Poppins" font-weight="800" font-size="12" text-anchor="middle" fill="#fff">PTS</text>'
            f'<text x="50" y="80" font-family="Inter" font-weight="700" font-size="7.5" text-anchor="middle" fill="{INK}">SOJA</text>')

def _peanut():
    return (f'<path d="M30 30 C42 18 58 26 56 40 C54 48 60 52 66 56 C80 64 72 86 56 82 C46 80 44 70 38 64 C32 60 20 58 20 46 C20 38 24 34 30 30Z" fill="#d9a865" stroke="{INK}" stroke-width="3"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#b07c3d"/>' for x, y in [(34,38),(42,32),(30,48),(60,66),(66,74),(56,72)]))

def _cabbage():
    return (f'<circle cx="50" cy="54" r="32" fill="#9fcf6a" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M50 24 C40 40 40 70 50 86 M50 24 C62 40 62 70 50 86" fill="none" stroke="#6ea83d" stroke-width="3"/>'
            f'<path d="M22 46 C34 50 40 60 38 76 M78 46 C66 50 60 60 62 76" fill="none" stroke="#6ea83d" stroke-width="3"/>')

def _carrot():
    return (f'<path d="M30 30 L78 74 C82 78 78 84 72 80 L24 40 C20 34 26 26 30 30Z" fill="{CORAL}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
            f'<path d="M28 32 C20 18 12 20 10 22 M28 32 C24 16 30 10 34 10 M28 32 C14 28 12 34 12 36" fill="none" stroke="{G2}" stroke-width="4" stroke-linecap="round"/>'
            f'<path d="M44 46 l6 -4 M56 56 l6 -4 M66 66 l5 -3" stroke="#c4462e" stroke-width="2.5" stroke-linecap="round"/>')

def _bread():
    return (f'<path d="M12 58 C10 38 30 30 50 30 C70 30 90 38 88 58 C86 70 70 72 50 72 C30 72 14 70 12 58Z" fill="#e3a95c" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M30 40 C36 46 38 54 36 62 M48 36 C54 44 56 54 52 64 M66 40 C72 46 72 54 68 62" fill="none" stroke="#f6d7a0" stroke-width="3.5" stroke-linecap="round"/>')

def _lentil():
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#c67b3c" stroke="{INK}" stroke-width="1.4"/>'
                   for x, y in [(30,46),(40,42),(52,40),(64,42),(72,47),(36,50),(48,48),(60,49),(46,36),(56,34)])
    top = f'<ellipse cx="50" cy="48" rx="36" ry="10" fill="#b5652e" stroke="{INK}" stroke-width="3"/>' + dots
    return _bowl("#f2d08a", top)

FOODS = dict(egg=_egg, fried_egg=_fried_egg, banana=_banana, drumstick=_drumstick, beans=_beans, rice=_rice,
             oats=_oats, milk=_milk, sweet_potato=_sweet_potato, liver=_liver, sardine=_sardine, pts=_pts,
             peanut=_peanut, cabbage=_cabbage, carrot=_carrot, bread=_bread, lentil=_lentil)

def food(name, size=64, bg=None):
    inner = FOODS[name]()
    back = f'<circle cx="50" cy="50" r="48" fill="{bg}"/>' if bg else ""
    return svg(size, size, back + inner, vb="0 0 100 100")


# ---------- capa ----------
def cover_art():
    body = (
        f'<circle cx="200" cy="200" r="185" fill="{LIME}" opacity=".35"/>'
        f'<circle cx="200" cy="200" r="150" fill="#fff" stroke="{INK}" stroke-width="5"/>'
        f'<circle cx="200" cy="200" r="122" fill="none" stroke="{SAND}" stroke-width="10"/>'
        # arroz
        f'<path d="M110 196 C104 140 170 110 200 140 L200 200 Z" fill="#fbf7ee" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'
        + "".join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="2.4" fill="#fff" stroke="#cfc7b6" stroke-width="1" transform="rotate({r} {x} {y})"/>'
                  for x, y, r in [(140,170,10),(160,156,-20),(180,150,30),(150,186,0),(172,176,40),(188,170,-10),(130,186,20),(186,190,0)]) +
        # feijão
        f'<path d="M200 140 C236 112 296 140 290 196 L200 200 Z" fill="#7d4a2e" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'
        + "".join(f'<ellipse cx="{x}" cy="{y}" rx="7" ry="5" fill="#5e321c" stroke="{INK}" stroke-width="1.5" transform="rotate({r} {x} {y})"/>'
                  for x, y, r in [(226,160,20),(248,150,-10),(262,170,30),(238,182,0),(272,190,-20),(214,186,10),(252,186,40)]) +
        # salada
        f'<path d="M200 200 L290 204 C286 250 250 282 206 286 Z" fill="#9fcf6a" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'
        f'<circle cx="236" cy="236" r="12" fill="{CORAL}" stroke="{INK}" stroke-width="3"/><circle cx="262" cy="222" r="9" fill="{CORAL}" stroke="{INK}" stroke-width="3"/>'
        f'<path d="M220 262 l20 -6 M244 262 l18 -10" stroke="{G}" stroke-width="5" stroke-linecap="round"/>'
        # frango
        f'<g transform="translate(108 196) scale(1.05)">{_drumstick()}</g>'
        # ovo
        f'<g transform="translate(150 228) scale(.62)">{_fried_egg()}</g>'
        # moeda
        f'<g transform="translate(300 54)"><circle cx="40" cy="40" r="40" fill="{YEL}" stroke="{INK}" stroke-width="5"/>'
        f'<circle cx="40" cy="40" r="30" fill="none" stroke="#d9a520" stroke-width="3"/>'
        f'<text x="40" y="50" font-family="Poppins" font-weight="800" font-size="26" text-anchor="middle" fill="{INK}">R$20</text></g>'
        # halter
        f'<g transform="translate(18 300) rotate(-18)"><rect x="0" y="18" width="20" height="44" rx="5" fill="{INK}"/><rect x="20" y="26" width="10" height="28" rx="3" fill="{INK}"/>'
        f'<rect x="30" y="35" width="56" height="10" rx="4" fill="#9aa59f"/><rect x="86" y="26" width="10" height="28" rx="3" fill="{INK}"/><rect x="96" y="18" width="20" height="44" rx="5" fill="{INK}"/></g>'
        # garfo e faca
        f'<g stroke="{INK}" stroke-width="7" stroke-linecap="round"><path d="M22 120 L22 250"/><path d="M12 120 L12 160 M32 120 L32 160 M12 160 C12 172 32 172 32 160"/></g>'
        f'<path d="M378 120 C396 150 394 196 378 206 L378 280" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
    )
    return svg(400, 400, body)


def back_art():
    body = (f'<circle cx="60" cy="60" r="56" fill="{LIME}" opacity=".5"/>'
            f'<g transform="translate(10 10)">{_fried_egg()}</g>')
    return svg(120, 120, body)


# ---------- conceitos ----------
def balance_scale(label_l, label_r, tilt=-8):
    body = (
        f'<path d="M150 40 L150 200" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
        f'<path d="M110 206 L190 206" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>'
        f'<circle cx="150" cy="40" r="9" fill="{CORAL}" stroke="{INK}" stroke-width="3"/>'
        f'<g transform="rotate({tilt} 150 46)">'
        f'<path d="M40 46 L260 46" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
        f'<path d="M40 46 L16 110 M40 46 L64 110 M260 46 L236 110 M260 46 L284 110" stroke="{MUTED}" stroke-width="2.5"/>'
        f'<path d="M8 110 L72 110 C70 128 56 136 40 136 C24 136 10 128 8 110Z" fill="{LIME}" stroke="{INK}" stroke-width="4"/>'
        f'<path d="M228 110 L292 110 C290 128 276 136 260 136 C244 136 230 128 228 110Z" fill="{CORAL}" stroke="{INK}" stroke-width="4"/>'
        f'<g transform="translate(18 66) scale(.42)">{_drumstick()}</g>'
        f'<g transform="translate(236 70) scale(.4)"><path d="M50 10 C60 30 80 40 72 64 C66 82 34 82 28 64 C20 40 40 30 50 10Z" fill="{YEL}" stroke="{INK}" stroke-width="5"/></g>'
        f'<text x="40" y="160" font-family="Poppins" font-weight="700" font-size="15" text-anchor="middle" fill="{INK}">{label_l}</text>'
        f'<text x="260" y="160" font-family="Poppins" font-weight="700" font-size="15" text-anchor="middle" fill="{INK}">{label_r}</text>'
        f'</g>')
    return svg(300, 215, body)


def macro_plate():
    # prato dividido: metade vegetais, 1/4 proteína, 1/4 carbo
    body = (
        f'<circle cx="130" cy="130" r="120" fill="#fff" stroke="{INK}" stroke-width="5"/>'
        f'<path d="M130 130 L130 18 A112 112 0 0 0 130 242 Z" fill="#b9de87" stroke="{INK}" stroke-width="3"/>'
        f'<path d="M130 130 L130 18 A112 112 0 0 1 242 130 Z" fill="#e8b48a" stroke="{INK}" stroke-width="3"/>'
        f'<path d="M130 130 L242 130 A112 112 0 0 1 130 242 Z" fill="#f6e7c2" stroke="{INK}" stroke-width="3"/>'
        f'<text x="76" y="126" font-family="Poppins" font-weight="700" font-size="15" text-anchor="middle" fill="{INK}">½ VEGETAIS</text>'
        f'<text x="76" y="144" font-family="Inter" font-size="11.5" text-anchor="middle" fill="{INK}">fibra, volume,</text>'
        f'<text x="76" y="158" font-family="Inter" font-size="11.5" text-anchor="middle" fill="{INK}">saciedade</text>'
        f'<text x="182" y="86" font-family="Poppins" font-weight="700" font-size="14" text-anchor="middle" fill="{INK}">¼ PROTEÍNA</text>'
        f'<text x="182" y="102" font-family="Inter" font-size="11" text-anchor="middle" fill="{INK}">frango, ovo,</text>'
        f'<text x="182" y="115" font-family="Inter" font-size="11" text-anchor="middle" fill="{INK}">fígado, soja</text>'
        f'<text x="180" y="176" font-family="Poppins" font-weight="700" font-size="14" text-anchor="middle" fill="{INK}">¼ CARBO</text>'
        f'<text x="180" y="192" font-family="Inter" font-size="11" text-anchor="middle" fill="{INK}">arroz, feijão,</text>'
        f'<text x="180" y="205" font-family="Inter" font-size="11" text-anchor="middle" fill="{INK}">batata-doce</text>'
    )
    return svg(260, 260, body)


def donut(parts, size=200, hole=58, title=""):
    import math
    total = sum(v for _, v, _ in parts)
    cx = cy = size / 2; r = size / 2 - 8; a0 = -math.pi / 2; out = ""
    for _, v, col in parts:
        a1 = a0 + 2 * math.pi * v / total
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        large = 1 if a1 - a0 > math.pi else 0
        out += f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {large} 1 {x1:.1f} {y1:.1f} Z" fill="{col}" stroke="#fff" stroke-width="3"/>'
        a0 = a1
    out += f'<circle cx="{cx}" cy="{cy}" r="{hole}" fill="{CREAM}"/>'
    out += f'<text x="{cx}" y="{cy-2}" font-family="Poppins" font-weight="800" font-size="26" text-anchor="middle" fill="{INK}">{title}</text>'
    out += f'<text x="{cx}" y="{cy+18}" font-family="Inter" font-size="11" text-anchor="middle" fill="{MUTED}">por dia</text>'
    return svg(size, size, out)


def hbar_chart(rows, width=440, unit="R$", highlight=3):
    # rows: (label, value)
    mx = max(v for _, v in rows); bh = 22; gap = 8; lw = 150
    h = len(rows) * (bh + gap) + 10; out = ""
    for i, (lab, v) in enumerate(rows):
        y = i * (bh + gap) + 4
        w = (width - lw - 70) * v / mx
        col = G2 if i < highlight else ("#c9d3cd" if v > 4.5 else "#9cc2ad")
        out += f'<text x="{lw-10}" y="{y+15.5}" font-family="Inter" font-size="12.5" text-anchor="end" fill="{INK}">{lab}</text>'
        out += f'<rect x="{lw}" y="{y}" width="{w:.1f}" height="{bh}" rx="5" fill="{col}"/>'
        out += f'<text x="{lw+w+8:.1f}" y="{y+15.5}" font-family="Poppins" font-weight="700" font-size="12.5" fill="{INK}">' + f'{unit} {v:.2f}'.replace(".", ",") + '</text>'
    return svg(width, h, out)


def line_chart(values, labels, width=440, height=190, color=G2):
    pad_l, pad_b, pad_t, pad_r = 40, 28, 12, 14
    mn, mx = min(values) - 1, max(values) + 1
    iw, ih = width - pad_l - pad_r, height - pad_t - pad_b
    def X(i): return pad_l + iw * i / (len(values) - 1)
    def Y(v): return pad_t + ih * (mx - v) / (mx - mn)
    out = ""
    for k in range(5):
        v = mn + (mx - mn) * k / 4; y = Y(v)
        out += f'<line x1="{pad_l}" x2="{width-pad_r}" y1="{y:.1f}" y2="{y:.1f}" stroke="#e3dccd" stroke-width="1"/>'
        out += f'<text x="{pad_l-6}" y="{y+4:.1f}" font-family="Inter" font-size="10" text-anchor="end" fill="{MUTED}">{v:.0f}</text>'
    pts = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(values))
    area = f"{X(0):.1f},{pad_t+ih} " + pts + f" {X(len(values)-1):.1f},{pad_t+ih}"
    out += f'<polygon points="{area}" fill="{color}" opacity=".12"/>'
    out += f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>'
    for i, v in enumerate(values):
        out += f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="4" fill="#fff" stroke="{color}" stroke-width="2.5"/>'
    for i, l in enumerate(labels):
        out += f'<text x="{X(i):.1f}" y="{height-8}" font-family="Inter" font-size="10" text-anchor="middle" fill="{MUTED}">{l}</text>'
    return svg(width, height, out)


# ---------- figuras de exercício (viewBox 160x120) ----------
def _fig(head, segs, extra=""):
    s = f'<line x1="6" y1="112" x2="154" y2="112" stroke="#cfc6b4" stroke-width="4" stroke-linecap="round"/>' + extra
    for (x1, y1, x2, y2) in segs:
        s += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
    s += f'<circle cx="{head[0]}" cy="{head[1]}" r="10" fill="{CORAL}" stroke="{INK}" stroke-width="3.5"/>'
    return s

POSES = {
    "agachamento": ((78, 26), [(80, 38, 72, 70), (72, 70, 96, 78), (96, 78, 90, 110), (72, 70, 100, 82), (100, 82, 98, 110), (78, 46, 118, 50)]),
    "flexão": ((32, 70), [(42, 74, 128, 98), (128, 98, 146, 108), (48, 76, 46, 110), (52, 78, 58, 110)]),
    "afundo": ((80, 18), [(80, 30, 80, 66), (80, 66, 108, 72), (108, 72, 108, 110), (80, 66, 60, 90), (60, 90, 40, 108), (80, 40, 70, 62), (80, 40, 92, 62)]),
    "mergulho": ((52, 30), [(54, 42, 58, 76), (58, 76, 108, 78), (108, 78, 114, 110), (56, 48, 40, 64), (40, 64, 34, 80)]),
    "ponte": ((24, 104), [(34, 104, 74, 78), (74, 78, 104, 84), (104, 84, 112, 110), (36, 106, 64, 108)]),
    "prancha": ((30, 72), [(40, 76, 136, 96), (136, 96, 146, 108), (44, 80, 40, 110), (40, 110, 62, 110)]),
    "remada": ((42, 40), [(52, 46, 92, 58), (92, 58, 88, 84), (88, 84, 92, 110), (92, 58, 110, 84), (110, 84, 112, 110), (58, 50, 60, 70), (60, 70, 72, 72)]),
    "superman": ((26, 92), [(36, 98, 108, 104), (108, 104, 146, 92), (30, 92, 6, 82)]),
    "abdominal": ((36, 74), [(42, 84, 72, 106), (72, 106, 100, 82), (100, 82, 118, 108), (44, 82, 64, 70)]),
    "polichinelo": ((80, 18), [(80, 30, 80, 70), (80, 70, 58, 110), (80, 70, 102, 110), (80, 40, 54, 14), (80, 40, 106, 14)]),
}

def exercise(name, size=128, bg="#fff"):
    head, segs = POSES[name]
    extra = ""
    if name == "mergulho":
        extra = f'<rect x="20" y="78" width="40" height="8" rx="3" fill="{SAND}" stroke="{INK}" stroke-width="2.5"/><line x1="26" y1="86" x2="26" y2="112" stroke="{INK}" stroke-width="3"/><line x1="54" y1="86" x2="54" y2="112" stroke="{INK}" stroke-width="3"/>'
    if name == "remada":
        extra = f'<rect x="64" y="66" width="20" height="24" rx="5" fill="{G2}" stroke="{INK}" stroke-width="3"/><path d="M68 66 C68 58 80 58 80 66" fill="none" stroke="{INK}" stroke-width="3"/>'
    back = f'<rect x="0" y="0" width="160" height="120" rx="14" fill="{bg}"/>'
    return svg(size, size * 120 // 160, back + _fig(head, segs, extra), vb="0 0 160 120")


# ---------- vida ----------
def sleep_art():
    body = (f'<circle cx="110" cy="80" r="70" fill="#24384a"/>'
            f'<path d="M126 34 C96 40 84 76 100 104 C112 124 140 128 156 116 C130 118 110 98 112 72 C113 56 118 42 126 34Z" fill="{YEL}" stroke="{INK}" stroke-width="3"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff"/>' for x, y, r in [(70,50,3),(84,112,2.5),(60,90,2),(150,56,2.5),(142,96,2)]) +
            f'<text x="56" y="72" font-family="Poppins" font-weight="800" font-size="20" fill="#fff">Z</text>'
            f'<text x="40" y="52" font-family="Poppins" font-weight="800" font-size="15" fill="#fff" opacity=".8">z</text>')
    return svg(220, 160, body)


def water_art():
    body = ""
    for i in range(8):
        x = 12 + i * 34; full = i < 8
        body += (f'<path d="M{x} 14 L{x+26} 14 L{x+22} 70 L{x+4} 70 Z" fill="#fff" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
                 f'<path d="M{x+2.5} 30 L{x+23.5} 30 L{x+22} 68 L{x+4} 68 Z" fill="#7fb7d6" opacity="{1 if full else .2}"/>')
    return svg(290, 80, body)


def mealprep_art():
    box = lambda x, a, b, c: (
        f'<rect x="{x}" y="30" width="96" height="62" rx="10" fill="#fff" stroke="{INK}" stroke-width="3.5"/>'
        f'<rect x="{x+6}" y="38" width="40" height="46" rx="6" fill="{a}"/>'
        f'<rect x="{x+50}" y="38" width="40" height="21" rx="5" fill="{b}"/>'
        f'<rect x="{x+50}" y="63" width="40" height="21" rx="5" fill="{c}"/>'
        f'<rect x="{x-3}" y="18" width="102" height="14" rx="6" fill="{G2}" stroke="{INK}" stroke-width="3"/>')
    body = box(8, "#fbf7ee", "#7d4a2e", "#c9743f") + box(122, "#a0567a", "#b9de87", "#c9743f") + box(236, "#fbf7ee", "#b5652e", "#8c2f2f")
    return svg(340, 100, body)


def calendar_art(days=30):
    out = ""
    for i in range(days):
        r, c = divmod(i, 7)
        x, y = 4 + c * 62, 4 + r * 46
        done = i < 9
        out += f'<rect x="{x}" y="{y}" width="56" height="40" rx="8" fill="{LIME if done else "#fff"}" stroke="{INK}" stroke-width="2"/>'
        out += f'<text x="{x+8}" y="{y+16}" font-family="Poppins" font-weight="700" font-size="11" fill="{INK}">{i+1}</text>'
        if done:
            out += f'<path d="M{x+26} {y+26} l6 6 l12 -14" fill="none" stroke="{G}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
    return svg(440, 5 * 46 + 4, out)


def tape_art():
    body = (f'<path d="M20 70 C20 30 150 30 150 70 C150 110 20 110 20 70Z" fill="none" stroke="{YEL}" stroke-width="18"/>'
            f'<path d="M20 70 C20 30 150 30 150 70 C150 110 20 110 20 70Z" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="2 8"/>'
            f'<rect x="140" y="56" width="50" height="30" rx="5" fill="{CORAL}" stroke="{INK}" stroke-width="3"/>'
            f'<text x="165" y="76" font-family="Poppins" font-weight="800" font-size="13" text-anchor="middle" fill="#fff">cm</text>')
    return svg(200, 130, body)


def cart_art():
    body = (f'<path d="M10 20 L36 20 L52 92 L140 92 L156 40 L44 40" fill="none" stroke="{INK}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>'
            f'<circle cx="62" cy="110" r="9" fill="{INK}"/><circle cx="130" cy="110" r="9" fill="{INK}"/>'
            f'<g transform="translate(46 4) scale(.42)">{_milk()}</g>'
            f'<g transform="translate(78 20) scale(.36)">{_beans()}</g>'
            f'<g transform="translate(106 14) scale(.4)">{_banana()}</g>'
            f'<g transform="translate(124 34) scale(.32)">{_carrot()}</g>')
    return svg(170, 125, body)


def check_icon(ok=True):
    if ok:
        b = f'<circle cx="12" cy="12" r="11" fill="{G2}"/><path d="M7 12.5 l3.4 3.4 L17 9" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
    else:
        b = f'<circle cx="12" cy="12" r="11" fill="{CORAL}"/><path d="M8 8 L16 16 M16 8 L8 16" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
    return svg(22, 22, b, vb="0 0 24 24", cls="ic")
