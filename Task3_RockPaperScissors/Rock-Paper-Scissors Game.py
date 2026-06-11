from tkinter import *
from tkinter import messagebox as mb
import random

root = Tk()
root.title('Rock paper scissors')
root.geometry('700x750')

rock1 = PhotoImage(file='rock1.png').subsample(2)
paper1 = PhotoImage(file='paper1.png').subsample(2)
scissors1 = PhotoImage(file='scissor1.png').subsample(2)

rock2 = PhotoImage(file='rock2.png').subsample(2)
paper2 = PhotoImage(file='paper2.png').subsample(2)
scissors2 = PhotoImage(file='scissors2.png').subsample(2)

comp_value = {0:'Rock', 1:'Paper', 2:'Scissors'}
comp_img = {'Rock':rock2, 'Paper':paper2, 'Scissors':scissors2}
count = pl_score = com_score = 0

def reset_game():
    global count, pl_score, com_score

    count = pl_score = com_score = 0

    b1['state'] = 'normal'
    b2['state'] = 'normal'
    b3['state'] = 'normal'

    l1.config(text='Player', image='')
    l3.config(text='Computer', image='')
    l4.config(text='')

    player_score.config(text='Player: 0')
    computer_score.config(text='Computer: 0')

def button_disable():
    b1['state'] = 'disabled'
    b2['state'] = 'disabled'
    b3['state'] = 'disabled'

def disp_score():
    global pl_score,com_score
    if pl_score > com_score:
        mb.showinfo('Game result', 'congrats! you won!!')
    elif pl_score < com_score:
        mb.showinfo('Game result', 'you Lose! Try again!!')
    else:
        mb.showinfo('Game result', 'Its a Tie!!')

def is_rock():
    global count, pl_score,com_score
    count+=1
    if count<=5:
        c_v = comp_value[random.randint(0,2)]
        if c_v == 'Rock':
            result = "Tie"
        elif c_v == 'Paper':
            result = 'Computer wins'
            com_score +=1
        else:
            result = 'Player win'
            pl_score +=1
        l4.config(text=result)
        l1.config(image=rock1)
        l3.config(image = comp_img[c_v])
        player_score.config(text='Player: ' + str(pl_score))
        computer_score.config(text='Computer: ' + str(com_score))
        if count == 5:
            button_disable()
            disp_score()


def is_paper():
    global count, pl_score,com_score
    count+=1
    if count<=5:
        c_v = comp_value[random.randint(0,2)]
        if c_v == 'Rock':
            result = "Player win"
            pl_score += 1
        elif c_v == 'Paper':
            result = 'Tie'
        else:
            result = 'Computer win'
            com_score +=1
        l4.config(text=result)
        l1.config(image=paper1)
        l3.config(image = comp_img[c_v])
        player_score.config(text='Player: ' + str(pl_score))
        computer_score.config(text='Computer: ' + str(com_score))
        if count == 5:
            button_disable()
            disp_score()

def is_scissors():
    global count, pl_score,com_score
    count+=1
    if count<=5:
        c_v = comp_value[random.randint(0,2)]
        if c_v == 'Rock':
            result = "Computer win"
            com_score +=1
        elif c_v == 'Paper':
            result = 'Player wins'
            pl_score +=1
        else:
            result = 'Tie'
        l4.config(text=result)
        l1.config(image=scissors1)
        l3.config(image = comp_img[c_v])
        player_score.config(text='Player: ' + str(pl_score))
        computer_score.config(text='Computer: ' + str(com_score))
        if count == 5:
            button_disable()
            disp_score()

title = Label(root, text='Rock Paper Scissors Game', font="normal 20 bold", bg='red4', fg='snow', width=30)
title.pack(pady=10)

f1 = Frame(root)
l1 = Label(f1,text='Player', font=10)
l2 = Label(f1,text='VS', font="normal 10 bold")
l3 = Label(f1,text='Computer', font=10)

f1.pack()
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root, text="", font='normal 20 bold', bg='white', width=15, borderwidth=2, relief="solid")
l4.pack(pady=15)

f2 = Frame(root)
f2.pack(pady=10)

b1=Button(f2, text='Rock', font='segoeUI 14 bold', bd=5, width=8, command=is_rock)
b2=Button(f2, text='Paper', font='segoeUI 14 bold', bd=5, width=8, command=is_paper)
b3=Button(f2, text='Scissors', font='segoeUI 14 bold', bd=5, width=8, command=is_scissors)

b1.pack(side=LEFT, padx=5)
b2.pack(side=LEFT, padx=5)
b3.pack(side=LEFT, padx=5)

f3 = Frame(root, bg='blue2', width=450, height=80)
f3.pack(pady=10)
f3.pack_propagate(0)

score = Label(f3, text='Score', font='normal 15 bold', fg='white', bg='blue2')
score.pack(pady=5)

player_score = Label(f3, text='Player: ', font='normal 15 bold', fg='white', bg='blue2')
player_score.pack(side=LEFT, padx=30, pady=5)

computer_score = Label(f3, text='Computer: ', font='normal 15 bold', fg='white', bg='blue2')
computer_score.pack(side=RIGHT, padx=30, pady=5)

button_frame = Frame(root)
button_frame.pack(pady=20)

reset = Button(root, text='Reset Game', font=10, fg='white', bg='green4', command=reset_game)
reset.pack(in_=button_frame, side=LEFT, padx=20)
close = Button(root, text='Exit Game', font=10, fg='white', bg='black', command=root.destroy)
close.pack(in_=button_frame, side=LEFT, padx=20)

root.mainloop()
