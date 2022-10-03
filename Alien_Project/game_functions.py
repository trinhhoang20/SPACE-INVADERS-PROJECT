import sys
import pygame as pg
from vector import Vector

movement = {pg.K_LEFT: Vector(-1, 0),  # dictionary to map keys to Vector velocities
            pg.K_RIGHT: Vector(1, 0),
            pg.K_UP: Vector(0, -1),
            pg.K_DOWN: Vector(0, 1)
            }


def check_keydown_events(event, settings, ship):
    key = event.key
    if key == pg.K_SPACE:
        ship.shooting = True
    elif key in movement.keys():
        ship.vel += settings.ship_speed_factor * movement[key]
    # print(f'ship now moving at {ship.vel}')


def check_keyup_events(event, ship):
    key = event.key
    if key == pg.K_SPACE:
        ship.shooting = False
    elif key == pg.K_ESCAPE:
        ship.vel = Vector()  # Note: Escape key stops the ship
    elif key in movement.keys(): ship.vel = Vector()


def check_events(settings, play_button, ship, hs_button):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event=event, settings=settings, ship=ship)
        elif event.type == pg.KEYUP:
            check_keyup_events(event=event, ship=ship)
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            check_play_button(settings, play_button, mouse_x, mouse_y)


def check_play_button(settings, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        settings.game_active = True


def clamp(posn, rect, settings):
    left, top = posn.x, posn.y
    width, height = rect.width, rect.height
    left = max(0, min(left, settings.screen_width - width))
    top = max(0, min(top, settings.screen_height - height))
    return Vector(x=left, y=top), pg.Rect(left, top, width, height)
