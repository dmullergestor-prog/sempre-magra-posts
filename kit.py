"""Gera os 7 slides de um carrossel Sempre Magra a partir de um post.json e renderiza em JPEG 1080x1350.

Uso:  python3 kit.py posts/2026-10-28-07h
      (a pasta precisa ter post.json; saem slide-1.jpg ... slide-7.jpg na mesma pasta)
"""
import html, json, re, sys, pathlib
from ilus import food, exercise, FOODS, POSES

G, G2, LIME, CORAL, INK, CREAM, YEL = "#1f6f4a", "#2f8f5f", "#d4ea6b", "#f0694a", "#1d2a24", "#faf6ee", "#f6c945"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">'

LOGO = (f'<svg viewBox="0 0 200 200" width="54" height="54"><circle cx="100" cy="100" r="78" fill="{CREAM}" stroke="{INK}" stroke-width="7"/>'
        f'<path d="M100 152 C58 124 60 72 100 46 C140 72 142 124 100 152Z" fill="{G2}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
        f'<path d="M100 142 L100 64" stroke="{LIME}" stroke-width="5" stroke-linecap="round"/>'
        f'<circle cx="146" cy="60" r="14" fill="{CORAL}" stroke="{INK}" stroke-width="5"/></svg>')
CHECK = (f'<svg viewBox="0 0 24 24" width="40" height="40" style="flex:0 0 40px"><circle cx="12" cy="12" r="11" fill="{LIME}"/>'
         f'<path d="M7 12.5 l3.4 3.4 L17 9" fill="none" stroke="{INK}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')

CSS = f"""
*{{box-sizing:border-box}} body{{margin:0}}
.s{{width:1080px;height:1350px;padding:84px 88px 72px;font-family:Inter,sans-serif;display:flex;flex-direction:column;overflow:hidden;position:relative}}
.light{{background:{CREAM};color:{INK}}} .dark{{background:{G};color:{CREAM}}}
.top{{display:flex;justify-content:space-between;align-items:center}}
.tag{{font-family:Poppins;font-weight:700;font-size:22px;letter-spacing:.14em;text-transform:uppercase;padding:12px 26px;border-radius:40px}}
.light .tag{{background:{G};color:{LIME}}} .dark .tag{{background:{LIME};color:{INK}}}
.num{{font-family:Poppins;font-weight:700;font-size:26px}} .light .num{{color:{G}}} .dark .num{{color:{LIME}}}
.brand{{display:flex;align-items:center;gap:12px;font-family:Poppins;font-weight:800;font-size:26px;line-height:.9}}
h1,h2{{font-family:Poppins;font-weight:800;letter-spacing:-.015em;margin:52px 0 0}}
h1{{font-size:100px;line-height:.98;margin-top:72px}} h2{{font-size:74px;line-height:1.04}}
.light em{{font-style:normal;color:{G2}}} .dark em{{font-style:normal;color:{LIME}}} strong.c{{color:{CORAL}}}
.body{{margin:26px 0 0;font-size:32px;line-height:1.45}} .light .body{{color:#33423a}} .dark .body{{color:#d8e8d2}}
.card{{background:#fff;border:2px solid #ebe3d2;border-radius:24px;color:{INK}}}
.items{{display:flex;flex-direction:column;gap:16px;margin-top:36px}}
.item{{display:flex;gap:22px;align-items:center;padding:20px 28px}}
.item .n{{flex:0 0 56px;height:56px;border-radius:50%;background:{LIME};font-family:Poppins;font-weight:800;font-size:26px;display:flex;align-items:center;justify-content:center}}
.item span.t{{font-size:29px;line-height:1.35}}
.grid3{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:36px}}
.tile{{padding:20px 16px;display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center}}
.tile b{{font-family:Poppins;font-size:26px}} .tile span{{font-size:23px;line-height:1.3;color:#4c5a52}}
.quote{{margin-top:32px;background:{G};color:#eaf3e0;border-radius:24px;padding:26px 32px;font-size:30px;line-height:1.4}}
.dark .quote{{background:{CREAM};color:{INK}}}
.quote b,.quote em{{color:{LIME}}} .dark .quote b,.dark .quote em{{color:{G}}}
.foot{{display:flex;justify-content:space-between;align-items:center;font-family:Poppins;font-weight:700;font-size:24px;padding-top:24px}}
.light .foot{{color:{G};border-top:2px solid #e3dccd}} .dark .foot{{color:{LIME}}}
.fill{{flex:1}}
table.tb{{width:100%;border-collapse:collapse;font-size:31px}}
.tb th{{font-family:Poppins;font-size:20px;letter-spacing:.1em;text-transform:uppercase;color:#6f7b74;text-align:left;padding:0 0 14px;border-bottom:3px dashed #e3dccd}}
.tb td{{padding:16px 0;border-bottom:2px solid #f3eee4}} .tb td+td,.tb th+th{{text-align:center;width:170px;font-family:Poppins;font-weight:700}}
.tb tr.total td{{background:#fde3db;font-family:Poppins;font-weight:800;border:none;padding:16px 18px}}
.stats{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:28px}}
.stat{{border-radius:24px;padding:26px 16px;text-align:center;font-size:22px}}
.stat b{{display:block;font-family:Poppins;font-size:50px;line-height:1.1}}
.stat.hi{{background:{G};color:#cfe3c2}} .stat.hi b{{color:{LIME}}}
.stat.lo{{background:#fff;border:2px solid #ebe3d2;color:#5d6b63}} .stat.lo b{{color:{G}}}
.disc{{font-size:19px;color:#6f7b74;margin:0 0 16px}} .dark .disc{{color:#cfe3c2}}
.sticker{{position:absolute;border:4px solid {INK};border-radius:18px;padding:18px 30px;font-family:Poppins;font-weight:800;font-size:36px;box-shadow:10px 10px 0 #14523a;white-space:nowrap}}
.bul{{display:flex;flex-direction:column;gap:16px}} .bul div{{display:flex;gap:20px;align-items:center;font-size:29px;line-height:1.3}}
.ctabox{{background:{LIME};color:{INK};border-radius:28px;padding:28px 36px;font-family:Poppins;font-weight:800;font-size:40px;line-height:1.15}}
.ctabox span{{background:{INK};color:{LIME};border-radius:12px;padding:2px 16px}}
.book{{flex:0 0 270px;height:380px;border-radius:10px 22px 22px 10px;background:{CREAM};border:4px solid {INK};box-shadow:18px 18px 0 {LIME};padding:24px 22px;display:flex;flex-direction:column;color:{INK};transform:rotate(3deg)}}
"""

