from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry('700x500')
win.resizable(0,0)


#___________________________________________________________________________________________________________________________________________________________________________

frame_gender = LabelFrame(win,text='جنسیت',labelanchor='ne')
frame_gender.place(x=600,y=300,width=85)

frame_information = LabelFrame(win,text='مشخصات فردی',height=100,labelanchor='ne')
frame_information.place(x=10,y=10,width=680)    

frame_skill = LabelFrame(win,text='مهارت ها',height=100,labelanchor='ne')
frame_skill.place(x=10,y=150,width=680)
#____________________________________________________________________________________________________________________________________________________________________________
def exit():
    win.destroy()

def clear():
    ent_ed.delete(0,END)
    ent_lname.delete(0,END)
    ent_name.delete(0,END)
    ent_phone.delete(0,END)
    var_skill.set('g')
    var.set('آقای/خانم')
    ent_name.focus_set()

def submit():
    if ent_name.get() == '' or ent_lname.get() == '':
        messagebox.showinfo('error','!باید نام و نام خانوادگی را مشخص کنید')    
        var.set('آقای/خانم')
    else:    
        win_1 = Toplevel(win)
        win.geometry('600x400')
        win.resizable(0,0)
        win.withdraw()
        lbl_welcome = Label(win_1,text=f'!خوش آمدید {ent_name.get()} {ent_lname.get()} {var.get()}')
        lbl_welcome.place(x=10,y=10)


#____________________________________________________________________________________________________________________________________________________________________________
var = StringVar()
var.set('آقای/خانم')

r_gender = Radiobutton(frame_gender,text='آقا',variable=var,value='آقای')
r_gender.pack(anchor='e')
r_gender_1 = Radiobutton(frame_gender,text='خانم',variable=var,value='خانم')
r_gender_1.pack(anchor='e')

var_skill = StringVar()
var_skill.set('fg fmgdmftdttrtjyey5')
r_python = Radiobutton(frame_skill,text='python',variable=var_skill,font='arial 15 bold',value='python')
r_python.place(x=10,y=20)
r_java = Radiobutton(frame_skill,text='java',font='arial 18 bold',variable=var_skill,value='java')
r_java.place(x=270,y=20)
r_c = Radiobutton(frame_skill,font='arial 18 bold',text='c#',variable=var_skill,value='c#')
r_c.place(x=500,y=20)
#____________________________________________________________________________________________________________________________________________________________________________


lbl_name = Label(frame_information,text=':نام',font='arial 15 bold')
lbl_name.place(x=575,y=7)

lbl_lname = Label(frame_information,text=':نام خانوادگی',font='arial 15 bold')
lbl_lname.place(x=554,y=40)

lbl_ed = Label(frame_information,text=':تحصیلات',font='arial 15 bold')
lbl_ed.place(x=150,y=6)

lbl_phone = Label(frame_information,text=':تلفن',font='arial 15 bold')
lbl_phone.place(x=150,y=40)

lbl_star = Label(frame_information,text='*',font='arial 18 bold',fg='red')
lbl_star.place(x=610,y=7)

lbl_star2 = Label(frame_information,text='*',font='arial 18 bold',fg='red')
lbl_star2.place(x=650,y=40)
#_______________________________________________________________________________________________________________________________________________________________________________

ent_name = Entry(frame_information,width=20)
ent_name.place(x=451,y=13)

ent_lname = Entry(frame_information,width=20)
ent_lname.place(x=431,y=49)

ent_ed = Entry(frame_information,width=20)
ent_ed.place(x=10,y=10)

ent_phone = Entry(frame_information,width=20)
ent_phone.place(x=10,y=49)

#________________________________________________________________________________________________________________________________________________________________________________

btn_sumbit = Button(win,text='submit',font='tahoma 15 bold',command=submit)
btn_sumbit.place(x=30,y=330)

btn_clear = Button(win,text='clear',font='tahoma 15 bold',command=clear)
btn_clear.place(x=150,y=330)

btn_exit = Button(win,text='exit',font='tahoam 15 bold',command=exit)
btn_exit.place(x=250,y=330)



win.mainloop()