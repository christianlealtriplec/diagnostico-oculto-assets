"""Objetos y escenarios del Capítulo 4 (radio, velas, quemadura, grifo, patio, techo)."""
from draw import PAL


def radio(x=540, y=1100, s=1.0, waves=True):
    """Radio de pilas: carcasa negra, dial naranja, antena."""
    w = "".join(f'<path d="M {120+i*45} -180 a {80+i*45} {80+i*45} 0 0 1 0 {160+i*90}" stroke="#ff9500" stroke-width="10" fill="none" opacity="{0.8-i*0.2:.1f}" transform="translate(0 -40)"/>'
                for i in range(3)) if waves else ""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<line x1="-150" y1="-170" x2="-260" y2="-480" stroke="#888" stroke-width="10"/><circle cx="-260" cy="-480" r="12" fill="#aaa"/>'
            '<rect x="-300" y="-180" width="600" height="360" rx="40" fill="#1c1c1f" stroke="#333" stroke-width="8"/>'
            + "".join(f'<circle cx="{cx}" cy="{cy}" r="9" fill="#333"/>' for cx in range(-250, -40, 36) for cy in range(-120, 140, 36)) +
            '<rect x="0" y="-130" width="260" height="90" rx="10" fill="#ff9500" opacity="0.85"/>'
            '<line x1="40" y1="-85" x2="220" y2="-85" stroke="#3a1a00" stroke-width="4"/><rect x="120" y="-125" width="6" height="80" fill="#e10600"/>'
            '<circle cx="70" cy="70" r="46" fill="#3a3a40"/><circle cx="200" cy="70" r="46" fill="#3a3a40"/>'
            '<line x1="70" y1="70" x2="70" y2="35" stroke="#ccc" stroke-width="8"/><line x1="200" y1="70" x2="225" y2="45" stroke="#ccc" stroke-width="8"/>'
            f'{w}</g>')