def md(t):
    """*texto* = destaque na cor da marca; !texto! = destaque coral; **x** = negrito."""
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)
    t = re.sub(r"!(.+?)!", r'<strong class="c">\1</strong>', t)
    return t

def icon(name, size=96, bg="#e7f2d6"):
    if name in FOODS: return food(name, size, bg)
    if name in POSES: return exercise(name, int(size * 2.7), bg)
    return ""

def top(sl, i):
    left = sl.get("tag")
    lhtml = (f'<span class="tag">{md(left)}</span>' if left else
             f'<div class="brand">{LOGO}<span>sempre<br>magra<span style="color:{CORAL}">.</span></span></div>')
    return f'<div class="top">{lhtml}<span class="num">{i}/7</span></div>'

def foot(sl, last=False):
    if last: return ""
    return f'<div class="foot"><span>{md(sl.get("rodape", "sempre magra."))}</span><span>Arraste →</span></div>'

def chart(values, color, label_a, label_b, aria):
    mn, mx = min(values), max(values); rng = (mx - mn) or 1
    pts = [(30 + 840 * i / (len(values) - 1), 30 + 190 * (mx - v) / rng) for i, v in enumerate(values)]
    pl = " ".join(f"{x:.0f},{y:.0f}" for x, y in pts)
    area = f"30,236 {pl} 870,236"
    return (f'<svg viewBox="0 0 900 260" width="844" height="244" role="img" aria-label="{html.escape(aria)}">'
            f'<line x1="30" x2="870" y1="236" y2="236" stroke="#e3dccd" stroke-width="2"/>'
            f'<polygon points="{area}" fill="{color}" opacity=".12"/>'
            f'<polyline points="{pl}" fill="none" stroke="{color}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>'
            f'<circle cx="{pts[0][0]:.0f}" cy="{pts[0][1]:.0f}" r="11" fill="#fff" stroke="{color}" stroke-width="5"/>'
            f'<circle cx="{pts[-1][0]:.0f}" cy="{pts[-1][1]:.0f}" r="13" fill="{color}" stroke="{INK}" stroke-width="4"/>'
            f'<text x="30" y="258" font-family="Inter" font-size="20" fill="#5d6b63">{html.escape(label_a)}</text>'
            f'<text x="870" y="258" font-family="Inter" font-size="20" text-anchor="end" fill="#5d6b63">{html.escape(label_b)}</text></svg>')

