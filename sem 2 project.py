from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from functools import partial
from datetime import date
import datetime as dt
import time
import json
import smtplib
import re
#window
import datetime
from tabulate import tabulate
itemlist=[]
b=[]
breakfast=[["Toast",20,100],["Milk",10,200],["Coffee",10,200],["Sandwich",30,100],["Bowl of Cereal",30,100]]
lunch=[["Salad",10,150],["Veg Burger",50,100],["Chicken Burger",70,100],["Rajma Rice",60,150],["Fried Rice",60,100],["Pizza",100,100],["Fries",40,150],["Coke",20,200],["Juice",20,200],["Hot Chocolate",50,150]]
dinner=[["Soup",30,150],["Chapati(veg.)",40,200],["Chapati(chicken)",50,150],["Veg Biryani",40,150],["Chicken Biryani",60,150],["Pav Bhaji",40,100],["Bread Omelette",40,150],["Ice Cream",20,150],["Coke",20,150],["Juice",20,150],["Plum Cake",120,50]]          
list1=[["Ankit",[["Soup",6],["Chapati(veg.)",4],["Pav Bhaji",3]]],["Uday",[["Paneer",2],["Noodles",1]]],["Sanky",[["pasta",3],["samosa",2],["idly",1],["dosa",3]]]]
klist=[]
def proceed(user):
    global klist
    today=date.today()
    today1=str(today)
    clist=today1.split("-")
    now = datetime.datetime.now()
    a=list(now.strftime("%H:%M:%S"))
    b=[]
    c=""
    j=0
    while(j<=len(a)-1):
        if a[j]==":":
          b.append(c)
          c=""
          j=j+1
        else:
          c=c+str(a[j])
          j=j+1
    clist.extend(b)
    breakfast1=[7,8,9,10,11]
    lunch1=[12,13,14,15,16,17]
    dinner1=[18,19,20,21,22,23]
    if len(itemlist)>=3:
         f=open("orders.txt","r")
         blist=[]
         c=f.read()
         dlist=c.split("$")
         dlist[-1]="flag"
         dlist.remove("flag")
         for i in range(len(dlist)):
             dlist[i]=eval(dlist[i])
         for i in range(len(dlist)):
          if int(b[0]) in breakfast1:
            menulist=breakfast1
            if dlist[i][3]==clist[2] and int(dlist[i][4]) in menulist:
                blist.append(dlist[i])
          if int(b[0]) in lunch1:
            menulist=lunch1
            if dlist[i][3]==clist[2] and int(dlist[i][4]) in menulist:
                blist.append(dlist[i])
          if int(b[0]) in dinner1:
            menulist=dinner1
            if dlist[i][3]==clist[2] and int(dlist[i][4]) in menulist:
                blist.append(dlist[i])
          token_no=100+len(blist)
    else:
         f=open("expressorder.txt","r")
         blist=[]
         c=f.read()
         dlist=c.split("$")
         dlist[-1]="flag"
         dlist.remove("flag")
         for i in range(len(dlist)):
             dlist[i]=eval(dlist[i])
         for i in range(len(dlist)):
          if int(b[0]) in breakfast1:
            menulist=breakfast1
            if dlist[i][3]==clist[2] and int(dlist[i][4]) in menulist:
                blist.append(dlist[i])
          if int(b[0]) in lunch1:
            menulist=lunch1
            if dlist[i][3]==clist[2] and int(dlist[i][4]) in menulist:
                blist.append(dlist[i])
          if int(b[0]) in dinner1:
            menulist=dinner1
            if dlist[i][3]==clist[2] and int(dlist[i][4]) in menulist:
                blist.append(dlist[i])
         token_no=len(blist)
    ka=Toplevel(tkWindow)
    ka.state("zoomed")
    kalabel=Label(ka,image=token)
    kalabel.place(relx=0.5,rely=0.5,anchor="center")
    kalab=Label(ka,text="YOUR TOKEN NO IS"+" "+str(token_no),font="times 25")
    kalab.place(relx=0.48,rely=0.5,anchor="center")
    
    f=open("login.txt","r")
    c=f.read()
    d=c.split()
    e=[]
    for i in d:
        e.append(i.split("-"))
    for i in range(len(e)):
        if e[i][0]==username.get():
            email=e[i][2]
            password=e[i][1]
    c=""
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()

    # Authentication
    s.login("hotel1.tas@gmail.com", "adzj pfqi twvm cnlz")
    
    
    c="Dear"+" "+user+","+"thank you for ordering with us, we are delighted to have you choose our restaurant for your meal today. Your order has been taken and you can come and collect it in 30 mins"
    d="\n"
    d2="\n"
    d1="                                                             ONLY OFFLINE PAYEMNT  IS ACCEPTED                                 "
    
    message=c+d+d2+d1

    # sending the mail
    s.sendmail("hotel1.tas@gmail.com",email, message)

    s.quit()

    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()

    # Authentication
    s.login("hotel1.tas@gmail.com", "adzj pfqi twvm cnlz")
    
    
    c="                                                               SUCCESSFULL ORDER!!                  "
    d="\n"
    d2="\n"
    d1="CUSTOMER NAME:"+" "+user
    if klist==breakfast1:
        d3="SESSION:"+" "+"BREAKFAST"
    if klist==lunch1:
        d3="SESSION:"+" "+"LUNCH"
    if klist==dinner1:
        d3="SESSION:"+" "+"DINNER"
    d4="TOKEN NO:"+" "+str(token_no)
    message=c+d+d2+d1+"\n"+d3+"\n"+d4
    # sending the mail
    s.sendmail("hotel1.tas@gmail.com","srisaiankit2110551@ssn.edu.in", message)

    s.quit()
    
def buttonfunc(var,itemre):
    global itemlist
    itemlist.append([itemre,var.get()])
