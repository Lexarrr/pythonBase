import turtle as t

colors = ['red', 'orange', 'yellow', 'green', 'aquamarine', 'blue', 'cyan', 'purple', 'pink', 'white']

t.bgcolor('black')
t.speed(0)  # maxspeed
angle = 323 / len(colors) - 1

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
