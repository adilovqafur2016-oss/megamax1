"""Qrafika tanzimlemeleri: antialiasing, duman, FOV, interfeys temizliyi."""
from panda3d.core import loadPrcFileData, AntialiasAttrib


def pre_init():
    """Ursina() cagirilmazdan EVVEL cagirilmalidir. V0.3: AA ve aniso azaldildi."""
    loadPrcFileData('', 'framebuffer-multisample 1\n'
                        'multisamples 2\n'
                        'texture-anisotropic-degree 4\n')


def setup():
    """Ursina() cagirildiqdan SONRA cagirilmalidir."""
    from ursina import window, camera, scene
    from textures import rgba

    window.color = rgba(5, 8, 6)
    camera.fov = 90
    camera.clip_plane_near = 0.05
    camera.clip_plane_far = 120

    for name in ('fps_counter', 'entity_counter', 'collider_counter', 'cog_button'):
        try:
            getattr(window, name).enabled = False
        except Exception:
            pass
    try:
        window.exit_button.visible = False
    except Exception:
        pass

    try:
        scene.fog_color = rgba(6, 10, 8)
        scene.fog_density = (8, 45)
    except Exception:
        pass