def edit(user,openw):
    openw.destroy()
    global itemlist
    itemlist=[]
    window=Toplevel(tkWindow)
    window.state("zoomed")
    newbr=Label(window,image=im1)
    newbr.place(x=0,y=0)
    b1=Button(window,image=bpic,command=window.destroy)
    b1.place(relx=0.25,rely=0.9,anchor="center")
    Payment=partial(payment,user)
    Open1=partial(open1,user)
    b2=Button(window,image=pic,command=Open1)
    b2.place(relx=0.6,rely=0.83)
    def breakfast_menu():
     label1=Label(window,text="MENU FOR BREAKFAST",font="times 30 bold")
     label1.place(x=570,y=20)

     labeli=Label(window,text="Item",font="times 22")
     labeli.place(x=190,y=80)

     labelp=Label(window,text="price",font="times 22")
     labelp.place(x=550,y=80)

     labelq=Label(window,text="Qty. Available",font="times 22")
     window.wm_attributes("-transparentcolor","#ab23ff")
     labelq.place(x=800,y=80)

     labelc=Label(window,text="Choose",font="times 22")
     labelc.place(x=1110,y=80)

     for i in range(len(breakfast)):
        li="label"+str(i)
        li=Label(window,text=breakfast[i][0],font="times 18")
        li.place(x=180,y=(30*(1.5*i)+150))
        
        lp="l2"+str(i)
        lp=Label(window,text=breakfast[i][1],font="times 18")
        lp.place(x=540,y=(30*(1.5*i)+150))

        lq="l2"+str(i)
        lq=Label(window,text=breakfast[i][2],font="times 18")
        lq.place(x=800,y=(30*(1.5*i)+150))

        
        itemre=breakfast[i][0]
        lc="l2"+str(i)
        var=StringVar()
        lc=Entry(window,textvariable=var)
        lc.place(x=1100,y=(30*(1.5*i)+150))
        Buttonfunc=partial(buttonfunc,var,itemre)
        button=Button(window,text="Add",command=Buttonfunc)
        button.place(x=1200,y=(30*(1.5*i)+150))
    def lunch_menu():
      label1=Label(window,text="MENU FOR LUNCH",font="times 20 bold")
      label1.place(x=570,y=0)

      labeli=Label(window,text="ITEM",font="times 22")
      labeli.place(x=190,y=80)

      labelp=Label(window,text="PRICE",font="times 22")
      labelp.place(x=550,y=80)

      labelq=Label(window,text="MAX QUANTITY",font="times 22")
      labelq.place(x=800,y=80)

      labelc=Label(window,text="SELECT",font="times 22")
      labelc.place(x=1110,y=80)
      for i in range(len(lunch)):
        li="label"+str(i)
        li=Label(window,text=lunch[i][0],font="times 18",width=10,height=1)
        li.place(x=180,y=(30*(1.5*i)+150))
        
        lp="l2"+str(i)
        lp=Label(window,text=lunch[i][1],font="times 18",width=10,height=1)
        lp.place(x=540,y=(30*(1.5*i)+150))

        lq="l2"+str(i)
        lq=Label(window,text=lunch[i][2],font="times 18",width=10,height=1)
        lq.place(x=800,y=(30*(1.5*i)+150))

        itemre=lunch[i][0]
        lc="l2"+str(i)
        var=StringVar()
        lc=Entry(window,textvariable=var)
        lc.place(x=1100,y=(30*(1.55*i)+150))
        Buttonfunc=partial(buttonfunc,var,itemre)
        button=Button(window,text="Add",command=Buttonfunc)
        button.place(x=1200,y=(30*(1.55*i)+150))
    def dinner_menu():
      label1=Label(window,text="MENU FOR DINNER",font="times 30 bold")
      label1.place(x=500,y=0)

      labeli=Label(window,text="Item",font="times 22")
      labeli.place(x=180,y=80)

      labelp=Label(window,text="price",font="times 22")
      labelp.place(x=540,y=80)

      labelq=Label(window,text="Qty. Available",font="times 22")
      labelq.place(x=810,y=80)

      labelc=Label(window,text="Choose",font="times 22")
      labelc.place(x=1110,y=80)
      for i in range(len(dinner)):
        li="label"+str(i)
        li=Label(window,text=dinner[i][0],font="times 18")
        li.place(x=180,y=(30*(1.5*i)+150))
        
        lp="l2"+str(i)
        lp=Label(window,text=dinner[i][1],font="times 18")
        lp.place(x=540,y=(30*(1.5*i)+150))

        lq="l2"+str(i)
        lq=Label(window,text=dinner[i][2],font="times 18")
        lq.place(x=800,y=(30*(1.5*i)+150))
        
        itemre=dinner[i][0]
        lc="l2"+str(i)
        var=StringVar()
        lc=Entry(window,textvariable=var)
        lc.place(x=1100,y=(30*(1.5*i)+150))
        Buttonfunc=partial(buttonfunc,var,itemre)
        button=Button(window,text="Add",command=Buttonfunc)
        button.place(x=1200,y=(30*(1.5*i)+150))
    now = datetime.datetime.now()
    a=list(now.strftime("%H:%M:%S"))
    b=[]
    c=""
    j=0
    while(j<=len(a)-1):
     if a[j]==":":
        b.append(c)
        c=""
        j=j+1
     else:
        c=c+str(a[j])
        j=j+1
    breakfast1=[7,8,9,10,11]
    lunch1=[12,13,14,15,16,17]
    dinner1=[18,19,20,21,22,23]
    print(b)
    for l in range(len(b)):
     if l==0:
        k=int(b[0])
        if k in breakfast1:
            breakfast_menu()
        if k in lunch1:
            lunch_menu()
        if k in dinner1:
            dinner_menu()
        if k>breakfast1[-1] and k<lunch1[0]:
            window=Toplevel(tkWindow)
            window.title("Menu for today")
            window.state("zoomed")
            lab3=Label(window,image=im1)
            lab3.place(x=0,y=0)
            button=ImageTk.PhotoImage(Image.open("home.png"))
            button=Label(window,image=button,command=window.destroy)
            button.place(relx=0.5,rely=0.75,anchor="center")
            min=int(b[1])/60
            c=lunch1[0]-(k+min)
            newmin=c*60
            if newmin>60:
                hr=newmin//60
                mm=newmin%60
                if hr==1:
                    label1=Label(window,text="There are still"+" "+str(hr)+" "+"hour"+" "+"and"+" "+str(round(mm))+"minutes"+" "+"for lunch,kindly wait",font="times 30 bold")
                    label1.place(x=300,y=0)
                else:
                     label1=Label(window,text="There are still"+" "+str(hr)+" "+"hours"+" "+"and"+" "+str(round(mm))+"minutes"+" "+"for lunch,kindly wait",font="times 30 bold")
                     label1.place(x=300,y=0)
            else:
               label1=Label(window,text="There are still"+" "+str(round(newmin))+" "+"minutes"+" "+"for lunch,kindly wait",font="times 30 bold")
               label1.place(x=300,y=0)

        if k>lunch1[-1] and k<dinner1[0]:
            window=Toplevel(tkWindow)
            window.title("Menu for today")
            window.state("zoomed")
            lab3=Label(window,image=im1)
            lab3.place(x=0,y=0)
            button=ImageTk.PhotoImage(Image.open("home.png"))
            button=Label(window,image=button,command=payment)
            button.place(relx=0.5,rely=0.75,anchor="center")
            min=int(b[1])/60
            c=dinner1[0]-(k+min)
            newmin=c*60
            if newmin>60:
              hr=newmin//60
              mm=newmin%60
              if hr==1:
                label1=Label(window,text="There are still"+" "+str(hr)+" "+"hour"+" "+"and"+" "+str(round(mm))+"minutes"+" "+"for dinner,kindly wait",font="times 30 bold")
                label1.place(x=300,y=0)
              else:
               label1=Label(window,text="There are still"+" "+str(hr)+" "+"hour"+" "+"and"+" "+str(round(mm))+"minutes"+" "+"for dinner,kindly wait",font="times 30 bold")
               label1.place(x=300,y=0)
            else:
                label1=Label(window,text="There are still"+" "+str(round(newmin))+" "+"minutes"+" "+"for dinner,kindly wait",font="times 30 bold")
                label1.place(x=300,y=0)
