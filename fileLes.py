import turtle as t

RND = 360  # 360 градусов в замкнутой фигуре
dist = 120  # длинна
figs = 8  # число figs
sides = 4  # число сторон
f_angle = RND / figs  # угол для наклона фигур
angle = RND / sides  # угол
fig_count = 0  # счетчик figs
count = 0  # счетчик сторон

while fig_count < figs:  # счетчик фигур
    count = 0  # обнуляем счетчик сторон
    while count < sides:  # счетчик сторон фигур
        t.forward(dist)
        t.right(angle)
        count += 1
    fig_count += 1
    t.right(f_angle)

t.mainloop()
