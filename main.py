#!/usr/bin/env python3

# importing the library
import pygame
from proto import ProtoSlide, LeftClickInput

screen_size = (400, 500)
flags = pygame.RESIZABLE
bg_color = (255, 255, 255)
color_red = (255, 0, 0)
color_green = (0, 255, 0)
scr_title = "Cycle of Power"
scr_iconsrc = "icc.png"
running = True
font = pygame


def initialize_pygame():
    # Initialize Pygame
    # pygame modules
    (numpass, numfail) = pygame.init()

    print("Number of modules initialized successfully:", numpass)


def is_initialized():
    is_initialized = pygame.get_init()
    print("Is pygame modules initialized:", is_initialized)
    return is_initialized


def name_screen(name):
    pygame.display.set_caption(name)


def set_screen():
    # Set up the game window
    screen = pygame.display.set_mode(screen_size, flags)
    name_screen(scr_title)
    set_icon(scr_iconsrc)
    return screen


def load_img(img_src):
    return pygame.image.load(img_src)


def set_icon(icon_src):
    icon_img = load_img(icon_src)
    pygame.display.set_icon(icon_img)


def paint_screen(screen, color):
    screen.fill(color)
    pygame.display.flip()


def main():
    global running
    global bg_color

    screen = set_screen()

    # ProtoSlide and ClickInput Implementation
    sld_proto = ProtoSlide()
    inp_lftclick = LeftClickInput()

    sld_proto.present_slide_name()

    if not is_initialized():
        initialize_pygame()

    # Game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Update Input
            inp_lftclick.update(event)

        paint_screen(screen, bg_color)

        if bg_color == color_red:
            bg_color = color_green
        else:
            bg_color = color_red

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
