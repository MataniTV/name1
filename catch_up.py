from pygame import *



x_b = 0
y_b = 0
window = display.set_mode((700, 500))
display.set_caption("Догонялки")
background = transform.scale(image.load("background.png"), (700, 500))

x1 = 100 
y1 = 100

x2 = 400
y2 = 400

FPS = 60
clock = time.Clock()

sprite1 = transform.scale(image.load("sprite1.png"), (100, 100)) 
sprite2 = transform.scale(image.load("sprite2.png"), (100, 100))



game = True
while game:
    window.blit(background,(x_b, y_b))
    window.blit(sprite1,(x1, y1))
    window.blit(sprite2,(x2, y2))


    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            keys = key.get_pressed()
            if keys[K_LEFT]:
                display.update()
                x_b += 1
                x1 -= 10
            if keys[K_RIGHT]:
                display.update()
                x_b -= 1
                x1 += 10



    display.update()
    clock.tick(FPS)