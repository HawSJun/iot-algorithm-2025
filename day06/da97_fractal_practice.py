from tkinter import *
import random

## 함수선언
def drawCircle(x, y, r):
    canvas.create_oval(x-r, y-r, x+r, y+r, width=2, outline=random.choice(colors))
    if r >= 5:
        drawCircle(x+r//2, y, r//2)
        drawCircle(x-r//2, y, r//2)

## 전역변수
colors = ['red', 'green', 'blue', 'black', 'orange', 'indigo', 'violet']
wSize = 1000
radius = 400

## 메인코드
root = Tk()
root.title('원 모양의 프랙탈')
canvas = Canvas(root, height=wSize, width=wSize, bg='white')
canvas.pack()

drawCircle(wSize//2, wSize//2, radius)

root.mainloop()