def Continue(user):
    continue1=Toplevel(tkWindow)
    continue1.state("zoomed")
    continuelabel=Label(continue1,text="ONCE YOU PRESS CONTINUE,YOUR ORDER WILL BE FINALIZED AND NO MORE CHANGES CAN BE MADE TO IT",font="times 20")
    continuelabel.place(relx=0.5,rely=0.5,anchor="center")
    Proceed=partial(proceed,user)
    continuebt=Button(continue1,text="CONTINUE",command=Proceed)
    continuebt.place(relx=0.5,rely=0.75,anchor="center")
def payment(user):
    today=date.today()
    today1=str(today)
    clist=today1.split("-")
    now = datetime.datetime.now()
    a=list(now.strftime("%H:%M:%S"))
    b=[]
    c=""
    j=0
    while(j<=len(a)-1):
     if a[j]==":":
       b.append(c)
       c=""
       j=j+1
     else:
       c=c+str(a[j])
       j=j+1
    clist.extend(b)
    b1=[user,itemlist,str(now.strftime("%H:%M:%S")),clist[2],clist[3]]
    if len(itemlist)>=3:
         f=open("orders.txt","a")
         f.write(str(b1))
         f.write("$")
         f.close()
         f=open("orders.txt","r")
         c=f.read()
         dlist=c.split("$")
         dlist[-1]="flag"
         dlist.remove("flag")
    else:
         f=open("expressorder.txt","a")
         f.write(str(b1))
         f.write("$")
         f.close()
         f=open("expressorder.txt","r")
         c=f.read()
         dlist=c.split("$")
         dlist[-1]="flag"
         dlist.remove("flag")
    blist=[]
    breakfast1=[7,8,9,10,11]
    lunch1=[12,13,14,15,16,17]
    dinner1=[18,19,20,21,22,23]
    if int(b[0]) in breakfast1:
        implist=breakfast1
    if int(b[0]) in lunch1:
        implist=lunch1
    if int(b[0]) in dinner1:
        implist=dinner1
    for i in range(len(dlist)):
        dlist[i]=eval(dlist[i])
    for i in range(len(dlist)):
        if dlist[i][3]==clist[2] and int(dlist[i][4]) in implist:
            blist.append(dlist[i])
    cat=Toplevel(tkWindow)
    cat.state("zoomed")
    imgna=Label(cat,image=look)
    imgna.place(x=0,y=0)
    cartlabel=Label(cat,image=bill)
    cartlabel.place(relx=0.45,rely=0.5,anchor="center")
    Cont=partial(Continue,user)
    proceedlabel=Button(cat,image=proceed1,command=Cont)
    proceedlabel.place(relx=0.92,rely=0.5,anchor="center")
    total=""
    total1=""
    for i in range(len(blist)):
     if user==blist[i][0]:
        for j in range(len(blist[i][1])):
            total=total+blist[i][1][j][0]+"\n"+"\n"
            total1=total1+str(blist[i][1][j][1])+"\n"+"\n"
        newlabel2=Label(cat,text=total,font="times 15")
        newlabel2.place(relx=0.18,rely=0.47,anchor="center")
        nlabel1=Label(cat,text=total1,font="times 15")
        nlabel1.place(relx=0.36,rely=0.47,anchor="center")
    pricetot=" "
    qtytot=" "
    amount=0
    breakfast1=[6,7,8,9,10,11]
    lunch1=[12,13,14,15,16,17]
    dinner1=[18,19,20,21,22,23]
    if int(b[0])>=breakfast1[0] and int(b[0])<=breakfast1[-1]:
        newlist=breakfast
    if int(b[0])>=lunch1[0] and int(b[0])<=lunch1[-1]:
        newlist=lunch
    if int(b[0])>=dinner1[0] and int(b[0])<=dinner1[-1]:
        newlist=dinner
    for i in range(len(blist)):
      if user==blist[i][0]:
        for j in range(len(blist[i][1])):
            for k in range(len(newlist)):
                if blist[i][1][j][0]==newlist[k][0]:
                    pricetot=pricetot+str(newlist[k][1])+"\n"+"\n"
                    qtytot=qtytot+str(int(blist[i][1][j][1])*newlist[k][1])+"\n"+"\n"
                    amount=amount+int(blist[i][1][j][1])*newlist[k][1]
    pricelabel=Label(cat,text=pricetot,font="times 15")
    pricelabel.place(relx=0.57,rely=0.47,anchor="center")
    qtylabel=Label(cat,text=qtytot,font="times 15")
    qtylabel.place(relx=0.77,rely=0.47,anchor="center")
    symbol1=Label(cat,text=str(amount),font="times 15")
    symbol1.place(relx=0.81,rely=0.81,anchor="center")
    symbol2=Label(cat,text=str(0.05*amount),font="times 15")
    symbol2.place(relx=0.81,rely=0.86,anchor="center")
    symbol3=Label(cat,text=str(1.05*amount),font="times 15")
    symbol3.place(relx=0.81,rely=0.91,anchor="center")
