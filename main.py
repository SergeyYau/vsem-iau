from tkinter import*
from tkinter.messagebox import showinfo
c = 0
def clck():
    global c
    if var1.get() == 3:
        c += 1
    if var2.get() == 4:
        c += 1
    if var3.get() == 8:
        c += 1
    if var4.get() == 11:
        c += 1
    if var5.get() == 15:
        c += 1
    showinfo(title='Результат', message=f'Ваш результат {c} из 5!')
    c = 0


root = Tk()
root.title('Тест')
root.geometry('360x950')
var1 = IntVar()
var1.set(0)
var2 = IntVar()
var2.set(0)
var3 = IntVar()
var3.set(0)
var4 = IntVar()
var4.set(0)
var5 = IntVar()
var5.set(0)
lb1 = Label(text='Квадрат 9?', font=('Arial 20 bold'))
lb1.pack()

r_1 = Radiobutton(text='72', variable=var1, value=1, font=('Arial 20'))
r_1.pack()
r_2 = Radiobutton(text='18', variable=var1, value=2, font=('Arial 20'))
r_2.pack()
r_3 = Radiobutton(text='81', variable=var1, value=3, font=('Arial 20'))
r_3.pack()

lb2 = Label(text='Корень 169?', font=('Arial 20 bold'))
lb2.pack()

r_4 = Radiobutton(text='13', variable=var2, value=4, font=('Arial 20'))
r_4.pack()
r_5 = Radiobutton(text='15', variable=var2, value=5, font=('Arial 20'))
r_5.pack()
r_6 = Radiobutton(text='17', variable=var2, value=6, font=('Arial 20'))
r_6.pack()

lb3 = Label(text='Первообразная 8х?', font=('Arial 20 bold'))
lb3.pack()

r_7 = Radiobutton(text='8', variable=var3, value=7, font=('Arial 20'))
r_7.pack()
r_8 = Radiobutton(text='4х**2', variable=var3, value=8, font=('Arial 20'))
r_8.pack()
r_9 = Radiobutton(text='8х**2', variable=var3, value=9, font=('Arial 20'))
r_9.pack()

lb4 = Label(text='Сумма углов треугоьника', font=('Arial 20 bold'))
lb4.pack()

r_10 = Radiobutton(text='360', variable=var4, value=10, font=('Arial 20'))
r_10.pack()
r_11 = Radiobutton(text='180', variable=var4, value=11, font=('Arial 20'))
r_11.pack()
r_12 = Radiobutton(text='90', variable=var4, value=12, font=('Arial 20'))
r_12.pack()

lb5 = Label(text='че как тест?', font=('Arial 20 bold'))
lb5.pack()

r_13 = Radiobutton(text='плохо', variable=var5, value=13, font=('Arial 20'))
r_13.pack()
r_14 = Radiobutton(text='ужасно', variable=var5, value=14, font=('Arial 20'))
r_14.pack()
r_15 = Radiobutton(text='молодец! сделал на 5!', variable=var5, value=15, font=('Arial 20'))
r_15.pack()

btn1 = Button(text='Проверить', command=clck)
btn1.pack()


root.mainloop()