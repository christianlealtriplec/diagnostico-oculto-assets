"""Piezas del Capítulo 6 (abuela en el suelo, manos en el pecho, llaves, cuarto)."""
from draw import PAL, abuela


def abuela_suelo(x=540, y=1350, s=1.0, lips="#7d8494"):
    """Carmen tumbada boca arriba en el suelo (la misma abuela, girada), ojos cerrados, boca abierta."""
    return (f'<g transform="translate({x} {y}) scale({s}) rotate(-90) translate(-362 -1000)">'
            + abuela(mood="ahogo", cannula=True, lips=lips) + '</g>'
            f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M 250 -60 C 420 -70, 620 -60, 760 -40 L 760 60 C 620 80, 420 80, 250 60 Z" fill="#3a3d47"/>'
            '<path d="M 760 -40 L 900 -30 L 900 50 L 760 60 Z" fill="#2a2018"/></g>')


def hands_shoulders(x=540, y=1200, s=1.0):
    """Tus dos manos sujetando los hombros (vista desde arriba)."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M -520 -520 C -420 -380, -360 -300, -300 -240 L -220 -300 C -280 -360, -340 -440, -420 -600 Z" fill="#1c2a48"/>'
            '<ellipse cx="-250" cy="-250" rx="70" ry="52" fill="url(#skin)" transform="rotate(35 -250 -250)"/>'
            '<path d="M 520 -520 C 420 -380, 360 -300, 300 -240 L 220 -300 C 280 -360, 340 -440, 420 -600 Z" fill="#1c2a48"/>'
            '<ellipse cx="250" cy="-250" rx="70" ry="52" fill="url(#skin)" transform="rotate(-35 250 -250)"/>'
            '<path d="M -330 -330 l -40 -30 M -300 -360 l -20 -46 M 330 -330 l 40 -30 M 300 -360 l 20 -46" stroke="#fff" stroke-width="8" stroke-linecap="round" opacity="0.7"/>'
            '</g>')


def compress_hands(x=540, y=1100, s=1.0):
    """Manos entrelazadas, talón de la mano en el centro del pecho, brazos rectos."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M -180 -900 L -60 -120 L 60 -120 L 180 -900 Z" fill="#1c2a48"/>'
            '<ellipse cx="0" cy="-60" rx="150" ry="95" fill="url(#skin)"/>'
            '<path d="M -110 -90 C -60 -110, 60 -110, 110 -90 M -120 -40 C -60 -60, 60 -60, 120 -40" stroke="#b98a66" stroke-width="10" fill="none"/>'
            '<path d="M -230 40 L -290 90 M 230 40 L 290 90 M 0 80 L 0 150" stroke="#ff3b30" stroke-width="14" stroke-linecap="round"/>'
            '</g>')


def keys_hand(x=760, y=900, s=1.0):
    """Mano con un manojo de llaves."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<ellipse cx="0" cy="0" rx="70" ry="56" fill="url(#skin)"/>'
            '<circle cx="0" cy="80" r="34" fill="none" stroke="#c9a24a" stroke-width="10"/>'
            '<path d="M -10 110 L -30 230 L -10 230 L -14 210 L 0 210 L -4 190 L 6 190 Z" fill="#c9cfd6"/>'
            '<path d="M 20 108 L 70 220 L 86 212 L 78 194 L 92 188 L 84 170 L 92 164 Z" fill="#c9a24a"/>'
            '</g>')


def bedroom(lit=True):
    """Habitación de la abuela: cama, concentrador al fondo, alfombra, puerta abierta."""
    from draw2 import wallpaper, floor_tiles
    from draw import bed, blanket, concentrator
    return (wallpaper("#151a2b", "#11162a") + floor_tiles(1250, "#1f1813", "#1a140f") +
            '<g transform="translate(0 -260)">' + bed(300, 760) + blanket(300, 1150) + '</g>'
            + concentrator(170, 960, 0.8, off=True) +
            '<ellipse cx="540" cy="1600" rx="460" ry="160" fill="#5a2a2a" opacity="0.6"/>'
            + ('<polygon points="0,1920 0,1500 400,900 1080,1100 1080,1920" fill="url(#beam)" opacity="0.6"/>' if lit else ""))
