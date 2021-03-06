import pygame
import sys

massiv = []

size = width, height = 492, 600
black = 52, 52, 54
color_inactive = pygame.Color(254, 90, 82)
color_active = pygame.Color(230, 192, 59)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BINARY SEARCH")
screen.fill(black)
font = pygame.font.Font(None, 32)
x_input = 100
y_input = 100
width_input = 36
height_input = 32

width_input1 = 292
height_input2 = 32
input_box = pygame.Rect(x_input, y_input, width_input, height_input)
box_1 = pygame.Rect(x_input, y_input + 42, width_input1, height_input2)

gameover = False
color = color_inactive
active = False
text = ''

ebani_solve = False

xCoord = {'-1': x_input + width_input * 0.0625 - 30, '0': x_input + width_input * 0.0625 - 9, '1': x_input + width_input * 0.0625 + 9, '2': x_input + width_input * 0.0625 + 28,
          '3': x_input + width_input * 0.0625 + 47, '4': x_input + width_input * 0.0625 + 65, '5': x_input + width_input * 0.0625 + 82,
          '6': x_input + width_input * 0.0625 + 100, '7': x_input + width_input * 0.0625 + 119, '8': x_input + width_input * 0.0625 + 136,
          '9': x_input + width_input * 0.0625 + 155, '10': x_input + width_input * 0.0625 + 173, '11': x_input + width_input * 0.0625 + 192,
          '12': x_input + width_input * 0.0625 + 209, '13': x_input + width_input * 0.0625 + 228, '14': x_input + width_input * 0.0625 + 245,
          '15': x_input + width_input * 0.0625 + 264, '16': x_input + width_input * 0.0625 + 284}

