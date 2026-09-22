from turtle import *
import colorsys
import math

speed(0)
bgcolor("black")
hideturtle()

# =========================
# PÉTALOS AMARILLOS
# =========================

goto(0, -40)
h = 0

for i in range(18):
    for j in range(20):

        # Amarillo con pequeñas variaciones
        c = colorsys.hsv_to_rgb(
            0.13,
            1,
            1 - j * 0.02
        )

        color(c)

        rt(90)
        circle(160 - j * 6, 90)

        lt(90)
        circle(160 - j * 6, 90)

        rt(180)

    circle(40, 20)


# =========================
# CENTRO DEL GIRASOL
# =========================

color("#5A2E00")
shape("circle")
shapesize(0.35)

phi = 137.508 * (math.pi / 180)

for i in range(300):

    r = 3.2 * math.sqrt(i)
    theta = i * phi

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    penup()
    goto(x, y)

    # Variación de tonos del centro
    if i % 3 == 0:
        color("#8B4513")
    elif i % 3 == 1:
        color("#6B2F00")
    else:
        color("#A0522D")

    stamp()


# =========================
# FINAL
# =========================

penup()
goto(0, -300)
color("yellow")
write(
    "🌻",
    align="center",
    font=("Arial", 30, "bold")
)

done()