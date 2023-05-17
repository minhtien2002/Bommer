import pygame
import pygame_menu

import game
from enums.algorithm import Algorithm
from pygame import mixer

COLOR_BACKGROUND = (255, 184, 184)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (255, 204, 204)
MENU_TITLE_COLOR = (255,255,255)
WINDOW_SCALE = 1

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

pygame.display.init()
INFO = pygame.display.Info()
TILE_SIZE = int(INFO.current_h * 0.065)
WINDOW_SIZE = (14.85 * TILE_SIZE, 14.85 * TILE_SIZE)

clock = None
player_alg = Algorithm.PLAYER
player_alg1 = Algorithm.PLAYERS
en1_alg = Algorithm.DIJKSTRA
en2_alg = Algorithm.DFS
en3_alg = Algorithm.DIJKSTRA
show_path = True
surface = pygame.display.set_mode(WINDOW_SIZE)

#load sounds
pygame.mixer.music.load('images/music.wav')
pygame.mixer.music.play(-1, 0.0, 5000)

def change_path(value, c):
    global show_path
    show_path = c


def change_player(value, c):
    global player_alg
    player_alg = c
    
def change_player1(value, c):
    global player_alg1
    player_alg1 = c


def change_enemy1(value, c):
    global en1_alg
    en1_alg = c


def change_enemy2(value, c):
    global en2_alg
    en2_alg = c


def change_enemy3(value, c):
    global en3_alg
    en3_alg = c


def run_game():
    game.game_init(surface, show_path, player_alg, player_alg1, en2_alg, en3_alg, TILE_SIZE)


def main_background():
    global surface
    surface.fill(COLOR_BACKGROUND)


def menu_loop():
    pygame.init()

    pygame.display.set_caption('Bomberman')
    clock = pygame.time.Clock()

    menu_theme = pygame_menu.Theme(
        selection_color=COLOR_WHITE,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_size=TILE_SIZE,
        title_font_color=COLOR_BLACK,
        title_font=pygame_menu.font.FONT_BEBAS,
        widget_font_color=COLOR_BLACK,
        widget_font_size=int(TILE_SIZE*0.7),
        background_color=MENU_BACKGROUND_COLOR,
        title_background_color=MENU_TITLE_COLOR,

    )

    play_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * WINDOW_SCALE),
        width=int(WINDOW_SIZE[0] * WINDOW_SCALE),
        title='Play menu'
    )

    play_options = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * WINDOW_SCALE),
        width=int(WINDOW_SIZE[0] * WINDOW_SCALE),
        title='Options'
    )
    play_options.add.selector("Character 1", [("Player", Algorithm.PLAYER)])
    
    play_options.add.selector("Character 2", [("DIJKSTRA", Algorithm.DIJKSTRA), ("DFS", Algorithm.DFS),
                                              ("None", Algorithm.NONE), ("Player2", Algorithm.PLAYERS)], onchange=change_player1)
    play_options.add.selector("Character 3", [("DIJKSTRA", Algorithm.DIJKSTRA), ("DFS", Algorithm.DFS),
                                              ("None", Algorithm.NONE)], onchange=change_enemy2,  default=1)
    play_options.add.selector("Character 4", [("DIJKSTRA", Algorithm.DIJKSTRA), ("DFS", Algorithm.DFS),
                                              ("None", Algorithm.NONE)], onchange=change_enemy3)
    play_options.add.selector("Show path", [("Yes", True), ("No", False)], onchange=change_path)

    play_options.add.button('Back', pygame_menu.events.BACK)
    play_menu.add.button('Start',
                         run_game)

    play_menu.add.button('Options', play_options)
    play_menu.add.button('Return  to  main  menu', pygame_menu.events.BACK)

    about_menu_theme = pygame_menu.themes.Theme(
        selection_color=COLOR_WHITE,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_size=TILE_SIZE,
        title_font_color=COLOR_BLACK,
        title_font=pygame_menu.font.FONT_BEBAS,
        widget_font_color=COLOR_BLACK,
        widget_font_size=int(TILE_SIZE*0.5),
        background_color=MENU_BACKGROUND_COLOR,
        title_background_color=MENU_TITLE_COLOR
    )

    about_menu = pygame_menu.Menu(
        theme=about_menu_theme,
        height=int(WINDOW_SIZE[1] * WINDOW_SCALE),
        width=int(WINDOW_SIZE[0] * WINDOW_SCALE),
        overflow=False,
        title='About'
    )
    about_menu.add.label("Player controls: ")
    about_menu.add.label("Movement: Arrows")
    about_menu.add.label("Plant bomb: Space")
    about_menu.add.label("Author: Michal Sliwa")
    about_menu.add.label("Sprite: ")
    about_menu.add.label("https://opengameart.org/ content/bomb-party-the-complete-set", wordwrap=True)
    about_menu.add.vertical_margin(25)
    about_menu.add.button('Return  to  main  menu', pygame_menu.events.BACK)

    main_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * WINDOW_SCALE),
        width=int(WINDOW_SIZE[0] * WINDOW_SCALE),
        onclose=pygame_menu.events.EXIT,
        title='Main menu'
    )

    main_menu.add.button('Play', play_menu)
    main_menu.add.button('About', about_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)

    running = True
    while running:

        clock.tick(FPS)

        main_background()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        if main_menu.is_enabled():
            main_menu.mainloop(surface, main_background)

        pygame.display.flip()

    exit()


if __name__ == "__main__":
    menu_loop()

