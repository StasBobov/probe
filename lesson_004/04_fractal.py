
# -*- coding: utf-8 -*-



# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

import pygame
import sys
import math

green = (0, 128, 0)

# next_angle=0, point_0r=[0, 0] - костыли
def draw_branches(point_0, angle, length, first_tree=0, next_angle=0, point_0r=[0, 0], point_0l=[0, 0]):
    if first_tree == 0:
        one_direction = (90 * math.pi) / 180
        dx = math.cos(one_direction) * length
        dy = math.sin(one_direction) * length
        end_point = (point_0[0] + dx, (point_0[1] - dy))
        pygame.draw.line(screen, green, point_0, end_point, 4)
        point_0r = end_point
        point_0l = end_point
        next_angle = angle
        length = length * 0.75
        direction = (angle * math.pi) / 180
        dx = math.cos(direction) * length
        dy = math.sin(direction) * length
        end_pointr = (point_0r[0] + dx, (point_0r[1] - dy))
        end_pointl = (point_0l[0] - dx, (point_0l[1] - dy))
        pygame.draw.line(screen, green, point_0r, end_pointr, 4)
        pygame.draw.line(screen, green, point_0l, end_pointl, 4)
        first_tree = 1
        point_0r = end_pointr
        point_0l = end_pointl
    if length < 10:
        return

    if first_tree == 1:
        angle = angle + next_angle
        length = length * 0.75
        direction = (angle * math.pi) / 180
        dx = math.cos(direction) * length
        dy = math.sin(direction) * length
        end_pointr = (point_0r[0] + dx, (point_0r[1] - dy))
        end_pointl = (point_0l[0] - dx, (point_0l[1] - dy))
        pygame.draw.line(screen, green, point_0r, end_pointr, 4)
        print(point_0r, point_0l)
        pygame.draw.line(screen, green, point_0l, end_pointl, 4)
        draw_branches(end_pointr, angle, length, first_tree=1, next_angle=next_angle, point_0r=end_pointr, point_0l=end_pointl)
        draw_branches(end_pointr, angle, length, first_tree=1, next_angle=next_angle, point_0l=end_pointl, point_0r=end_pointr)




pygame.init()

screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    length = 200

    draw_branches((600, 600), 30, length)
    pygame.display.update()
    clock.tick(60)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()



