from ursina import color

# ---------------- Seviyye ----------------
ROOM = 10        # otaq olcusu (metr)
ROOMS_PER_MAP = 6
N_MAPS = 2
N_ROOMS = ROOMS_PER_MAP   # bir xeritedeki otaq sayi
H = 2.6          # dam hundurluyu (oyunçu 1.7 + ehtiyat)
T = 0.3          # divar qalinligi
WALL = color.green
WALL_DARK = color.green.tint(-.2)
DOOR_COL = color.green.tint(-.45)

# xerite 2-nin baslangic ofseti (x oxu)
MAP2_OFFSET = 200

# her otaqdaki esger sayi (sonuncu otaqda esger yoxdur, boss var)
# her xerite 6 otaq: 5 doyush + 1 boss
SOLDIERS_PER_ROOM = [1, 1, 2, 2, 2, 0]

# ---------------- Oyunçu ----------------
PLAYER_MAX_HP = 1000
PLAYER_DAMAGE = 1        # esas silah zereri
FIRE_RATE = 0.12         # esas silah atesh sureti
SPAWN = (5, 0.15, 5)

# ---------------- Shotgun ----------------
SHOTGUN_DAMAGE = 100
SHOTGUN_FIRE_RATE = 0.55
SHOTGUN_PELLETS = 6      # bir atishda neche shua (vizual + hit)

# ---------------- Esger ----------------
SOLDIER_HP = 3
SOLDIER_DAMAGE = 2

# ---------------- Boss ----------------
BOSS_HP = 700
BOSS_DAMAGE = 5
BOSS_COOLDOWN = 1.0
BOSS_SPEED = 2.5
BOSS_SIZE = 1.2
BOSS_HEIGHT = 1.1

# ---------------- Umumi oyun veziyyeti ----------------
game = {
    'hp': PLAYER_MAX_HP,
    'dead': False,
    'alive_enemies': 0,
    'enemies': [],
    'player': None,
    'map': 0,                 # 0 = xerite 1, 1 = xerite 2
    'weapon': 1,              # 1 = esas, 2 = shotgun
    'has_shotgun': False,
    'transitioning': False,
}
