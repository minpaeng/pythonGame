from tkinter import *
import random

lists=["abandon","machine","retirement","particular","revolution","victorious","technological"]
word= random.choice(lists)
b=len(word)

list2=["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]

window = Tk()
window.title("몰랑이")
window.geometry("1000x600+100+40")


#추측값 입력창 
guessframe=Frame(window,bg="pink")
guessframe.pack(side=LEFT,fill=BOTH,expand=1)

life=10
true=0

def guess_all():
    
    #문자 입력창
    guess_e=Entry(guessframe)
    guess_e.grid(row=1,column=0,columnspan=3)

    #정답 및 라이프 관련창
    textview=Text(guessframe,width=30,heigh=40)
    textview.grid(row=2,column=0)
    textview.insert(END,str("한글자씩 알파벳 소문자로 입력해주세요."))
    textview.insert(END,str("\n"))
    for i in range(b):
        textview.insert(END,list2[i])              #'_'를 b개 출력
    textview.insert(END,"\n")

    def press():
        global life
        global true
        if life>0:
            d = 0
            textview.insert(END,"\n입력한 글자: "+str(guess_e.get()))
            for i in range(b):
                if word[i]==str(guess_e.get()):
                    textview.insert(END,"\n")
                    textview.insert(END,str(i+1)+"번째 문자 정답입니다!")
                    textview.insert(END,"\n")
                    list2[i]=str(guess_e.get())
                    for i in range(b):
                        textview.insert(END,list2[i])
                    textview.insert(END,"\n")
                    true +=1
                else:
                    d +=1
                if d==b:
                    life += -1
                    textview.insert(END,"\n입력하신 문자는 없습니다.")
                    textview.insert(END,"\nlife="+str(life))
                    textview.insert(END,"\n")
                    for i in range(b):
                        textview.insert(END,list2[i])
                    textview.insert(END,"\n")
                #life에 따라 그림을 그린다   
                if life == 9:
                    canvas.create_oval(270,75,320,205,fill="white",width=4)
                if life == 8:
                    canvas.create_oval(320,75,370,205,fill="white",width=4)
                if life == 7:
                    canvas.create_oval(150,150,500,500,fill="white",width=4)
                if life == 6:
                    canvas.create_oval(185,300,260,375,fill="pink",width=0)
                if life == 5:
                    canvas.create_oval(390,300,465,375,fill="pink",width=0)
                if life == 4:
                    canvas.create_oval(213,280,253,320,fill="black")
                if life == 3:
                    canvas.create_oval(397,280,437,320,fill="black")
                if life == 2:
                    canvas.create_oval(325,290,325,315,width=5)
                if life == 1:
                    canvas.create_line(325,315,295,328,width=5)
                if life == 0:
                    canvas.create_line(325,315,355,328,width=5)
                    textview.insert(END,"\nGAME OVER")
                    textview.insert(END,"\n정답은 "+word)
            guess_e.delete(0,END)
            #사용자가 문자를 다 맞추었을때 출력
            if true == b:
                textview.insert(END,"\nYOU WIN!!")
    #입력버튼
    guess_b=Button(guessframe,text="입력",command=press)
    guess_b.grid(row=1,column=3,columnspan=5,sticky=W)
    textview.insert(END,"\n문자를 입력한 후 '입력'버튼을 눌러주세요")

start_b=Button(guessframe,text="Game Start",font='Arial 16',command=guess_all,width=14)
start_b["fg"]="red"
start_b.grid(row=0, column=0,columnspan=5)

#캔버스 화면
canvasframe=Frame(window)
canvasframe.pack(side=LEFT,expand=1,fill=BOTH)
canvas=Canvas(canvasframe,width=700,height=400,bg="skyblue")
canvas.pack(side=LEFT,fill=BOTH)