def open1(user):
    openw=Toplevel(tkWindow)
    openw.state("zoomed")
    openw.geometry("400x200")
    openlabel=Label(openw,text="ONCE YOU FINALIZE CART, YOU CANNOT MAKE CHANGES!!",font="times 30")
    openlabel.place(relx=0.5,rely=0.3,anchor="center")
    Edit=partial(edit,user,openw)
    button3=Button(openw,text="EDIT/CANCEL CART",command=Edit,height=10,width=20,font="times 10")
    button3.place(relx=0.2,rely=0.6)
    Payment=partial(payment,user)
    button4=Button(openw,text="CONFIRM ORDER",command=Payment,height=10,width=20,font="times 10")
    button4.place(relx=0.8,rely=0.6)
def main(user):
      new=Toplevel(tkWindow)
      new.state("zoomed")
      Menu=partial(menu,user)
      Track_order=partial(track_order,user)
      image1=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\restuarant1.jpg"))
      label3=Label(new,image=image1)
      label3.place(x=0,y=0)
      newlabel=Label(new,image=hotel)
      newlabel.place(relx=0.5,rely=0.13,anchor="center")
      new.title("Welcome to XYZ hotel")
      about=Button(new,text="About us",padx=50,pady=50,command=about_us,image=logo)
      about.place(relx=0.04,rely=0.4,anchor="center")
      menu1=Button(new,command=Menu,image=menl)
      menu1.place(relx=0.5,rely=0.5,anchor="center")
      Order=Button(new,padx=50,pady=50,image=order,command=Track_order)
      Order.place(relx=0.5,rely=0.7,anchor="center")
      new.mainloop()
