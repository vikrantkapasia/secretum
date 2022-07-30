from tkinter import *
import base64
from tkinter import messagebox
import tkinter.font as font
from PIL import Image, ImageTk

def encode(key, msg):
  enc = []
  for i in range(len(msg)):
    list_key = key[i % len(key)]
    list_enc = chr((ord(msg[i]) +
             ord(list_key)) % 256)
    enc.append(list_enc)
  return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, code):
  dec = []
  enc = base64.urlsafe_b64decode(code).decode()
  for i in range(len(enc)):
   list_key = key[i % len(key)]
   list_dec = chr((256 + ord(enc[i]) - ord(list_key)) % 256)

  dec.append(list_dec)
  return "".join(dec)

wn = Tk()
canv = Canvas(master=wn)
canv.place(x=0,y=0,width=1920,height=1080)
img = ImageTk.PhotoImage(Image.open('D:\Project\VIkrant\img.jpg',mode='r'))
canv.create_image(0,0,image=img,anchor='nw')
# wn.geometry("1920x1080")
# wn.configure(bg='azure2')
wn.title("Welcome to Secretum Network!")

Message = StringVar()
key = StringVar()
mode = IntVar()
Output = StringVar()

headingFrame1 = Frame(wn,bg="cyan",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.7,relheight=0.16)

headingLabel = Label(headingFrame1, text=" Welcome to Encryption and Decryption with \n SECRETUM ", fg='grey19', font=('Courier',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


label1 = Label(wn, text='Enter Your Message', font=('Courier',15,'bold'),bg="azure2")
label1.place(x=550,y=250)

msg = Entry(wn,textvariable=Message, width=55, font=('calibre',10,'normal'))
msg.place(x=800,y=260)

label2 = Label(wn, text='Enter Key', font=('Courier',15,'bold'),bg="azure2")
label2.place(x=550,y=300)

InpKey = Entry(wn, textvariable=key, width=55,font=('calibre',10,'normal'))
InpKey.place(x=800,y=310)

label3 = Label(wn, text='What you want to do?', font=('Courier',15,'bold'),bg="azure2")
label3.place(x=550,y=365)

Radiobutton(wn, text='Encrypt', variable=mode, value=1,bg="azure2", font=('Courier',15,'bold')).place(x=800,y=400)
Radiobutton(wn, text='Decrypt', variable=mode, value=2,bg="azure2", font=('Courier',15,'bold')).place(x=950,y=400)

label3 = Label(wn, text='Resulted Message', font=('Courier',15,'bold'), bg="azure2")
label3.place(x=550,y=480)

res = Entry(wn,textvariable=Output, width=55, font=('calibre',10,'normal'))
res.place(x=800,y=490)

#Function that executes on clicking Show Message function in python message encryption decryption project
def Result():
  msg = Message.get()
  k= key.get()
  i = mode.get()
  if (i==1):
    Output.set(encode(k, msg))
  elif(i==2):
    Output.set(decode(k, msg))
  else:
    messagebox.showinfo('Notice From Secretum', 'Either you did not enter the message or key or \nyou did not select the operation. Try again.')

#Function that executes on clicking Reset function
def Reset():
  Message.set("")
  key.set("")
  mode.set(0)
  Output.set("")


ShowBtn = Button(wn,text="Show Message",bg='lavender blush2', fg='black',width=15,height=1,command=Result)
ShowBtn['font'] = font.Font( size=15,weight="bold")
ShowBtn.place(x=740,y=550)

ResetBtn = Button(wn, text='Reset', bg='honeydew2', fg='black', width=15,height=1,command=Reset)
ResetBtn['font'] = font.Font( size=15,weight="bold")
ResetBtn.place(x=740,y=600)

QuitBtn = Button(wn, text='Exit', bg='old lace', fg='black',width=15,height=1, command=wn.destroy)
QuitBtn['font'] = font.Font( size=15,weight="bold")
QuitBtn.place(x=740,y=650)


# wn.mainloop()
mainloop()

