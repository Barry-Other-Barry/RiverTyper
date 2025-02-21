import pygame
from random import randint

pygame.init()
HEIGHT = 1080
WIDTH = 1920
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT_SIZE = 300
FONT = pygame.font.Font(None, FONT_SIZE)
QWERTY_KEYS = {
    'K_a': 'a', 'K_b': 'b', 'K_c': 'c', 'K_d': 'd',
    'K_e': 'e', 'K_f': 'f', 'K_g': 'g', 'K_h': 'h',
    'K_i': 'i', 'K_j': 'j', 'K_k': 'k', 'K_l': 'l',
    'K_m': 'm', 'K_n': 'n', 'K_o': 'o', 'K_p': 'p',
    'K_q': 'q', 'K_r': 'r', 'K_s': 's', 'K_t': 't',
    'K_u': 'u', 'K_v': 'v', 'K_w': 'w', 'K_x': 'x',
    'K_y': 'y', 'K_z': 'z',
    'K_0': '0', 'K_1': '1', 'K_2': '2', 'K_3': '3',
    'K_4': '4', 'K_5': '5', 'K_6': '6', 'K_7': '7',
    'K_8': '8', 'K_9': '9',
}


pygame.display.set_caption("Rivers Letters")



def main():
    running = True
    letter_to_display = None
    rv, gv, bv = 255, 255, 255
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                for key, value in QWERTY_KEYS.items():
                    if pressed_keys[getattr(pygame, key)]:
                        letter_to_display = value
                        rv = randint(100, 255)
                        gv = randint(100, 255)
                        bv = randint(100, 255)
                        break

        print(letter_to_display)

        text = FONT.render(letter_to_display, True, (rv, gv, bv))
        SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()
        SCREEN .fill((0, 0, 0))

if __name__ == "__main__":
    main()