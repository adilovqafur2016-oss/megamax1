import gfx

gfx.pre_init()

from ursina import *

app = Ursina(title='MegaMax1 v1.9', borderless=False)
gfx.setup()

import config
from config import game
from level import build_level, spawn_enemies_for_map
from player import create_player, restart
from terminal import init_terminal, get_terminal

build_level()
player = create_player()

game['enemies'] = spawn_enemies_for_map(0)
game['alive_enemies'] = len(game['enemies'])
game['map'] = 0

term = init_terminal()


def input(key):
    t = get_terminal()

    # terminal toggle
    if key == 'grave' or key == '`':  # ` duymesi
        if t:
            t.toggle()
        return

    # terminal aciqdirsa komandalari ud
    if t and t.open:
        if key == 'escape':
            t.toggle()
            return
        t.handle_key(key)
        return

    if key == 'escape':
        application.quit()
    if key == 'r' and game['dead']:
        restart()


app.run()
