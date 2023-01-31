#Пример окна#
'''from tkinter import *
root=Tk()
def button_clicked():
    print('Button was clicked')
def close():
    root.destroy()
    root.quit()

Label(text='Window').pack()
Entry(text='Input').pack()
Button(text='Button',bg='orange',width='30',height='50',activebackground='blue').pack()

root.title('Program 1')
root.geometry('300x200')
root.mainloop()'''

#Сломанный калькулятор
'''from tkinter import*
def button_1():
    l.config(int(a.get())*2)
root=Tk()
root.title('Приложение')
root.geometry('500x300')
a=Entry(root,width=15,bg='gray',fg='cyan',font='consolas')
a.pack()
Button(root,text='Умножить на 2',width=15,height=2,bg='white',command=button_1).pack()
l=Label(root,width=15,bg='gray',fg='cyan',font='consolas')
l.pack()
root.mainloop()'''


###################
'''from tkinter import*
root=Tk()
canvas=Canvas(root,width=200,height=200,bg='cyan')
canvas.pack()
canvas.create_polygon(15,15,190,140,20,120,fill='yellow',width=5,outline='blue',dash=(30,20,10))
canvas.create_line(30,40,300,400)
Button(root,text='Умножить на 2').pack()
root.mainloop()'''


##########игра кликер
'''from tkinter import*
import random
score,max_score=0,18
size_x,size_y=1000,800
def put():
    global button
    button=Button(root,text='Нажми меня!',bg='gray',activebackground='red',command=click)
    button.place(x=random.randint(20,size_x),y=random.randint(10,size_y))
def click():
    global score
    global label
    button.destroy()
    if score <=max_score:
        score+=1
        put()
    else:
        label=Label(root,text='Вы выйграли, \n поздравляем!')
        label.place(relx=0.5,rely=0.5)
root=Tk()
root.title('Наша первая игра')
root.geometry(f'{size_x}x{size_y}')
root.resizable(False,False)
put()
root.mainloop()'''


#сложный калькулятор
'''from tkinter import*
def set_value(formula):
    if formula=='':
        l['text']='0'
    else:
        l['text']=str(eval(formula))
def logic(operation):
    if operation=='C':
        set_value('')
    elif operation=='DEL':
        set_value(l['text'][1:-1])
    elif operation=='X^2':
        set_value(str((eval(l['text']))**2))
    elif operation=='=':
        set_value(l['text'])
    else:
        if l['text']=='0':
            l['text']=''
        l['text']=l['text']+operation
root=Tk()
root['bg']='black'
root.title('калькулятор')
root.geometry('485x550+220+220')
root.resizable(False,False)
l=Label(text='0',font=('Consolas',21,'bold'),bg='black',foreground='white')
l.place(x=11,y=50)
list=['C','DEL','*','=','1','2','3','/','4','5','6','+','7','8','9','-','(','0',')','X^2']
x=10
y=140

for lis in list:
    com=lambda x=lis: logic(x)
    Button(text=lis,bg='white',font=('Consolas',15),command=com).place(x=x,y=y,width=115,height=79)
    x+=117
    if x>400:
        x=10
        y+=81

root.mainloop()'''
##################################################### csv

'''filename=r'C:\data.csv'
def get_line():
    line=list(input().split())
    return (int(line[0]),line[1],line[2],int(line[3]),int(line[4]),int(line[5]))
def insert(line):
    if line not in data:
        data.append(line)
def write_to_file(filename):
    with open(filename, 'w') as file:
        file.write(','.join(columns))
        for line in data:
            line=[str(i) for i in line]
            file.write(','.join(line)+'\n')
def read_to_file(filename):
    with open(filename, 'r') as file:
        columns = tuple(file.readline().split(','))
        data = []
        for line in file:
            line = line.split(',')
            data.append((int(line[0]),line[1],line[2],int(line[3]),int(line[4]),int(line[5])))
        return columns, data
def print_data():
    m=max([len(i) for i in columns])
    for i in columns:
        print(str(i).ljust(m+1, ' '), end = '')
    print()
    for line in data:
        for i in line:
            print(str(i).ljust(m+1, ' '), end = '')
        print()
global data, columns
columns, data = read_to_file(filename)
insert(get_line())
write_to_file(filename)
print_data()'''

################################################