def menu(user):
    global im
    gl=user
    counti=0
    window=Toplevel(tkWindow)
    window.state("zoomed")
    newbr=Label(window,image=im1)
    newbr.place(x=0,y=0)
    b1=Button(window,image=bpic,command=window.destroy)
    b1.place(relx=0.25,rely=0.9,anchor="center")
    Payment=partial(payment,user)
    Open1=partial(open1,user)
    b2=Button(window,image=pic,command=Open1)
    b2.place(relx=0.6,rely=0.83)
    def breakfast_menu():
     nonlocal gl
     nonlocal counti
     label1=Label(window,text="MENU FOR BREAKFAST",font="times 30 bold")
     label1.place(x=570,y=20)

     labeli=Label(window,text="Item",font="times 22")
     labeli.place(x=190,y=80)

     labelp=Label(window,text="price",font="times 22")
     labelp.place(x=550,y=80)

     labelq=Label(window,text="Qty. Available",font="times 22")
     window.wm_attributes("-transparentcolor","#ab23ff")
     labelq.place(x=800,y=80)

     labelc=Label(window,text="Choose",font="times 22")
     labelc.place(x=1110,y=80)

     for i in range(len(breakfast)):
        li="label"+str(i)
        li=Label(window,text=breakfast[i][0],font="times 18")
        li.place(x=180,y=(30*(1.5*i)+150))
        
        lp="l2"+str(i)
        lp=Label(window,text=breakfast[i][1],font="times 18")
        lp.place(x=540,y=(30*(1.5*i)+150))

        lq="l2"+str(i)
        lq=Label(window,text=breakfast[i][2],font="times 18")
        lq.place(x=800,y=(30*(1.5*i)+150))

        
        itemre=breakfast[i][0]
        lc="l2"+str(i)
        var=StringVar()
        lc=Entry(window,textvariable=var)
        lc.place(x=1100,y=(30*(1.5*i)+150))
        Buttonfunc=partial(buttonfunc,var,itemre)
        button=Button(window,text="Add",command=Buttonfunc)
        button.place(x=1200,y=(30*(1.5*i)+150))
    def lunch_menu():
      nonlocal gl
      nonlocal counti
      label1=Label(window,text="MENU FOR LUNCH",font="times 25 bold")
      label1.place(x=570,y=10)

      labeli=Label(window,text="ITEM",font="times 22")
      labeli.place(x=190,y=80)

      labelp=Label(window,text="PRICE",font="times 22")
      labelp.place(x=550,y=80)

      labelq=Label(window,text="MAX QUANTITY",font="times 22")
      labelq.place(x=800,y=80)

      labelc=Label(window,text="SELECT",font="times 22")
      labelc.place(x=1110,y=80)
      for i in range(len(lunch)):
        li="label"+str(i)
        li=Label(window,text=lunch[i][0],font="times 18",width=10,height=1)
        li.place(x=180,y=(30*(1.5*i)+150))
        
        lp="l2"+str(i)
        lp=Label(window,text=lunch[i][1],font="times 18",width=10,height=1)
        lp.place(x=540,y=(30*(1.5*i)+150))

        lq="l2"+str(i)
        lq=Label(window,text=lunch[i][2],font="times 18",width=10,height=1)
        lq.place(x=800,y=(30*(1.5*i)+150))

        itemre=lunch[i][0]
        lc="l2"+str(i)
        var=StringVar()
        lc=Entry(window,textvariable=var)
        lc.place(x=1100,y=(30*(1.55*i)+150))
        Buttonfunc=partial(buttonfunc,var,itemre)
        button=Button(window,text="Add",command=Buttonfunc)
        button.place(x=1200,y=(30*(1.58*i)+150))
    def dinner_menu():
      nonlocal gl
      label1=Label(window,text="MENU FOR DINNER",font="times 30 bold")
      label1.place(x=500,y=0)

      labeli=Label(window,text="Item",font="times 22")
      labeli.place(x=180,y=80)

      labelp=Label(window,text="price",font="times 22")
      labelp.place(x=540,y=80)

      labelq=Label(window,text="Qty. Available",font="times 22")
      labelq.place(x=810,y=80)

      labelc=Label(window,text="Choose",font="times 22")
      labelc.place(x=1110,y=80)
      for i in range(len(dinner)):
        li="label"+str(i)
        li=Label(window,text=dinner[i][0],font="times 18")
        li.place(x=180,y=(30*(1.5*i)+150))
        
        lp="l2"+str(i)
        lp=Label(window,text=dinner[i][1],font="times 18")
        lp.place(x=540,y=(30*(1.5*i)+150))

        lq="l2"+str(i)
        lq=Label(window,text=dinner[i][2],font="times 18")
        lq.place(x=800,y=(30*(1.5*i)+150))
        
        itemre=dinner[i][0]
        lc="l2"+str(i)
        var=StringVar()
        lc=Entry(window,textvariable=var)
        lc.place(x=1100,y=(30*(1.5*i)+150))
        Buttonfunc=partial(buttonfunc,var,itemre)
        button=Button(window,text="Add",command=Buttonfunc)
        button.place(x=1200,y=(30*(1.5*i)+150))
    breakfast1=[6,7,8,9,10,11]
    lunch1=[12,13,14,15,16,17]
    dinner1=[18,19,20,21,22,23]
    now = datetime.datetime.now()
    a=list(now.strftime("%H:%M:%S"))
    b=[]
    c=""
    j=0
    while(j<=len(a)-1):
     if a[j]==":":
        b.append(c)
        c=""
        j=j+1
     else:
        c=c+str(a[j])
        j=j+1
    print(b)
    for l in range(len(b)):
     if l==0:
        k=int(b[0])
        if k in breakfast1:
            breakfast_menu()
        if k in lunch1:
            lunch_menu()
        if k in dinner1:
            dinner_menu()
        if k>breakfast1[-1] and k<lunch1[0]:
            window=Toplevel(tkWindow)
            window.title("Menu for today")
            window.state("zoomed")
            lab3=Label(window,image=im1)
            lab3.place(x=0,y=0)
            button=ImageTk.PhotoImage(Image.open("home.png"))
            button=Label(window,image=button,command=window.destroy)
            button.place(relx=0.5,rely=0.75,anchor="center")
            min=int(b[1])/60
            c=lunch1[0]-(k+min)
            newmin=c*60
            if newmin>60:
                hr=newmin//60
                mm=newmin%60
                if hr==1:
                    label1=Label(window,text="There are still"+" "+str(hr)+" "+"hour"+" "+"and"+" "+str(round(mm))+"minutes"+" "+"for lunch,kindly wait",font="times 30 bold")
                    label1.place(x=300,y=0)
                else:
                     label1=Label(window,text="There are still"+" "+str(hr)+" "+"hours"+" "+"and"+" "+str(round(mm))+"minutes"+" "+"for lunch,kindly wait",font="times 30 bold")
                     label1.place(x=300,y=0)
            else:
               label1=Label(window,text="There are still"+" "+str(round(newmin))+" "+"minutes"+" "+"for lunch,kindly wait",font="times 30 bold")
               label1.place(x=300,y=0)

        if k>lunch1[-1] and k<dinner1[0]:
            window=Toplevel(tkWindow)
            window.title("Menu for today")
            window.state("zoomed")
            lab3=Label(window,image=im1)
            lab3.place(x=0,y=0)
            button=ImageTk.PhotoImage(Image.open("home.png"))
            button=Label(window,image=button,command=payment)
            button.place(relx=0.5,rely=0.75,anchor="center")
            min=int(b[1])/60
            c=dinner1[0]-(k+min)
            newmin=c*60
            if newmin>60:
              hr=newmin//60
              mm=newmin%60
              if hr==1:
                label1=Label(window,text="There are still"+" "+str(hr)+" "+"hour"+" "+"and"+" "+str(round(mm))+"minutes"+" "+"for dinner,kindly wait",font="times 30 bold")
                label1.place(x=300,y=0)
              else:
               label1=Label(window,text="There are still"+" "+str(hr)+" "+"hour"+" "+"and"+" "+str(round(mm))+"minutes"+" "+"for dinner,kindly wait",font="times 30 bold")
               label1.place(x=300,y=0)
            else:
                label1=Label(window,text="There are still"+" "+str(round(newmin))+" "+"minutes"+" "+"for dinner,kindly wait",font="times 30 bold")
                label1.place(x=300,y=0)
def hotel_f():
    window=Toplevel(tkWindow)
    window.state("zoomed")
    newbr=Label(window,image=im1)
    newbr.place(x=0,y=0)
    def breakfast_menu():
     label1=Label(window,text="MENU FOR BREAKFAST",font="times 30 bold")
     label1.place(x=500,y=0)

     labeli=Label(window,text="Item",font="times 22")
     labeli.place(x=400,y=100)

     labelp=Label(window,text="Price",font="times 22")
     labelp.place(x=900,y=100)

     for i in range(len(breakfast)):
        li="label"+str(i)
        li=Label(window,text=breakfast[i][0],font="times 18")
        li.place(x=400,y=(30*(1.5*i)+150))
        
        lp="l2"+str(i)
        lp=Label(window,text=breakfast[i][1],font="times 18")
        lp.place(x=900,y=(30*(1.5*i)+150))


    def lunch_menu():
      label1=Label(window,text="MENU FOR LUNCH",font="times 30 bold")
      label1.place(x=500,y=0)

      labeli=Label(window,text="ITEM",font="times 22")
      labeli.place(x=400,y=100)

      labelp=Label(window,text="PRICE",font="times 22")
      labelp.place(x=900,y=100)

      for i in range(len(lunch)):
        li="label"+str(i)
        li=Label(window,text=lunch[i][0],font="times 18",width=10,height=1)
        li.place(x=400,y=(30*(1.5*i)+150))
        
        lp="l2"+str(i)
        lp=Label(window,text=lunch[i][1],font="times 18",width=10,height=1)
        lp.place(x=900,y=(30*(1.5*i)+150))


    def dinner_menu():
      label1=Label(window,text="MENU FOR DINNER",font="times 30 bold")
      label1.place(x=500,y=0)

      labeli=Label(window,text="ITEM",font="times 22")
      labeli.place(x=400,y=100)

      labelp=Label(window,text="PRICE",font="times 22")
      labelp.place(x=900,y=100)

      for i in range(len(dinner)):
        li="label"+str(i)
        li=Label(window,text=dinner[i][0],font="times 18")
        li.place(x=400,y=(30*(1.5*i)+150))
        
        lp="l2"+str(i)
        lp=Label(window,text=dinner[i][1],font="times 18")
        lp.place(x=900,y=(30*(1.5*i)+150))

    breakfast1=[6,7,8,9,10,11]
    lunch1=[12,13,14,15,16,17]
    dinner1=[18,19,20,21,22,23]
    now = datetime.datetime.now()
    a=list(now.strftime("%H:%M:%S"))
    b=[]
    c=""
    j=0
    while(j<=len(a)-1):
     if a[j]==":":
        b.append(c)
        c=""
        j=j+1
     else:
        c=c+str(a[j])
        j=j+1
    print(b)
    for l in range(len(b)):
     if l==0:
        k=int(b[0])
        if k in breakfast1:
            breakfast_menu()
        if k in lunch1:
            lunch_menu()
        if k in dinner1:
            dinner_menu()
