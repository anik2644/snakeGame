import glfw
from OpenGL.GL import *
import math
 
W, H = 800, 800
 
colors = [[255, 255, 255],
          [255, 0, 0],
          [0, 255, 0],
          [0, 0, 255],
          [255, 255, 0],
          [0, 255, 255],
          [255, 0, 255],
          [127, 127, 127]]
 
 
def get_zone_custom(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
 
    if dx >= 0 and dy >= 0:
        if dx > dy:
            return 0
        return 1
 
    elif dx >= 0 and dy < 0:
        if dx > abs(dy):
            return 7
        return 6
 
    elif dx < 0 and dy >= 0:
        if abs(dx) > dy:
            return 3
        return 2
 
    else:
        if abs(dx) > abs(dy):
            return 4
        return 5
 
 
def return_back_custom(zone, x, y):  # zone3 to all zones
    if zone == 0:
        return -x, y
    elif zone == 1:
        return y, -x
    elif zone == 2:
        return -y, -x
    elif zone == 3:
        return x, y
    elif zone == 4:
        return x, -y
    elif zone == 5:
        return -y, x
    elif zone == 6:
        return y, x
    else:
        return -x, -y
 
 
def all_zone_to_3_custom(zone, x, y):  # all zone to zone3
    if zone == 0:
        return -x, y
    elif zone == 1:
        return -y, x
    elif zone == 2:
        return -y, -x
    elif zone == 3:
        return x, y
    elif zone == 4:
        return x, -y
    elif zone == 5:
        return y, -x
    elif zone == 6:
        return y, x
    else:
        return -x, -y
 
 
def draw_axes_custom():
    glColor3ub(127, 127, 127)
    glBegin(GL_LINES)
    glVertex2f(-W / 2, 0)
    glVertex2f(W / 2 - 1, 0)
    glVertex2f(0, -H / 2)
    glVertex2f(0, H / 2 - 1)
    glEnd()
 
 
def draw_pixel_custom(x, y, zone):
    x, y = return_back_custom(zone, x, y)
    glVertex2f(x, y)
 
 
def draw_pixel_2_custom(x, y):
    glVertex2f(x, y)
 
 
def draw_line_3_custom(x0, y0, x1, y1, zone):
    dx = x1 - x0
    dy = y1 - y0
    x = x0
    y = y0
    d = -2 * dx + dy
    del_w = -2 * dy
    del_nw = -2 * (dx + dy)
    draw_pixel_custom(x, y, zone)
    while x > x1:
        if d < 0:
            d += del_nw
            x -= 1
            y += 1
        else:
            d += del_w
            x -= 1
        draw_pixel_custom(x, y, zone)
 
 
def read_polygon_file_custom(filename):
    points = []
    with open(filename, 'r') as file:
        num_vertices = int(file.readline().strip())
        for _ in range(num_vertices):
            x, y = map(int, file.readline().strip().split(','))
            points.append((x, y))
    return points
 
 
def construct_edge_table_custom(points):
    edges = {}
 
    for i in range(1, len(points)):
        edges[i - 1] = [points[i], points[i - 1]]
        edges[i - 1] = sorted(edges[i - 1], key=lambda x: (x[1], x[0]))
 
        if i == len(points) - 1:
            edges[i] = [points[i], points[0]]
            edges[i] = sorted(edges[i], key=lambda x: (x[1], x[0]))
 
    _, y_min = min(points, key=lambda x: (x[1], x[0]))
    x_of_y_max, y_max = max(points, key=lambda x: (x[1], x[0]))
 
    def slope(x0, y0, x1, y1):
        if (x1 - x0) == 0:
            return 0
        return (y1 - y0) / (x1 - x0)
 
    edge_table = {}
    for i in range(y_min, y_max):
        edge_vertexs = []
        for key, edge in edges.items():
            first_vertex, second_vertex = edge[0], edge[1]
            x0, y0 = first_vertex
            x1, y1 = second_vertex
            if y0 == i and y0 != y1:
                m = slope(x0, y0, x1, y1)
                if m == 0:
                    edge_vertexs.append((y1, x0, 0))
                else:
                    edge_vertexs.append((y1, x0, 1 / m))
 
        if i != y_min:
            previous_edge_vertexs = edge_table[i - 1]
            for triplet in previous_edge_vertexs:
                prev_y_max, prev_x_of_y_min, prev_slope = triplet
                if prev_y_max != i:
                    prev_x_of_y_min += prev_slope
                    edge_vertexs.append((prev_y_max, prev_x_of_y_min, prev_slope))
 
        edge_vertexs = sorted(edge_vertexs, key=lambda x: (x[1], x[0]))
 
        edge_table[i] = edge_vertexs
 
    return y_min, y_max, edge_table, points, edges
 
 
def draw_polygon_vertex_custom(points):
    glPointSize(5)
    glBegin(GL_POINTS)
    for point in points:
        glColor3ub(255, 255, 255)
        draw_pixel_2_custom(point[0], point[1])
    glEnd()
    glPointSize(1)
 
 
def draw_edges_custom(edges):
    glPointSize(2)
    glBegin(GL_POINTS)
    for key, edge in edges.items():
        x0, y0 = edge[0]
        x1, y1 = edge[1]
        zone = get_zone_custom(x0, y0, x1, y1)
        x0, y0 = all_zone_to_3_custom(zone, x0, y0)
        x1, y1 = all_zone_to_3_custom(zone, x1, y1)
 
        glColor3ub(255, 255, 0)
        draw_line_3_custom(x0, y0, x1, y1, zone)
    glEnd()
    glPointSize(1)
 
 
def draw_boundary_pixels_custom(edges):
    glPointSize(6)
    glBegin(GL_POINTS)
    for key, edge in edges.items():
        first_vertex, second_vertex = edge[0], edge[1]
        x0, y0 = first_vertex
        x1, y1 = second_vertex
 
        num_pixels = max(abs(x1 - x0), abs(y1 - y0)) + 1
        dx = (x1 - x0) / num_pixels
        dy = (y1 - y0) / num_pixels
 
        for i in range(num_pixels):
            pixel_x = round(x0 + i * dx)
            pixel_y = round(y0 + i * dy)
            glColor3ub(0, 0, 255)
            draw_pixel_2_custom(pixel_x, pixel_y)
 
    glEnd()
    glPointSize(1)
 
 
def draw_polygon_fill_custom(y_min, y_max, edge_table):
    glBegin(GL_POINTS)
    for y in range(y_min, y_max):
        i = 0
        while i < len(edge_table[y]):
            first_triplet = edge_table[y][i]
            second_triplet = edge_table[y][i + 1]
 
            x0, y0 = first_triplet[1], y
            x1, y1 = second_triplet[1], y
 
            zone = get_zone_custom(x0, y0, x1, y1)
            x0, y0 = all_zone_to_3_custom(zone, x0, y0)
            x1, y1 = all_zone_to_3_custom(zone, x1, y1)
 
            glColor3ub(255, 255, 0)
 
            draw_line_3_custom(x0, y, x1, y, zone)
 
            i += 2
 
    glEnd()
 
 
draw_vertex_flag_custom = True
draw_boundary_pixel_flag_custom = False
draw_polygon_fill_flag_custom = False
y_min_custom, y_max_custom, edge_table_custom, points_custom, edges_custom = 0, 0, {}, [], {}
 
 
def rotate_point_custom(point, angle):
    x, y = point
    angle_rad = math.radians(angle)
    new_x = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    new_y = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return new_x, new_y
 
 
def rotate_polygon_custom(points, angle):
    cx = sum(x for x, _ in points) / len(points)
    cy = sum(y for _, y in points) / len(points)
 
    translated_points = [(x - cx, y - cy) for x, y in points]
 
    rotated_points = [rotate_point_custom(point, angle) for point in translated_points]
 
    new_points = [(round(x + cx), round(y + cy)) for x, y in rotated_points]
 
    return new_points
 
 
def key_callback_custom(window, key, scancode, action, mods):
    global draw_vertex_flag_custom, draw_boundary_pixel_flag_custom, draw_polygon_fill_flag_custom
    global y_min_custom, y_max_custom, edge_table_custom, points_custom, edges_custom
 
    mouse_x, mouse_y = glfw.get_cursor_pos(window)
    window_width, window_height = glfw.get_window_size(window)
    if 0 <= mouse_x < window_width and 0 <= mouse_y < window_height:
        if action == glfw.PRESS:
            if key == glfw.KEY_KP_0:
                draw_vertex_flag_custom = True
                draw_boundary_pixel_flag_custom = False
                draw_polygon_fill_flag_custom = False
            elif key == glfw.KEY_KP_1:
                draw_vertex_flag_custom = False
                draw_boundary_pixel_flag_custom = True
                draw_polygon_fill_flag_custom = False
            elif key == glfw.KEY_KP_2:
                draw_vertex_flag_custom = False
                draw_boundary_pixel_flag_custom = False
                draw_polygon_fill_flag_custom = True
            elif key == glfw.KEY_LEFT:
                points_custom = rotate_polygon_custom(points_custom, 5)
                y_min_custom, y_max_custom, edge_table_custom, points_custom, edges_custom = \
                    construct_edge_table_custom(points_custom)
            elif key == glfw.KEY_RIGHT:
                points_custom = rotate_polygon_custom(points_custom, -5)
                y_min_custom, y_max_custom, edge_table_custom, points_custom, edges_custom = \
                    construct_edge_table_custom(points_custom)
 
 
def main():
    global draw_vertex_flag_custom, draw_boundary_pixel_flag_custom, draw_polygon_fill_flag_custom
    global y_min_custom, y_max_custom, edge_table_custom, points_custom, edges_custom
 
    if not glfw.init():
        return
 
    window = glfw.create_window(W, H, "Lab 3", None, None)
    if not window:
        glfw.terminate()
        return
 
    glfw.make_context_current(window)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-W / 2, W / 2 - 1, -H / 2, H / 2 - 1, -1, 1)
 
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
 
    points_custom = read_polygon_file_custom("vertex.txt")
    y_min_custom, y_max_custom, edge_table_custom, points_custom, edges_custom = \
        construct_edge_table_custom(points_custom)
 
    glfw.set_key_callback(window, key_callback_custom)
 
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glfw.poll_events()
 
        draw_axes_custom()
 
        if draw_vertex_flag_custom:
            draw_polygon_vertex_custom(points_custom)
        elif draw_boundary_pixel_flag_custom:
            draw_boundary_pixels_custom(edges_custom)
        elif draw_polygon_fill_flag_custom:
            draw_polygon_fill_custom(y_min_custom, y_max_custom, edge_table_custom)
 
        glfw.swap_buffers(window)
 
    glfw.terminate()
 
 
main()