def ebani_liniu(x, y, w, h, color):
    pygame.draw.line(screen, color, (x + w // 2 - 1, y), (x + w // 2 - 1, y + h), 2)


def update_screen():
    txt_surface = font.render(text, True, color)
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, color, input_box, 2)
    pygame.display.flip()


def new_obj(time):
    pygame.time.wait(time)
    pygame.display.update()


array = []

time = 500

def bin_p():
    l = -1
    r = 16
    point = pygame.image.load("arrowL.png")
    point.set_colorkey((255, 255, 255))
    pointRect = point.get_rect(center=(300, 400))
    pointRect.x = xCoord.get(str(l))
    pointRect.y = y_input + 90
    screen.blit(point, pointRect)


    point = pygame.image.load("arrowR.png")
    point.set_colorkey((255, 255, 255))
    pointRect = point.get_rect(center=(300, 400))
    pointRect.x = xCoord.get(str(r))
    pointRect.y = y_input + 90
    screen.blit(point, pointRect)
    pygame.display.update()
    pygame.time.wait(time)
    while r - l > 1:
        mid = (l + r) // 2
        point = pygame.image.load("arrowM.png")
        point.set_colorkey((255, 255, 255))
        pointRect = point.get_rect(topleft=(300, 400))
        pointRect.x = xCoord.get(str(mid))
        pointRect.y = y_input + 90
        screen.blit(point, pointRect)
        pygame.display.update()
        pygame.time.wait(time)

        if array[mid] == 0:
            point = pygame.image.load("bump.png")
            point.set_colorkey((255, 255, 255))
            pointRect = point.get_rect(topleft=(300, 400))
            pointRect.x = xCoord.get(str(l)) + 7
            pointRect.y = y_input + 90
            screen.blit(point, pointRect)
            pygame.display.update()
            pygame.time.wait(time)
            point = pygame.image.load("bump.png")
            point.set_colorkey((255, 255, 255))
            pointRect = point.get_rect(topleft=(300, 400))
            pointRect.x = xCoord.get(str(mid)) + 7
            pointRect.y = y_input + 90
            screen.blit(point, pointRect)
            pygame.display.update()
            pygame.time.wait(time)
            l = mid
            point = pygame.image.load("arrowL.png")
            point.set_colorkey((255, 255, 255))
            pointRect = point.get_rect(center=(300, 400))
            pointRect.x = xCoord.get(str(l))
            pointRect.y = y_input + 90
            screen.blit(point, pointRect)
            pygame.display.update()
            pygame.time.wait(time)

        else:
            point = pygame.image.load("bump.png")
            point.set_colorkey((255, 255, 255))
            pointRect = point.get_rect(topleft=(300, 400))
            pointRect.x = xCoord.get(str(r)) + 7
            pointRect.y = y_input + 90
            screen.blit(point, pointRect)
            pygame.display.update()
            pygame.time.wait(time)
            point = pygame.image.load("bump.png")
            point.set_colorkey((255, 255, 255))
            pointRect = point.get_rect(topleft=(300, 400))
            pointRect.x = xCoord.get(str(mid)) + 7
            pointRect.y = y_input + 90
            screen.blit(point, pointRect)
            pygame.display.update()
            pygame.time.wait(time)
            r = mid
            point = pygame.image.load("arrowR.png")
            point.set_colorkey((255, 255, 255))
            pointRect = point.get_rect(topleft=(300, 400))
            pointRect.x = xCoord.get(str(r))
            pointRect.y = y_input + 90
            screen.blit(point, pointRect)
            pygame.display.update()
            pygame.time.wait(time)


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
                    for i in range(len(massiv)):
                        massiv[i] = int(massiv[i])
                    # print(*massiv)
                    # text = ''
                    # print(massiv[0])
                    for i in range(massiv[0]):
                        array.append(0)
                    for i in range(16 - massiv[0]):
                        array.append(1)
                    ebani_solve = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                    screen.fill(black)
                else:
                    text += event.unicode

    if ebani_solve:
        pygame.draw.rect(screen, color, box_1, 2)
        ebani_liniu(x_input, y_input + 42, width_input1 / 16 + 20, height_input2, color)  # box 3
        screen.blit(font.render(str(array[0]), True, (color)), (x_input + width_input * 0.0625 + 2, y_input + 47))
        ebani_liniu(x_input, y_input + 42, width_input1 / 4 + 2, height_input2, color)  # box 3
        screen.blit(font.render(str(array[1]), True, (color)), (x_input + width_input * 0.0625 + 20, y_input + 47))
        ebani_liniu(x_input, y_input + 42, width_input1 / 16 + 92, height_input2, color)  # box 3
        screen.blit(font.render(str(array[2]), True, (color)), (x_input + width_input * 0.0625 + 38, y_input + 47))
        ebani_liniu(x_input, y_input + 42, width_input1 / 2 + 2, height_input2, color)  # box 3
        screen.blit(font.render(str(array[3]), True, (color)), (x_input + width_input * 0.0625 + 56, y_input + 47))
        ebani_liniu(x_input, y_input + 42, width_input1 / 16 + 165, height_input2, color)  # box 3
        screen.blit(font.render(str(array[4]), True, (color)), (x_input + width_input * 0.0625 + 74, y_input + 47))
        ebani_liniu(x_input, y_input + 42, width_input1 / 2 + 72, height_input2, color)  # box 3
        screen.blit(font.render(str(array[5]), True, (color)), (x_input + width_input * 0.0625 + 93, y_input + 47))
        ebani_liniu(x_input, y_input + 42, width_input1 * 0.875, height_input2, color)  # box 3
        screen.blit(font.render(str(array[6]), True, (color)), (x_input + width_input * 0.0625 + 110, y_input + 47))
        ebani_liniu(x_input, y_input + 42, width_input1, height_input2, color)  # box 3
        screen.blit(font.render(str(array[7]), True, (color)), (x_input + width_input * 0.0625 + 129, y_input + 47))
        ebani_liniu(x_input, y_input + 42, width_input1 * 1.25 - 38, height_input2, color)  # box 3\
        screen.blit(font.render(str(array[8]), True, (color)), (x_input + width_input * 0.0625 + 147, y_input + 47))
        ebani_liniu(x_input, y_input + 42, width_input1 * 1.25 - 2, height_input2, color)  # box 3
        screen.blit(font.render(str(array[9]), True, (color)), (x_input + width_input * 0.0625 + 165, y_input + 47))
        ebani_liniu(x_input, y_input + 42, width_input1 * 1.25 + 35, height_input2, color)  # box 3
        screen.blit(font.render(str(array[10]), True, (color)), (x_input + width_input * 0.0625 + 183, y_input + 47))
        ebani_liniu(x_input, y_input + 42, width_input1 * 1.5 - 2, height_input2, color)  # box 3
        screen.blit(font.render(str(array[11]), True, (color)), (x_input + width_input * 0.0625 + 201, y_input + 47))
        ebani_liniu(x_input, y_input + 42, width_input1 * 1.675 - 15, height_input2, color)  # box 3
        screen.blit(font.render(str(array[12]), True, (color)), (x_input + width_input * 0.0625 + 219, y_input + 47))
        ebani_liniu(x_input, y_input + 42, width_input1 * 1.75 - 2, height_input2, color)  # box 3\
        screen.blit(font.render(str(array[13]), True, (color)), (x_input + width_input * 0.0625 + 238, y_input + 47))
        ebani_liniu(x_input, y_input + 42, width_input1 * 1.875 - 2, height_input2, color)  # box 3
        screen.blit(font.render(str(array[14]), True, (color)), (x_input + width_input * 0.0625 + 255, y_input + 47))
        screen.blit(font.render(str(array[15]), True, (color)), (x_input + width_input * 0.0625 + 274, y_input + 47))
        bin_p()
        new_obj(500)
        while not gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = True
    update_screen()
sys.exit()