def table(a,b,datawin):
     breakfast1=[7,8,9,10,11]
     lunch1=[12,13,14,15,16,17]
     dinner1=[18,19,20,21,22,23]
     f=open("orders.txt","r")
     c=f.read()
     dlist=c.split("$")
     dlist[-1]="flag"
     dlist.remove("flag")
     f1=open("expressorder.txt","r")
     c=f1.read()
     wlist=c.split("$")
     wlist[-1]="flag"
     wlist.remove("flag")
     for i in range(len(dlist)):
        dlist[i]=eval(dlist[i])
     for i in range(len(wlist)):
        wlist[i]=eval(wlist[i])
     wlist.extend(dlist)
     biglist=[["S.NO","CUSTOMER NAME","NO OF DISHES","TOTAL BILL AMOUNT"]]
     k1=a.get().split("-")
     if b.get()=="Breakfast":
        count2=0
        for i in range(len(wlist)):
            tot=0
            if int(wlist[i][4]) in breakfast1 and wlist[i][3]==k1[0]:
                count2=count2+1
                for j in range(len(wlist[i][1])):
                    for k in range(len(breakfast)):
                        if wlist[i][1][j][0]==breakfast[k][0]:
                            tot=tot+int(wlist[i][1][j][1])*breakfast[k][1]
                br=[count2,wlist[i][0],len(wlist[i][1]),tot*1.05]
                biglist.append(br)
     if b.get()=="Lunch":
        count2=0
        for i in range(len(wlist)):
            tot=0
            if int(wlist[i][4]) in lunch1 and wlist[i][3]==k1[0]:
                count2+=1
                for j in range(len(wlist[i][1])):
                    for k in range(len(lunch)):
                        if wlist[i][1][j][0]==lunch[k][0]:
                             tot=tot+int(wlist[i][1][j][1])*lunch[k][1]
                br=[count2,wlist[i][0],len(wlist[i][1]),tot*1.05]
                biglist.append(br)
     print(biglist)
     if b.get()=="Dinner":
        count2=0
        for i in range(len(wlist)):
            tot=0
            if int(wlist[i][4]) in dinner1 and wlist[i][3]==k1[0]:
                count2+=1
                for j in range(len(wlist[i][1])):
                    for k in range(len(dinner)):
                        if wlist[i][1][j][0]==dinner[k][0]:
                            tot=tot+int(wlist[i][1][j][1])*dinner[k][1]
                br=[1,wlist[i][0],len(wlist[i][1]),tot*1.05]
                biglist.append(br)
     if len(biglist)==1:
        big=Toplevel(tkWindow)
        big.state("zoomed")
        biglab=Label(big,text="THERE ARENT ANY ORDERS YET FOR THIS SESSION",font="times 25")
        biglab.place(relx=0.5,rely=0.5,anchor="center")
     else:
        def Table_create(root):
         for i in range(total_rows):
            for j in range(total_columns):
                 
                e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                e.grid(row=i, column=j)
                e.insert(END, biglist[i][j])
        total_rows=len(biglist)
        total_columns=len(biglist[0])

        display=Toplevel(tkWindow)
        if b.get()=="Breakfast":
         display.title("MENU FOR BREAKFAST")
        if b.get()=="Lunch":
         display.title("MENU FOR LUNCH")
        if b.get()=="Dinner":
         display.title("MENU FOR FINNER")
        t=Table_create(display)
    

def data():
    datawin=Toplevel(tkWindow)
    datawin.state("zoomed")
    datawin.configure(bg="white")
    dataimg=Label(datawin,image=details)
    dataimg.place(relx=0.20,rely=0.2,anchor="center")
    datalab=Label(datawin,text="ORDER DETAILS",font="times 30")
    datalab.place(relx=0.45,rely=0.2,anchor="center")
    datalabel=Label(datawin,text="Enter date (in DD-MM-YYYY format)",font="times 25")
    datalabel.place(relx=0.27,rely=0.50,anchor="center")
    dateentry=StringVar()
    date=Entry(datawin,textvariable=dateentry)
    date.place(relx=0.5,rely=0.50,anchor="center")
    session=Label(datawin,text="Enter session",font="times 25")
    session.place(relx=0.35,rely=0.65,anchor="center")
    sessionentry=StringVar()
    sessionentry=Entry(datawin,textvariable=sessionentry)
    sessionentry.place(relx=0.5,rely=0.65,anchor="center")
    Table=partial(table,dateentry,sessionentry,datawin)
    ok=Button(datawin,text="OK",command=Table,height= 5, width=10)
    ok.place(relx=0.45,rely=0.80,anchor="center")
def Help():
    helpwin=Toplevel(tkWindow)
    helpwin.state("zoomed")
    label5=Label(helpwin,image=back)
    label5.place(x=0,y=0)
    label6=Label(helpwin,image=help4)
    label6.place(relx=0.55,rely=0.5,anchor="center")
    b3=Button(helpwin,image=home1,command=helpwin.destroy)
    b3.place(relx=0.085,rely=0.5,anchor="center")
    

