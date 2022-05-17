import subprocess
from glob import glob
from tkinter import Frame, Tk, Label, Button, Entry, StringVar, IntVar, END, W, E

root = Tk()
root.title("Instalador de certificados")
root.geometry("300x250")

Label(root, text="Nombre del certificado:").grid(row=0, column=0, sticky=W)
frame = Frame(root, bg="white", borderwidth=1, relief="groove")
frame.grid(row=1, column=0, sticky=W)
files = glob("*.crt" and "*.cer")
def install():
    for cert in files:
        subprocess.Popen(["CERTUTIL", "-addstore", "root", cert])
        print("Instalado:", cert)

Button(root, text="Instalar", command=lambda: install()).grid(row=1, column=1, sticky=W)

for file in files:
    Label(frame, text=file, bg="white").grid(row=files.index(file) + 1, column=0, sticky=W)



root.mainloop()