import matplotlib.pyplot as plt
import math

def bresenham_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    
    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    
    return points

def plot_line(points, color='black'):
    x_vals, y_vals = zip(*points)
    plt.plot(x_vals, y_vals, color=color)

center_x, center_y = 0, 0
radius = 100 

angle_hour = 60
angle_minute = 90

x1_hour = int(center_x + (radius * 0.6) * math.cos(math.radians(90 - angle_hour)))
y1_hour = int(center_y + (radius * 0.6) * math.sin(math.radians(90 - angle_hour)))

x1_minute = int(center_x + radius * math.cos(math.radians(90 - angle_minute)))
y1_minute = int(center_y + radius * math.sin(math.radians(90 - angle_minute)))

hour_line_points = bresenham_line(center_x, center_y, x1_hour, y1_hour)
minute_line_points = bresenham_line(center_x, center_y, x1_minute, y1_minute)

plt.figure(figsize=(6,6))

plot_line(hour_line_points, color='blue')
plot_line(minute_line_points, color='red') 

plt.xlim(-radius, radius)
plt.ylim(-radius, radius)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)

plt.show()