tkWindow = Tk()
tkWindow.title("HOTEL ASA")
tkWindow.state("zoomed")
image=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\Restaurant.jpg"))
label=Label(tkWindow,image=image)
label.place(x=0,y=0)
logoimage=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\logo.jpg"))
label34=Label(tkWindow,image=logoimage)
label34.place(relx=0.5,rely=0.35,anchor="center")
imag=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\username.jpg"))
pass1=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\pass1.jpg"))
emage=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\emage.jpg"))
im=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\buff.jpg"))
#border=ImageTk.PhotoImage(Image.open("border.png"))
black=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\black.png"))
blacklabel=Label(tkWindow,image=black)
#borderlabel=Label(tkWindow,image=border)
#borderlabel.place(x=0,y=0)
blacklabel.place(relx=0.5,rely=0.1,anchor="center")
proceed1=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\proceed.jpg"))
im1=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\lunch.jpg"))
im45=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\manager.png"))
im2=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\dinner.jpg"))
back=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\About.jpg"))
imagen=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\now.png"))
logo=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\aboutlogo.jpg.png"))
menl=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\menulogo.png"))
order=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\order.png"))
hotel=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\hotel.png"))
cart=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\cart.png"))
look=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\look.jpg"))
bpic=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\home.png"))
pic=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\payment.png"))
asa=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\hotel asa.png"))
passwind=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\passwin.png"))
bill=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\bill.png"))
token=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\token.png"))
fig=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\fig.png"))
details=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\details.png"))
help3=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\help.jpg"))
help4=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\helpus.png"))
home1=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\home1.png"))
def about_us():
    global back
    w=Toplevel(tkWindow)
    w.state("zoomed")
    wlabel=Label(w,image=back)
    wlabel.place(x=0,y=0)
    bimg=Label(w,image=imagen)
    bimg.place(relx=0.5,rely=0.5,anchor="center")
def track_order(username):
    user=username
    ca=Toplevel(tkWindow)
    ca.state("zoomed")
    imgna=Label(ca,image=look)
    imgna.place(x=0,y=0)
    cartlabel=Label(ca,image=cart)
    cartlabel.place(relx=0.5,rely=0.5,anchor="center")
    b4=Button(ca,image=home1,command=ca.destroy)
    b4.place(relx=0.085,rely=0.5,anchor="center")
    tot=""
    tot1=""
    count=0
    today=date.today()
    today1=str(today)
    clist=today1.split("-")
    now = datetime.datetime.now()
    a=list(now.strftime("%H:%M:%S"))
    b=[]
    c=""
    j=0
    while(j<=len(a)-1):
     if a[j]==":":
       b.append(c)
       c=""
       j=j+1
     else:
       c=c+str(a[j])
       j=j+1
    clist.extend(b)
    breakfast1=[7,8,9,10,11]
    lunch1=[12,13,14,15,16,17]
    dinner1=[18,19,20,21,22,23]
    b1=[user,itemlist,clist[2],clist[3]]
    f=open("orders.txt","r")
    c=f.read()
    dlist=c.split("$")
    dlist[-1]="flag"
    dlist.remove("flag")
    blist=[]
    for i in range(len(dlist)):
        dlist[i]=eval(dlist[i])
    print(dlist)
    print(clist)
    for i in range(len(dlist)):
        if int(b[0]) in breakfast1:
            menulist=breakfast1
            if dlist[i][3]==clist[2] and int(dlist[i][4]) in menulist:
                blist.append(dlist[i])
        if int(b[0]) in lunch1:
            menulist=lunch1
            if dlist[i][3]==clist[2] and int(dlist[i][4]) in menulist:
                blist.append(dlist[i])
        if int(b[0]) in dinner1:
            menulist=dinner1
            if dlist[i][3]==clist[2] and int(dlist[i][4]) in menulist:
                blist.append(dlist[i])
    print(blist)
    for i in range(len(blist)):
        if user==blist[i][0]:
            for j in range(len(blist[i][1])):
                tot=tot+blist[i][1][j][0]+"\n"+"\n"
                tot1=tot1+str(blist[i][1][j][1])+"\n"+"\n"
            newlabel=Label(ca,text=tot,font="times 20")
            newlabel.place(relx=0.39,rely=0.47,anchor="center")
            nlabel=Label(ca,text=tot1,font="times 20")
            nlabel.place(relx=0.62,rely=0.47,anchor="center")
        else:
            count=count+1
    if count==len(blist):
        sigma=Label(ca,image=fig)
        sigma.place(relx=0.5,rely=0.5,anchor="center")
def validateLogin(username, password):
  global logo
  user=username.get()
  Menu=partial(menu,user)
  Track_order=partial(track_order,user)
  f=open("login.txt","r")
  c=f.read()
  d=c.split()
  e=[]
  for i in d:
    e.append(i.split("-"))
  count=0
  for i in range(len(e)):
    if e[i][0]==username.get() and e[i][1]==password.get():
      new=Toplevel(tkWindow)
      new.state("zoomed")
      image1=ImageTk.PhotoImage(Image.open("C:\\Users\\ankit\\OneDrive\\Desktop\\Project folder\\restuarant1.jpg"))
      label3=Label(new,image=image1)
      label3.place(x=0,y=0)
      newlabel=Label(new,image=hotel)
      newlabel.place(relx=0.5,rely=0.13,anchor="center")
      new.title("Welcome to XYZ hotel")
      about=Button(new,text="About us",padx=50,pady=50,command=about_us,image=logo)
      about.place(relx=0.04,rely=0.4,anchor="center")
      help1=Button(new,image=help3,command=Help)
      help1.place(relx=0.04,rely=0.55,anchor="center")
      menu1=Button(new,command=Menu,image=menl)
      menu1.place(relx=0.5,rely=0.5,anchor="center")
      Order=Button(new,padx=50,pady=50,image=order,command=Track_order)
      Order.place(relx=0.5,rely=0.7,anchor="center")
      new.mainloop()
    else:
      count=count+1
  if count==len(e):
   loginlab=Toplevel(tkWindow)
   loginlab.geometry=("400z400")
   loginlab.state("zoomed")
   loginlabel=Label(loginlab,text="YOU DONT SEEM TO HAVE REGISTERED WITH US"+"\n"+"KINDLY REGISTER IF YOU HAVENT",font="times 10")
   loginlabel.place(relx=0.5,rely=0.5,anchor="center")
   buttonlab=Button(loginlab,text="OK",padx=3.5,command=loginlab.destroy)
   buttonlab.place(relx=0.5,rely=0.75,anchor="center")
  f.close()
