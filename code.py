import os
from tkinter import *

root = Tk()
root.title('SRC PING INTERFACE')
root.geometry('1300x1366')

canvas1 = Canvas(root, width=2000, height=30, bg="light blue")
canvas1.create_text(770, 20, text="SRC PING INTERFACE", fill="white", font='sans 20 bold')
canvas1.place(x=0, y=0)

window1 = Canvas(root, width=310, height=310)
window1.place(x=600, y=50)
image = PhotoImage(file='drdo.png')
window1.create_image(0, 0, anchor=NW, image=image)

root.configure(background='light blue')
root.iconphoto(False, PhotoImage(file='drdo.png'))


def ipping_ceptem():
    hostname = "www.google.com"
    response = os.system("ping -n 6 " + hostname)
    if response == 0:
        label = Label(root, text="CEPTEM CONNECTED", fg='green', bg='light blue')
        label.place(x=350, y=560)
    else:
        label = Label(root, text="CEPTEM NOT CONNECTED", fg='red', bg='light blue')
        label.place(x=350, y=560)


def ipping_issa():
    hostname = "10.2.158.2"
    response = os.system("ping -n 6 " + hostname)
    if response == 0:
        label = Label(root, text="ISSA CONNECTED", fg='green', bg='light blue')
        label.place(x=550, y=560)
    else:
        label = Label(root, text="ISSA NOT CONNECTED", fg='red', bg='light blue')
        label.place(x=550, y=560)


def ipping_jcb():
    hostname = "10.2.208.2"
    response = os.system("ping -n 6 " + hostname)
    if response == 0:
        label = Label(root, text="JCB CONNECTED", fg='green', bg='light blue')
        label.place(x=750, y=560)
    else:
        label = Label(root, text="JCB NOT CONNECTED", fg='red', bg='light blue')
        label.place(x=750, y=560)


def ipping_sag():
    hostname = "10.2.60.2"
    response = os.system("ping -n 6 " + hostname)
    if response == 0:
        label = Label(root, text="SAG CONNECTED", fg='green', bg='light blue')
        label.place(x=950, y=560)
    else:
        label = Label(root, text="SAG NOT CONNECTED", fg='red', bg='light blue')
        label.place(x=950, y=560)


def ipping_dgre():
    hostname = "10.2.64.2"
    response = os.system("ping -n 6 " + hostname)
    if response == 0:
        label = Label(root, text="DGRE CONNECTED", fg='green', bg='light blue')
        label.place(x=1150, y=560)
    else:
        label = Label(root, text="DGRE NOT CONNECTED", fg='red', bg='light blue')
        label.place(x=1150, y=560)


def ipping_lastec():
    hostname = "10.2.70.2"
    response = os.system("ping -n 6 " + hostname)
    if response == 0:
        label = Label(root, text="LASTEC CONNECTED", fg='green', bg='light blue')
        label.place(x=450, y=710)
    else:
        label = Label(root, text="LASTEC NOT CONNECTED", fg='red', bg='light blue')
        label.place(x=450, y=710)


def ipping_cce():
    hostname = "0.0.0.0"
    response = os.system("ping -n 6 " + hostname)
    if response == 0:
        label = Label(root, text="CCE CONNECTED", fg='green', bg='light blue')
        label.place(x=650, y=710)
    else:
        label = Label(root, text="CCE NOT CONNECTED", fg='red', bg='light blue')
        label.place(x=650, y=710)


def ipping_firewall():
    hostname = "10.2.51.2"
    response = os.system("ping -n 6 " + hostname)
    if response == 0:
        label = Label(root, text="FIREWALL CONNECTED", fg='green', bg='light blue')
        label.place(x=850, y=710)
    else:
        label = Label(root, text="FIREWALL NOT CONNECTED", fg='red', bg='light blue')
        label.place(x=850, y=710)


def ipping_drona():
    hostname = "10.2.114.1"
    response = os.system("ping -n 6 " + hostname)
    if response == 0:
        label = Label(root, text="DRONA CONNECTED", fg='green', bg='light blue')
        label.place(x=1050, y=710)
    else:
        label = Label(root, text="DRONA NOT CONNECTED", fg='red', bg='light blue')
        label.place(x=1050, y=710)


btn1 = Button(root, text='CEPTEM', bd='10', command=ipping_ceptem, font='sans 12 bold')
btn1.place(x=350, y=495)
btn2 = Button(root, text='ISSA', bd='10', command=ipping_issa, font='sans 12 bold')
btn2.place(x=550, y=495)
btn3 = Button(root, text='JCB', bd='10', command=ipping_jcb, font='sans 12 bold')
btn3.place(x=750, y=495)
btn4 = Button(root, text='SAG', bd='10', command=ipping_sag, font='sans 12 bold')
btn4.place(x=950, y=495)
btn5 = Button(root, text='DGRE', bd='10', command=ipping_dgre, font='sans 12 bold')
btn5.place(x=1150, y=495)
btn6 = Button(root, text='LASTEC', bd='10', command=ipping_lastec, font='sans 12 bold')
btn6.place(x=450, y=650)
btn7 = Button(root, text='CCE', bd='10', command=ipping_cce, font='sans 12 bold')
btn7.place(x=650, y=650)
btn8 = Button(root, text='FIREWALL', bd='10', command=ipping_firewall, font='sans 12 bold')
btn8.place(x=850, y=650)
btn9 = Button(root, text='DRONA', bd='10', command=ipping_drona, font='sans 12 bold')
btn9.place(x=1100, y=650)

canvas2 = Canvas(root, width=2000, height=30, bg="light blue")
canvas2.create_text(720, 20, text="Developed For: NSD, DESIDOC, DRDO ©️ 2022 Developed by: Ritika, Intern",
                    fill="white", font='sans 12 bold')
canvas2.place(x=0, y=850)
root.mainloop()