def bag_supplies(x=540, y=1350, s=1.0):
    """Bolsa de plástico con velas y paquetes de pilas asomando."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            + "".join(f'<rect x="{bx}" y="-260" width="50" height="190" rx="8" fill="#f1ead8"/>' for bx in (-150, -90)) +
            '<rect x="-20" y="-220" width="130" height="80" rx="8" fill="#2a2a2a"/><rect x="-20" y="-220" width="130" height="24" fill="#e0b52a"/>'
            '<text x="45" y="-160" font-family="DejaVu Sans" font-weight="bold" font-size="26" fill="#e0b52a" text-anchor="middle">AA</text>'
            '<path d="M -220 -120 L 220 -120 L 190 200 L -190 200 Z" fill="#e8ecf2" opacity="0.92"/>'
            '<path d="M -150 -120 C -150 -230, -60 -230, -60 -120 M 60 -120 C 60 -230, 150 -230, 150 -120" stroke="#e8ecf2" stroke-width="16" fill="none"/>'
            '<path d="M -180 0 L 180 0" stroke="#c7ccd3" stroke-width="5"/></g>')


def tap(x=540, y=700, drip=True, running=False):
    """Grifo de cocina sobre el fregadero."""
    water = ('<rect x="-22" y="230" width="44" height="560" fill="#9fd4ff" opacity="0.75"/>' if running else
             ('<path d="M 0 250 C 14 275, 14 290, 0 296 C -14 290, -14 275, 0 250 Z" fill="#9fd4ff"/>'
              '<path d="M 0 400 C 12 422, 12 436, 0 441 C -12 436, -12 422, 0 400 Z" fill="#9fd4ff" opacity="0.7"/>' if drip else ""))
    return (f'<g transform="translate({x} {y})">'
            '<rect x="-60" y="-260" width="120" height="120" rx="20" fill="#9aa0a8"/>'
            '<path d="M 0 -140 L 0 -40 C 0 60, 40 100, 0 200" stroke="#b8bdc4" stroke-width="56" fill="none" stroke-linecap="round"/>'
            '<rect x="-30" y="190" width="60" height="50" rx="10" fill="#8a9098"/>'
            '<rect x="-150" y="-300" width="300" height="40" rx="18" fill="#c9ccd2"/>'
            f'{water}</g>'
            f'<rect x="80" y="{y+800}" width="920" height="60" rx="20" fill="#9aa0a8"/>'
            f'<path d="M 140 {y+860} L 940 {y+860} L 900 {y+1150} L 180 {y+1150} Z" fill="#6c727a"/>')


def burned_hand(x=540, y=1000, s=1.0, under_water=False):
    """Mano de niño con piel enrojecida, ampolla y restos de cera."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M -420 260 C -300 200, -200 160, -120 150 L -100 300 C -200 320, -320 360, -420 400 Z" fill="#f2cf4a"/>'
            '<path d="M -130 140 C -40 60, 120 50, 220 90 C 300 120, 330 180, 300 230 C 250 300, 80 330, -110 310 Z" fill="url(#skin)"/>'
            + "".join(f'<path d="M {fx} {fy} C {fx+60} {fy-20}, {fx+130} {fy-10}, {fx+150} {fy+10} C {fx+140} {fy+40}, {fx+60} {fy+45}, {fx} {fy+35} Z" fill="url(#skin)"/>'
                      for fx, fy in [(180, 80), (210, 140), (200, 200), (170, 255)]) +
            '<ellipse cx="90" cy="180" rx="190" ry="110" fill="#e0302a" opacity="0.55" filter="url(#blur6)"/>'
            '<ellipse cx="110" cy="170" rx="60" ry="42" fill="#ffe6d6" opacity="0.92" stroke="#e8a090" stroke-width="5"/>'
            '<ellipse cx="96" cy="158" rx="20" ry="10" fill="#fff" opacity="0.9"/>'
            '<path d="M -20 210 C 0 230, 30 240, 40 260 C 20 270, -10 250, -20 210 Z" fill="#f1ead8"/>'
            + ('<rect x="-60" y="-900" width="200" height="1300" fill="#9fd4ff" opacity="0.45"/>' if under_water else "") +
            '</g>')


def curtain(x=640, y=200, w=380, h=1300, smoke=True, towel=False):
    folds = "".join(f'<path d="M {x+i*60} {y} C {x+i*60+20} {y+h*0.4}, {x+i*60-20} {y+h*0.7}, {x+i*60} {y+h}" stroke="#5a1f1f" stroke-width="14" fill="none"/>'
                    for i in range(1, w // 60))
    sm = "".join(f'<circle cx="{x+80+i*40}" cy="{y+h-180-i*150}" r="{60+i*25}" fill="#8a8f9c" opacity="{0.42-i*0.06:.2f}" filter="url(#blur6)"/>'
                 for i in range(6)) if smoke else ""
    scorch = f'<path d="M {x} {y+h} C {x+40} {y+h-160}, {x+120} {y+h-220}, {x+180} {y+h-140} C {x+200} {y+h-60}, {x+220} {y+h}, {x+220} {y+h} Z" fill="#1a0a06"/>'
    tw = (f'<path d="M {x-60} {y+h-330} C {x+80} {y+h-380}, {x+200} {y+h-360}, {x+300} {y+h-300} L {x+260} {y+h-60} C {x+160} {y+h-110}, {x+40} {y+h-120}, {x-90} {y+h-80} Z" fill="#5a8fc4"/>'
          f'<path d="M {x-40} {y+h-260} C {x+80} {y+h-300}, {x+180} {y+h-290}, {x+280} {y+h-240}" stroke="#3f6f9e" stroke-width="10" fill="none"/>'
          + "".join(f'<path d="M {x+30+i*60} {y+h-60} q 8 30 0 50" stroke="#9fd4ff" stroke-width="8" fill="none"/>' for i in range(4))) if towel else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#7a2a2a"/>{folds}{scorch}{sm}{tw}'
