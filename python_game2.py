import random
import turtle

t=turtle.Turtle()
t.width(2)

life=10                 #그림이 10번 그려지므로 목숨은 10개
true=0

#타원을 그리는 함수
def oval(a):
    t.width(3)
    t.color("brown")
    t.penup()
    t.goto(-12-a,155)
    t.pendown()
    for x in range(-12-a,13-a):
        t.goto(x,((800*(1-(((x+a)**2)/144)))**0.5)+155)
    t.penup()
    t.goto(-12-a,155)
    t.pendown()
    for x in range(-12-a,13-a):
        t.goto(x,(-((800*(1-(((x+a)**2)/144)))**0.5))+155)

lists=["abandon","machine","retirement","particular","revolution","victorious","technological"]
word= random.choice(lists)

alpabet1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
alpabet2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]

#게임 시작 부분
t.penup()
t.goto(-300,250)
t.pendown()
t.write("GAME START!", font=("Arial",30,"normal"))
t.hideturtle()
t.color("white")
t.penup()
t.goto(-300,300)
t.pendown()
t.fillcolor("white")
t.begin_fill()
for i in range(4):
    t.forward(400)
    t.right(90)
t.end_fill()

#터틀 그래픽에 알파벳표시
t.color("black")
t.speed(100)
for i in range(13):             
    t.penup()
    t.goto(300,290-i*50)
    t.pendown()
    t.write(alpabet1[i],font=("Arial",20,"normal"))
for i in range(13):
    t.penup()
    t.goto(350,290-i*50)
    t.pendown()
    t.write(alpabet2[i], font=("Arial",20,"normal"))

#밑줄 및 주의사항
b=len(word)
t.up()
t.goto(-250,-200)
t.down()
t.write("ㅡ"*b,font=("Arial",15,"normal"))
print("주의사항1: 한글자씩 알파벳 소문자로 입력해야 합니다.")
print("주의사항2: 다음 글자를 입력할때 잠시 기다려 주십시오.")

#구현부
while life>0:
    d=0
    guess=input("글자를 추측해주세요: ")
    if guess in alpabet1:                   #받은 알파벳을 터틀그래픽에서
        for i in range(13):              #지우도록 함 
            if guess==alpabet1[i]:
                t.penup()
                t.goto(300,290-i*50)
                t.pendown()
                t.color("red")
                t.write("X", font=("Airal",20,"bold"))
                t.hideturtle()
    if guess in alpabet2:
        for i in range(13):
            if guess==alpabet2[i]:
                t.penup()
                t.goto(350,290-i*50)
                t.pendown()
                t.color("red")
                t.write("X", font=("Arial",20,"bold"))
                t.hideturtle()      
    for i in range(b):
        if word[i]==guess:
            t.penup()
            t.goto(-250+i*20,-190)
            t.pendown()
            t.color("black")
            t.write(guess, font=("Arial",25,"normal"))
            t.hideturtle()
            print(str(i+1)+"번째 문자 정답입니다!")
            true +=1
        else:
            d +=1
        if d==b:
            life += -1
            print("입력하신 문자는 없습니다.")
            print("life=",life)
        #life에 따라 그림을 그린다   
        if life == 9:
            oval(12)
        if life == 8:
            oval(-12)
        if life == 7:
            t.penup()
            t.goto(0,-50)
            t.pendown()
            t.color("brown")
            t.fillcolor("white")
            t.begin_fill()
            t.circle(100)      
            t.end_fill()  
        if life == 6:
            t.penup()
            t.goto(-60,20)
            t.color("pink")
            t.pendown()
            t.begin_fill()
            t.circle(20)
            t.end_fill()
        if life == 5:
            t.penup()
            t.goto(60,20)
            t.color("pink")
            t.pendown()
            t.begin_fill()
            t.circle(20)
            t.end_fill()
        if life == 4:
            t.penup()
            t.color("brown")
            t.goto(-55,50)
            t.pendown()
            t.begin_fill()
            t.circle(10)
            t.end_fill()
        if life == 3:
            t.penup()
            t.goto(55,50)
            t.pendown()
            t.color("brown")
            t.begin_fill()
            t.circle(10)
            t.end_fill()
        if life == 2:
            t.penup()
            t.goto(0,50)
            t.pendown()
            t.color("brown")
            t.width(5)
            t.goto(0,65)
        if life == 1:
            t.penup()
            t.goto(0,50)
            t.pendown()
            t.color("brown")
            t.width(5)
            t.goto(-14,45)
        if life == 0:
            t.penup()
            t.goto(0,50)
            t.pendown()
            t.color("brown")
            t.goto(14,45)
            t.penup()
            t.goto(-250,0)
            t.pendown()
            t.color("red")
            t.write("GAME OVER", font=("Arial",50,"bold"))
            t.penup()
            t.goto(-250,-70)
            t.pendown()
            t.write("정답은 "+word, font=("Arial",50,"bold"))
            t.hideturtle()
    #사용자가 문자를 다 맞추었을때 출력
    if true == b:
        t.penup()
        t.left(45)
        t.goto(-200,0)
        t.pendown()
        t.color("red")
        t.write("YOU WIN!!", font=("Arial",50,"bold"))
        t.hideturtle()
        break
