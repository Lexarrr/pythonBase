import turtle as t

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'aquamarine', 'white', ]

t.bgcolor('black')
t.speed(0)  # maxspeed
angle = 360 / len(colors) - 2

for x in range(300):
    t.pencolor(colors[x % len(colors)])
    t.width(x // 100 + 1)
    t.forward(x)
    t.left(angle)

t.mainloop()

aq = []

for x in range(101):
    aq.append(x)
print(aq[0:len(aq):5])