def validate_hotel(username,password):
    f1=open("hotelogin.txt","r")
    c=f1.read()
    d=c.split()
    e=[]
    for i in d:
        e.append(i.split("-"))
    for i in range(len(e)):
        if e[i][0]==username.get() and e[i][1]==password.get():
            hotle=Toplevel(tkWindow)
            hotle.geometry("400x400")
            hotle.configure(bg="white")
            hotle.state("zoomed")
            hotelim=Label(hotle,image=im45)
            hotelim.place(relx=0.5,rely=0.45,anchor="center")
            lab=Label(hotle,text="WELCOME MR."+e[i][0].upper(),font="times 30")
            lab.place(relx=0.5,rely=0.12,anchor="center")
            btnd=Button(hotle,text="View Current Session's menu",command=hotel_f)
            btnd.place(relx=0.4,rely=0.77,anchor="center")
            btnd1=Button(hotle,text="View Order details",command=data)
            btnd1.place(relx=0.6,rely=0.77,anchor="center")
    f1.close()
def validateRegister(username,password,email):
  f=open("login.txt","r")
  c=f.read()
  d=c.split()
  user=username.get()
  if "@gmail.com" not in email.get():
      emaillab=Toplevel(tkWindow)
      emaillab.geometry("410x400")
      label6=Label(emaillab,text="KINDLY ENTER A CORRECT EMAIL ADDRESS",font="times 15")
      label6.place(relx=0.5,rely=0.4,anchor="center")
  else:
      e=[]
      countlog=0
      flag=True
      for i in d:
        e.append(i.split("-"))
      if bool(re.search(r'\d', user))==True or len(password.get())>6:
            userlab1=Toplevel(tkWindow)
            userlab1.geometry("410x400")
            c="                     TROUBLE REGISTERING!!           "
            c1="            PLEASE CHECK FOR THE FOLLOWING           "
            c2="               1. USERNAME SHOULD CONTAIN ONLY ALPHABETS      "
            c3="               2.PASSWORD LENGTH SHOULD NOT EXCEED 6 CHARACTERS  "
            d=c+"\n"+"\n"+c1+"\n"+"\n"+c2+"\n"+c3+"\n"
            label22=Label(userlab1,text=d,font="times 10")
            label22.place(relx=0.5,rely=0.5,anchor="center")
            flag=False
      for i in range(len(e)):
        if username.get()==e[i][0] or password.get()==e[i][1]:
          userlab=Toplevel(tkWindow)
          userlab.geometry("410x400")
          label=Label(userlab,text="Credentials already exists, try a new one",font="times 20")
          label.place(x=40,y=150)
          break
        else:
            countlog=countlog+1
      if countlog==len(e) and flag==True:
          f=open("login.txt","a")
          f.write("\n")
          f.write(username.get())
          f.write("-")
          f.write(password.get())
          f.write("-")
          f.write(email.get())
          f.close()
          wini=Toplevel(tkWindow)
          wini.geometry("200x200")
          winlabel=Label(wini,image=asa)
          winlabel.place(x=0,y=0)
          Main=partial(main,user)
          button2=Button(wini,text="Continue",command=Main)
          button2.place(relx=0.5,rely=0.75,anchor="center")
def forgot_password(username):
    f=open("login.txt","r")
    c=f.read()
    d=c.split()
    e=[]
    for i in d:
        e.append(i.split("-"))
    for i in range(len(e)):
        if e[i][0]==username.get():
            email=e[i][2]
            password=e[i][1]
    c=""
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()

    # Authentication
    s.login("hotel1.tas@gmail.com", "adzj pfqi twvm cnlz")
    
    
    c=c+"Your password is"+" "+str(password)

    # message to be sent
    message=c

    # sending the mail
    s.sendmail("hotel1.tas@gmail.com",email, message)

    s.quit()
    passwin=Toplevel(tkWindow)
    passwin.geometry("325x200")
    passlabel=Label(passwin,image=passwind)
    passlabel.place(x=0,y=0)
    newimg=Button(passwin,text="OK",command=passwin.destroy)
    newimg.place(relx=0.5,rely=0.75,anchor="center")
#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name",font="times 25",image=imag)
usernameLabel.place(relx=0.4,rely=0.55,anchor="center")
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username)
usernameEntry.place(relx=0.565,rely=0.55,anchor="center",height=26,width=200)
#password label and password entry box
passwordLabel = Label(tkWindow,text="Password",font="times 25",image=pass1)
passwordLabel.place(relx=0.4,rely=0.68,anchor="center")
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password,show='*')
passwordEntry.place(relx=0.5,rely=0.66,height=26,width=200)

#email label and email entry box
emaillabel=Label(tkWindow,text="Email(Only for registering)",font="times 25",image=emage)
emaillabel.place(relx=0.29,rely=0.77)
email=StringVar()
emailentry=Entry(tkWindow,textvariable=email)
emailentry.place(relx=0.5,rely=0.795,height=26,width=200)
     
validateLogin = partial(validateLogin,username, password)
#login button
loginButton = Button(tkWindow, text="Customer Login", command=validateLogin)
loginButton.place(relx=0.21,rely=0.92)
validate_Hotel=partial(validate_hotel,username,password)
#hotel login
hotellogin=Button(tkWindow,text="Manager Login",command=validate_Hotel)
hotellogin.place(relx=0.35,rely=0.92)
#register button
validateRegister=partial(validateRegister,username,password,email)
Registerbutton=Button(tkWindow, text="Register",command=validateRegister)
Registerbutton.place(relx=0.50,rely=0.92)
#forgot password button
forgotpassword=partial(forgot_password,username)
Forgotpassword=Button(tkWindow,text="Forgot Password",command=forgotpassword)
Forgotpassword.place(relx=0.65,rely=0.92)
