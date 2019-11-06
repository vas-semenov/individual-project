import pygame
import sys

massiv = []

size = width, height = 492, 600
black = 52, 52, 54
color_inactive = pygame.Color(254, 90, 82)
color_active = pygame.Color(230, 192, 59)

def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    width_input = 292
    input_box = pygame.Rect(100, 100, width_input, 32)
    gameover = False
    color = color_inactive
    active = False
    text = ''
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        massiv = text.split(" ")
                        print(*massiv)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        screen.fill(black)
        txt_surface = font.render(text, True, color)
        input_box.w = width_input
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
        clock.tick(30)
    print(width_input)
    sys.exit()

main()