def render_slide(sl, i):
    t = sl["tipo"]; theme = "dark" if t in ("capa", "cta") or sl.get("escuro") else "light"
    out = top(sl, i)
    if t == "capa":
        out += f'<h1>{md(sl["titulo"])}</h1>'
        if sl.get("texto"): out += f'<p class="body">{md(sl["texto"])}</p>'
        st = sl.get("adesivos", [])[:6]
        pos = [(30, 40, -8), (470, 10, 6), (120, 190, 4), (540, 200, -5), (20, 350, -3), (500, 380, 7)]
        cols = [(CREAM, INK), (YEL, INK), (CREAM, INK), (LIME, INK), (CORAL, "#fff"), (CREAM, INK)]
        out += '<div class="fill" style="position:relative;margin-top:48px">'
        if st:
            out += '<div style="display:flex;flex-wrap:wrap;gap:34px 26px;align-content:flex-start;padding:10px 6px">'
            for k, s in enumerate(st):
                x, y, r = pos[k]; bg, fg = cols[k]
                out += f'<span class="sticker" style="position:static;transform:rotate({r}deg);background:{bg};color:{fg}">{md(s)}</span>'
            out += '</div>'
            if sl.get("arremate"):
                out += f'<span style="position:absolute;right:10px;bottom:6px;transform:rotate(-4deg);font-family:Poppins;font-weight:800;font-size:34px;color:{LIME}">{md(sl["arremate"])}</span>'
        elif sl.get("icones"):
            out += '<div style="display:flex;gap:28px;justify-content:center;align-items:flex-end;height:100%">' + "".join(icon(n, 220, "#2f8f5f") for n in sl["icones"][:3]) + '</div>'
        out += '</div>'
        out += f'<div class="foot"><span>{md(sl.get("rodape", "sempre magra."))}</span><span>Arraste →</span></div>'
    elif t == "cta":
        out += (f'<div style="display:flex;gap:44px;align-items:center;margin-top:52px"><div style="flex:1">'
                f'<h2 style="margin:0;font-size:70px;line-height:1.02">{md(sl["titulo"])}</h2>'
                f'<p class="body">{md(sl.get("texto", "O passo a passo está no guia **Shape no Bolso**."))}</p></div>'
                f'<div class="book"><span style="align-self:flex-start;font-family:Poppins;font-weight:700;font-size:13px;letter-spacing:.12em;text-transform:uppercase;background:{G};color:{LIME};padding:5px 12px;border-radius:20px">Guia prático</span>'
                f'<b style="font-family:Poppins;font-weight:800;font-size:44px;line-height:.95;margin-top:14px;color:{G}">Shape<br>no Bolso</b>'
                f'<span style="font-size:15px;line-height:1.35;margin-top:10px;color:#33423a">Perca gordura e ganhe músculo com comida de verdade</span>'
                f'<div style="flex:1;display:flex;align-items:flex-end;justify-content:center">{food("fried_egg", 110, "#e7f2d6")}</div></div></div>')
        out += f'<p style="margin:52px 0 20px;font-family:Poppins;font-weight:700;font-size:30px;color:{LIME}">No guia você recebe:</p>'
        out += '<div class="bul">' + "".join(f'<div>{CHECK}<span>{md(b)}</span></div>' for b in sl["itens"][:4]) + '</div>'
        out += f'<div class="fill"></div><div class="ctabox">Comente <span>QUERO</span> {md(sl.get("chamada", "e receba o link do guia"))}</div>'
    else:
        out += f'<h2>{md(sl["titulo"])}</h2>'
        if sl.get("texto"): out += f'<p class="body">{md(sl["texto"])}</p>'
        if t == "tabela":
            hd = sl["cabecalho"]
            rows = "".join(f'<tr><td>{md(r[0])}</td>' + "".join(f'<td style="color:{G if k == 0 else "#c4462e"}">{md(c)}</td>' for k, c in enumerate(r[1:])) + '</tr>' for r in sl["linhas"])
            tot = sl.get("total")
            if tot: rows += f'<tr class="total"><td>{md(tot[0])}</td>' + "".join(f'<td style="color:{G if k == 0 else "#9a2f17"}">{md(c)}</td>' for k, c in enumerate(tot[1:])) + '</tr>'
            out += f'<div class="card" style="margin-top:36px;padding:30px 40px"><table class="tb"><tr>' + "".join(f'<th>{md(h)}</th>' for h in hd) + f'</tr>{rows}</table></div>'
        if t in ("grafico", "resultado") and sl.get("valores"):
            cor = CORAL if sl.get("cor") == "coral" else G2
            out += (f'<div class="card" style="margin-top:32px;padding:26px 30px 14px"><div style="display:flex;justify-content:space-between;font-family:Poppins;font-weight:700;font-size:24px;color:#5d6b63;margin-bottom:6px">'
                    f'<span>{md(sl.get("legenda_grafico", ""))}</span><span style="color:{cor}">{md(sl.get("selo_grafico", ""))}</span></div>'
                    f'{chart(sl["valores"], cor, sl.get("inicio", ""), sl.get("fim", ""), sl.get("legenda_grafico", "gráfico"))}</div>')
        if sl.get("blocos"):
            bl = sl["blocos"]
            if all(b.get("icone") for b in bl) and len(bl) == 3:
                out += '<div class="grid3">' + "".join(
                    f'<div class="card tile">{icon(b["icone"], 96)}<b>{md(b["titulo"])}</b>' + (f'<span>{md(b["texto"])}</span>' if b.get("texto") else "") + '</div>' for b in bl) + '</div>'
            else:
                out += '<div class="items">' + "".join(
                    f'<div class="card item"><span class="n">{md(b.get("marca", str(k + 1)))}</span><span class="t"><b>{md(b["titulo"])}</b> {md(b.get("texto", ""))}</span></div>' for k, b in enumerate(bl[:4])) + '</div>'
        if t == "resultado":
            out += '<div class="stats">' + "".join(f'<div class="stat {"hi" if k == 0 else "lo"}"><b>{md(s["valor"])}</b>{md(s["rotulo"])}</div>' for k, s in enumerate(sl["numeros"][:3])) + '</div>'
        if sl.get("citacao"): out += f'<div class="quote">{md(sl["citacao"])}</div>'
        out += '<div class="fill"></div>'
        if t == "resultado" or sl.get("aviso"):
            out += f'<p class="disc">Personagem e resultados ilustrativos. Os resultados variam de pessoa para pessoa.</p>'
        out += foot(sl)
    return f'<section class="s {theme}">{out}</section>'

