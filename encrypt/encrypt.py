from tkinter import *
from tkinter import messagebox
import base64

from PIL import ImageTk


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def save_and_encrypt_notes():


    title=title_entry.get()
    message=input_text.get("1.0",END)
    master_secret=master_secret_entry.get()

    if len(title)==0 or len(message)==0 or len(master_secret)==0:
        messagebox.showinfo(title="ERROR",message="Please Enter All Info")
    else:
        #encryption
        message_encrypted=encode(master_secret, message)
        try :
            with open("encrypted.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        except FileNotFoundError:
            with open("encrypted.txt","w") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")

        finally:
            title_entry.delete(0,END)
            master_secret_entry.delete(0,END)
            input_text.delete("1.0",END)

def decrypt_notes():
    message_encrypted=input_text.get("1.0",END)
    master_secret=master_secret_entry.get()

    if len(message_encrypted)==0 or len(master_secret)==0:
        messagebox.showinfo(title="ERROR !",message="Please Enter All Info")
    else:
        try:
            decrypted_message=decode(master_secret, message_encrypted)
            input_text.delete("1.0",END)
            input_text.insert("1.0",decrypted_message)
        except:
            messagebox.showinfo(title="Error!",message="Please Enter excrypted text")



#UI

window=Tk()
window.title("Secret Notes")
window.config(padx=30,pady=30)


photo=PhotoImage(file="Screenshot_3.png")
photo_label=Label(image=photo)
photo_label.pack()


title_info_label=Label(window,text="Enter your title")
title_info_label.pack()

title_entry=Entry(width=30)
title_entry.pack()

input_info_label=Label(window,text="Enter your secret")
input_info_label.pack()

input_text=Text(width=30,height=10)
input_text.pack()

master_secret_label=Label(window,text="Enter Master Key")
master_secret_label.pack()

master_secret_entry=Entry(width=30)
master_secret_entry.pack()

save_button=Button(window,text="Save & Encyrpt",command=save_and_encrypt_notes)
save_button.pack()

decyrpt_button=Button(window,text="Decrypt",command=decrypt_notes)
decyrpt_button.pack()

window.mainloop()
