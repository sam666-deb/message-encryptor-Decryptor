from tkinter import *
import base64


root = Tk()

root.geometry('500x500')
root.resizable(0,0)
root.title('Message Encode and Decode')

Label(root,text='Encode / Decode',font='Roboto 20').pack()
Label(root,text='OneStep.com',font='System 10 bold').pack(side=BOTTOM)

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

def Encode(key,message):
    enc = []
    for i in range(len(message)):
        key_c = key[(i%len(key))]
        enc.append(chr((ord(message[i])+ord(key_c))%256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key,message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key(i%len(key))
        dec.append(chr(256 + ord(message[i]) - ord(key_c))%256)
    return ''.join(dec)

def Mode():
    if(mode.get()=='e'):
        Result.set(Encode(private_key.get(),Text.get()))
    elif(mode.get()=='d'):
        Result.set(Decode(private_key.get(),Text.get()))
    else:
        Result.set('Invalid Mode')


def Exit():
    root.destroy()

def Reset():
    Text.set('')
    private_key.set('')
    mode.set('')
    Result.set('')


Label(root,font='Roboto 12', text='Message').place(x=60,y=90)
Entry(root,font='Roboto 10',textvariable=Text,bg='black').place(x=290,y=60)

Label(root,font='Roboto 12', text='Key').place(x=60,y=90)
Entry(root,font='Roboto 10',textvariable=private_key,bg='black').place(x=290,y=60)

Label(root,font='Roboto 12', text='Mode(e-Encode,d-Decode)').place(x=60,y=120)
Entry(root,font='Roboto 10',textvariable=mode,bg='black').place(x=290,y=120)


Entry(root,font='Roboto 10',textvariable=Result,bg='black',width=52).place(x=65,y=150)

Button(root,font='Roboto 10 bold',bd=0, text='Encrypt / Decrypt', padx=10,
        pady=2,bg='LimeGreen',fg='white',command=Mode).place(x=65,y=200)

Button(root,font='Roboto 10 bold',bd=0, text='Reset',width=6, padx=2,
        pady=2,bg='LimeGreen',fg='white',command=Reset).place(x=300,y=200)

Button(root,font='Roboto 10 bold',bd=0, text='Exit', padx=10,
        pady=2,bg='LimeGreen',fg='white',command=Exit).place(x=375,y=200)

root.mainloop()