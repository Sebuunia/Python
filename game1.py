import turtle
import random
import time

global atak

window = turtle.Screen()

Bok = 600

X = -300
Y = 300


window.setup(Bok, Bok)
window.title('Tic Tac Toe')
window.bgcolor('Black')

tu = turtle.Turtle()
tu.color('White')
tu.pensize(8)
tu.speed(0)
tu.hideturtle()

tabelka = [[None,None,None], 
            [None,None,None],
             [None,None,None]]

space = int(Bok / 3)

atak = random.choice(['x', 'o'])

for a in [1,2]:
    tu.penup()
    tu.goto(X + a*space, Y)
    tu.pendown()
    tu.goto(X + a*space, -Y)

    tu.penup()
    tu.goto(X, Y - a*space)
    tu.pendown()
    tu.goto(-X, Y - a*space)

def check():
    
    #cant
    if tabelka[0][0] == tabelka[1][1] == tabelka[2][2]: return tabelka[2][2]
    if tabelka[0][2] == tabelka[1][1] == tabelka[2][0]: return tabelka[2][0]

    #verse
    # for w in range(2):
    if tabelka[2][0] == tabelka[2][1] == tabelka[2][2]: return tabelka[2][2]
    if tabelka[1][0] == tabelka[1][1] == tabelka[1][2]: return tabelka[1][2]
    if tabelka[0][0] == tabelka[0][1] == tabelka[0][2]: return tabelka[0][2]

    #in column
    # for k in range(2):
    if tabelka[0][0] == tabelka[1][0] == tabelka[2][0]: return tabelka[2][0]
    if tabelka[0][1] == tabelka[1][1] == tabelka[2][1]: return tabelka[2][1]
    if tabelka[0][2] == tabelka[1][2] == tabelka[2][2]: return tabelka[2][2]


def click(x,y):

    global atak

    column = 0
    verse = 0

    if x < X + space: column = 0
    elif x > X + 2*space: column = 2
    else: column = 1

    if y < Y - 2*space: verse = 2
    elif y > Y - space: verse = 0
    else: verse = 1

    print(verse, column)


    if tabelka[verse][column] != None: return

    column_center = (column*space + space/2) - Bok / 2
    verse_center = (-verse*space - space/2) + Bok / 2

    tu.penup()
    tu.goto(column_center-25, verse_center-25)
    if atak == 'x': tu.write('X', font=('Arial', 50))
    elif atak == 'o': tu.write('O', font=('Arial', 50))
    # else: tu.write('O', font=('Arial', 50))


    tabelka[verse][column] = atak


    if atak == 'o': atak = 'x'
    else: atak = 'o'

    if check() != None:
        tu.penup()
        tu.goto(-150, 0)
        time.sleep(0)
        tu.clear()
        tu.write("Win The Game " + check(), font=('Courier New', 30))

window.onclick(click)

window.listen()
window.mainloop()