from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime 
import tkinter.messagebox as tmb

def every_60(text):
    final_text = ""
    for i in  range(0,len(text)):
        final_text +=text[i]
        if i%60==0 and i!=0:
            final_text +="\n"
    return final_text 

def button_pressed():
    print("Submitting Form!")
    print(f"{namevalue.get(), phonevalue.get()}")
    Label(root,text="Succesfully Subscribed!,Thanks You for Supporting",fg="blue",bg="grey").pack()
    

    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get()}\n")          

root = Tk()
root.title("Cricketer News")
root.geometry("800x900")

texts= []
photos= []
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text =  f.read()
        texts.append(every_60(text))
    image = Image.open(f"{i+1}.jpeg")

    #TODO:resize the image
    image=image.resize((180,180),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))   

f1 = Frame(root,width=550,height=80)
Label(f1,text="Cricketer",font="lucida 30 bold", padx=10, pady=10,bg="white").pack()
Label(f1,text=f"Date : {datetime.now().date()}",font="lucida 10 italic").pack()
f1.pack()

f2 =  Frame(root,width=900,height=200)
Label(f2,text=texts[0],font="lucida 12 italic",padx=15,pady=20,bg="white",).pack(side ="left")
Label(f2,image=photos[0],anchor="e").pack()
f2.pack(anchor="w")

f3 =  Frame(root,width=900,height=200)
Label(f3,text=texts[1],font="lucida 12 italic",padx=15,pady=20,bg="white").pack(side="right")
Label(f3,image=photos[1],anchor="e").pack(side="left")
f3.pack(anchor="w")

f4 =  Frame(root,width=900,height=200)
Label(f4,text=texts[2],font="lucida 12 italic",padx=15,pady=20,bg="white").pack(side="left")
Label(f4,image=photos[2],anchor="e").pack()
f4.pack(anchor="w")

f5=Frame(root,width=100,height=100)
f6=Frame(root,width=100,height=100)
Label(root, text="Please Support and Subscribe",fg="white",bg="black").pack()
f5.pack()
f6.pack()

name = Label(f5, text = "Name").pack(side="left")
phone = Label(f6, text = "Phone").pack(side="left")

namevalue = StringVar()
phonevalue = StringVar()

nameentry = Entry(f5, textvariable = namevalue).pack(side="right")
phoneentry = Entry(f6, textvariable = phonevalue).pack(side="right")

Button(text = "Subscribe", command = button_pressed ,fg="grey",bg="black").pack()

def numbers():
    tmb.showinfo("Succesfull.","Thank you for submitting!")

def rateUs():
    a = tmb.askokcancel("Rate", "Are you willing To Rate?")
    print(a)
    if a==True:
        tmb.showinfo("Rated", "Thanks for rating us .")
    else:
        tmb.showinfo("Not Rated", "We are looking forward for your drawback!.\n Thanks!")

def help():
    tmb.showinfo("Help","We are glad to help You.\n We will soon solve your mess.\nKindly wait for a minute.\nThank You")

    
mycontextbar = Menu(root)

m1 = Menu(mycontextbar, tearoff=0)
m1.add_command(label='Rate Us', command=rateUs)
m1.add_command(label='Help', command=help)

mycontextbar.add_cascade(label='Menu', menu=m1)
mycontextbar.add_command(label='Exit', command=quit)
root.config(menu=mycontextbar)

myslider = Scale(root, from_ = 0, to = 5, orient = HORIZONTAL)
Label(root,text="RATE US!").pack()
myslider.pack()
myslider.set(3)
Button(root, text="success",command= numbers).pack()

root.mainloop()