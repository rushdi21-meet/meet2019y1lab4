import turtle
turtle.bgcolor("purple")
x=turtle.clone()
x.color("yellow")
x.shape('circle')
r=turtle.clone()
r.color('green')
r.shape('arrow')
x.goto(0,150)
x.goto(-75,150)
x.color('white')
x.goto(-75,0)
x.stamp()
r.goto(0,-150)
r.goto(75,-150)
r.color('blue')
r.goto(75,0)
turtle.mainloop()