def build(folder):
    folder = pathlib.Path(folder)
    post = json.loads((folder / "post.json").read_text())
    slides = post["slides"]
    assert len(slides) == 7, "o carrossel precisa ter 7 slides"
    assert slides[-1]["tipo"] == "cta", "o slide 7 precisa ser do tipo cta"
    assert any(s["tipo"] == "resultado" for s in slides), "precisa de um slide de resultado (traz o aviso de ilustrativo)"
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
        problems = []
        for i, sl in enumerate(slides, 1):
            doc = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{render_slide(sl, i)}</body></html>'
            (folder / f"slide-{i}.html").write_text(doc)
            pg.set_content(doc, wait_until="networkidle"); pg.wait_for_timeout(300)
            over = pg.evaluate("""() => { const s=document.querySelector('.s'); const r=s.getBoundingClientRect(); let bad=[];
                for (const el of s.querySelectorAll('*')) { const q=el.getBoundingClientRect(); if (q.width && (q.bottom>r.bottom-40 || q.right>r.right+1) && !el.closest('.sticker')) bad.push(el.tagName+':'+(el.textContent||'').slice(0,30)); }
                return bad.slice(0,3); }""")
            if over: problems.append((i, over))
            pg.locator(".s").screenshot(path=str(folder / f"slide-{i}.jpg"), type="jpeg", quality=90)
        b.close()
    if problems:
        print("ATENÇÃO, conteúdo saindo da área do slide:", problems); sys.exit(2)
    print("ok:", [f"slide-{i}.jpg" for i in range(1, 8)])

if __name__ == "__main__":
    build(sys.argv[1])
