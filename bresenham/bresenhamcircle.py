from PIL import Image

def draw_circle_bresenham(image, xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r
    pixels = image.load()

    def plot_circle_points(xc, yc, x, y):
        pixels[xc + x, yc + y] = (255, 255, 255)
        pixels[xc - x, yc + y] = (255, 255, 255)
        pixels[xc + x, yc - y] = (255, 255, 255)
        pixels[xc - x, yc - y] = (255, 255, 255)
        pixels[xc + y, yc + x] = (255, 255, 255)
        pixels[xc - y, yc + x] = (255, 255, 255)
        pixels[xc + y, yc - x] = (255, 255, 255)
        pixels[xc - y, yc - x] = (255, 255, 255)

    plot_circle_points(xc, yc, x, y)
    
    while y >= x:
        x += 1
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        plot_circle_points(xc, yc, x, y)

xc, yc = 100, 100 
r = 50  

image_size = (200, 200)
image = Image.new("RGB", image_size, (0, 0, 0))

draw_circle_bresenham(image, xc, yc, r)

image.show()
image.save("bresenham_circle.png")
