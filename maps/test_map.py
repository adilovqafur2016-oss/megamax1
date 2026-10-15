"""Numune Ursina xeritesi – terminal: map load test"""
from ursina import *
from ursina.color import Color

MAP_NAME = 'test'
MAP_TITLE = 'TEST ARENA'
MAP_DESC = 'Ursina ile yazilmis test xeritesi'
SPAWN = (5, 0.15, 5)

ROOM = 12
H = 2.6


def build(base_x=0):
    cx = base_x + ROOM / 2
    Entity(model='cube', color=color.dark_gray,
           position=(cx, -0.2, ROOM / 2), scale=(ROOM, 0.4, ROOM), collider='box')
    Entity(model='cube', color=color.gray,
           position=(cx, H + 0.2, ROOM / 2), scale=(ROOM, 0.4, ROOM), collider='box')
    T = 0.3
    Entity(model='cube', color=color.rgb(40, 60, 50),
           position=(cx, H / 2, 0), scale=(ROOM, H, T), collider='box')
    Entity(model='cube', color=color.rgb(40, 60, 50),
           position=(cx, H / 2, ROOM), scale=(ROOM, H, T), collider='box')
    Entity(model='cube', color=color.rgb(40, 60, 50),
           position=(base_x, H / 2, ROOM / 2), scale=(T, H, ROOM), collider='box')
    Entity(model='cube', color=color.rgb(40, 60, 50),
           position=(base_x + ROOM, H / 2, ROOM / 2), scale=(T, H, ROOM), collider='box')
    Entity(model='cube', color=color.rgb(80, 90, 70),
           position=(cx, 0.4, ROOM / 2), scale=(2.5, 0.8, 2.5), collider='box')
    Entity(model='quad', color=Color(0.9, 0.95, 0.6, 0.25),
           position=(cx, 0.02, ROOM / 2), scale=6, rotation_x=90)
    Entity(model='quad', color=color.lime,
           position=(base_x + T / 2 + 0.02, 1.4, ROOM / 2),
           scale=(1.2, 0.3), rotation_y=-90)


def spawn_enemies(base_x=0):
    return []
