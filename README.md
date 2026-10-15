# MegaMax1 v1.9

Ursina/Panda3D FPS demo.

## Run (Linux)
```bash
pip3 install --user ursina pillow
cd megamax1
python3 main.py
# or
chmod +x run_linux.sh && ./run_linux.sh
```

## Controls
- WASD + mouse – movement
- LMB – shoot
- 1 / 2 – pistol / shotgun (after pickup)
- ` (grave) – terminal
- R – restart when dead
- Esc – quit

## Terminal
```
help
map list
map load sector_a
map load sector_b
map load test
map rescan
```

Custom maps: put Ursina `.py` files in `maps/` with `MAP_NAME`, `build(base_x)`, optional `spawn_enemies(base_x)`.

## Lore notes
- Soldiers: smö SOLDIERS
- Boss: unkown61
