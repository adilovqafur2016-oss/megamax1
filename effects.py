import random
from collections import deque

from panda3d.core import TransparencyAttrib
from ursina import *
from ursina.color import Color

import textures as tx

_decals = deque()
MAX_DECALS = 24  # V0.3: daha az dekal


def make_transparent(e, depth_write=False):
    """Seffaf (alfa) teksturali/rengli obyekt ucun lazimi tanzimlemeler."""
    try:
        e.setTransparency(TransparencyAttrib.MAlpha)
        if not depth_write:
            e.setDepthWrite(False)
        e.double_sided = True
    except Exception:
        pass
    return e


def spark(pos, col=None, n=4, speed=0.55, size=0.035, life=0.22):
    """Qigilcim / qan / partlayis hissecikleri. V0.3: daha az hissecik."""
    if col is None:
        col = tx.rgba(255, 200, 90)
    pos = Vec3(*pos)
    for _ in range(n):
        e = Entity(model='cube', color=col, position=pos, scale=size)
        d = Vec3(random.uniform(-1, 1), random.uniform(-0.3, 1), random.uniform(-1, 1)) * speed
        e.animate_position(pos + d, duration=life, curve=curve.out_quad)
        e.animate_scale(0.001, duration=life)
        destroy(e, delay=life + 0.03)


def beam(start, end, col, width=0.03, life=0.12):
    """Qisa muddetli gulle izi / lazer suasi."""
    start, end = Vec3(*start), Vec3(*end)
    length = (end - start).length()
    if length < 0.01:
        return
    e = Entity(model='cube', color=col, position=(start + end) / 2, scale=(width, width, length))
    e.look_at(end)
    make_transparent(e)
    e.animate_color(Color(col.r, col.g, col.b, 0), duration=life)
    destroy(e, delay=life + 0.03)


def bullet_hole(point, normal):
    try:
        point, normal = Vec3(*point), Vec3(*normal)
        d = Entity(model='quad', texture=tx.hole(), position=point + normal * 0.012,
                   scale=random.uniform(0.1, 0.17))
        d.look_at(point - normal)
        make_transparent(d)
        _decals.append(d)
        if len(_decals) > MAX_DECALS:
            destroy(_decals.popleft())
    except Exception:
        pass
