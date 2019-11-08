import pygame
import sys
# названия переменных измени гений. как мы это презентовать будем?
massiv = []

size = width, height = 492, 600
black = 52, 52, 54
color_inactive = pygame.Color(254, 90, 82)
color_active = pygame.Color(230, 192, 59)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("INDIVIDUAL PROJECT!!!")
screen.fill(black)
font = pygame.font.Font(None, 32)
x_input = 100
y_input = 100
width_input = 292
height_input = 32

input_box = pygame.Rect(x_input, y_input, width_input, height_input)
box_1 = pygame.Rect(x_input, y_input + 42, width_input, height_input)
box_2 = pygame.Rect(x_input, y_input + 84, width_input, height_input)
box_3 = pygame.Rect(x_input, y_input + 126, width_input, height_input)
box_4= pygame.Rect(x_input, y_input + 168, width_input, height_input)

gameover = False
color = color_inactive
active = False
text = ''

ebani_solve = False


def ebani_liniu(x, y, w, h, color):
    pygame.draw.line(screen, color, (x + w / 2 - 1, y), (x + w / 2 - 1, y + h), 2)

def update_screen():
    txt_surface = font.render(text, True, color)
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, color, input_box, 2)
    pygame.display.flip()

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
                    # text = ''
                    ebani_solve = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                    screen.fill(black)
                else:
                    text += event.unicode
    # начало отрисовки
    if ebani_solve:
        ebani_liniu(x_input, y_input, width_input, height_input, color)  # box 3
        ebani_liniu(x_input, y_input, width_input / 2 + 2, height_input, color)  # box 3
        ebani_liniu(x_input, y_input, width_input * 1.5 - 2, height_input, color)  # box 3
        ebani_liniu(x_input, y_input, width_input / 4 + 2, height_input, color)  # box 3
        ebani_liniu(x_input, y_input, width_input * 1.75 - 2, height_input, color)  # box 3
        ebani_liniu(x_input, y_input, width_input / 2 + 72, height_input, color)  # box 3
        ebani_liniu(x_input, y_input, width_input * 1.25 - 2, height_input, color)  # box 3
        ebani_liniu(x_input, y_input, width_input / 2 + 72, height_input, color)  # box 3
        ebani_liniu(x_input, y_input, width_input * 1.25 - 2, height_input, color)  # box 3
        ebani_liniu(x_input, y_input, width_input / 16 + 20, height_input, color)  # box 3
        ebani_liniu(x_input, y_input, width_input / 16 + 92, height_input, color)  # box 3
        ebani_liniu(x_input, y_input, width_input / 16 + 165, height_input, color)  # box 3
        ebani_liniu(x_input, y_input, width_input * 1.25 - 38, height_input, color)  # box 3
        ebani_liniu(x_input, y_input, width_input * 1.25 + 35, height_input, color)  # box 3
        ebani_liniu(x_input, y_input, width_input * 0.875, height_input, color)  # box 3
        ebani_liniu(x_input, y_input, width_input * 1.875 - 2, height_input, color)  # box 3
        ebani_liniu(x_input, y_input, width_input * 1.675 - 15, height_input, color)  # box 3
        pygame.time.wait(500)
        pygame.display.update()

        pygame.draw.rect(screen, color, box_1, 2)
        screen.blit(font.render(text, True, (color)), (x_input + 5, y_input + 47))
        ebani_liniu(x_input, y_input + 42, width_input, height_input, color)  # box 1
        ebani_liniu(x_input, y_input + 42, width_input / 2 + 2, height_input, color)  # box 1
        ebani_liniu(x_input, y_input + 42, width_input * 1.5 - 2, height_input, color)  # box 1
        ebani_liniu(x_input, y_input + 42, width_input / 4 + 2, height_input, color)  # box 2
        ebani_liniu(x_input, y_input + 42, width_input * 1.75 - 2, height_input, color)  # box 2
        ebani_liniu(x_input, y_input + 42, width_input / 2 + 72, height_input, color)  # box 2
        ebani_liniu(x_input, y_input + 42, width_input * 1.25 - 2, height_input, color)  # box 2
        pygame.time.wait(500)
        pygame.display.update()

        pygame.draw.rect(screen, color, box_2, 2)
        screen.blit(font.render(text, True, (color)), (x_input + 5, y_input + 89))
        ebani_liniu(x_input, y_input + 84, width_input, height_input, color)  # box 2
        ebani_liniu(x_input, y_input + 84, width_input / 2 + 2, height_input, color)  # box 2
        ebani_liniu(x_input, y_input + 84, width_input * 1.5 - 2, height_input, color)  # box 2
        pygame.time.wait(500)
        pygame.display.update()


        pygame.draw.rect(screen, color, box_3, 2)
        screen.blit(font.render(text, True, (color)), (x_input + 5, y_input + 131))
        ebani_liniu(x_input, y_input + 126, width_input, height_input, color)
        pygame.time.wait(500)
        pygame.display.update()

        pygame.draw.rect(screen, color, box_4, 2)
        screen.blit(font.render(text, True, (color)), (x_input + 5, y_input + 173))
        pygame.time.wait(500)
        pygame.display.update()


        while not gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = True
    update_screen()
sys.exit()
