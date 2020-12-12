import math

data_file = open('./data/data12')
movements = list(map(lambda row: [row[:1], int(row[1:])], data_file.read().split('\n')))
data_file.close()

def get_coords_guessed_rules(movements):
    x = 0
    y = 0
    direction = 90

    for movement in movements:
        action = movement[0]
        distance = movement[1]
        if action == 'R':
            direction = (direction + distance) % 360
        elif action == 'L':
            direction = (direction - distance) % 360
        elif action == 'N' or (action == 'F' and direction == 0):
            y += distance
        elif action == 'E' or (action == 'F' and direction == 90):
            x += distance
        elif action == 'S' or (action == 'F' and direction == 180):
            y -= distance
        elif action == 'W' or (action == 'F' and direction == 270):
            x -= distance
    return x,y

def rotate_vector(ox, oy, px, py, angle):
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return round(qx), round(qy)

def get_coords_actural_rules(movements, way_x = 0, way_y = 0):
    x = 0
    y = 0

    for movement in movements:
        action = movement[0]
        distance = movement[1]
        if action == 'R':
            way_x, way_y = rotate_vector(0, 0, way_x, way_y, -math.radians(distance))
        elif action == 'L':
            way_x, way_y = rotate_vector(0, 0, way_x, way_y, math.radians(distance))
        elif action == 'N':
            way_y += distance
        elif action == 'E':
            way_x += distance
        elif action == 'S':
            way_y -= distance
        elif action == 'W':
            way_x -= distance
        elif action == 'F':
            x += way_x * distance
            y += way_y * distance

    return x,y

[x, y] = get_coords_guessed_rules(movements)
print(sum([abs(x), abs(y)]))

[a, b] = get_coords_actural_rules(movements, way_x = 10, way_y = 1)
print(sum([abs(a), abs(b)]))
