import pygame
import sys

massiv = []

size = width, height = 492, 600
black = 52, 52, 54
color_inactive = pygame.Color(254, 90, 82)
color_active = pygame.Color(230, 192, 59)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("INDIVIDUAL PROJECT!!!")
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()
x_input = 100
y_input = 100
width_input = 292
height_input = 32
input_box = pygame.Rect(x_input, y_input, width_input, height_input)
gameover = False
color = color_inactive
active = False
text = ''

ebani_solve = False

def ebani_liniu(x, y, w, h):
    pygame.draw.line(screen, (255, 255, 255), (x + w / 2 - 1, y), (x + w / 2 - 1, y + h), 2)

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
                    #text = ''

                    ebani_solve = True

                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
    screen.fill(black)
    txt_surface = font.render(text, True, color)
    input_box.w = width_input

    if ebani_solve:
        ebani_liniu(x_input, y_input, width_input, height_input)

    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, color, input_box, 2)
    pygame.display.flip()
    clock.tick(30)
sys.exit()
