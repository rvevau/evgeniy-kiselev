import PIL
from PIL import Image
from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.title("SimpComp")
root.configure(background='gainsboro')
root.geometry('235x50')
root.resizable(width=False, height=False)

text = "Thank you for using SimpComp!\n File will lose quality and weight"

label = Label(root, font=('Helvetica', 15), background="gainsboro", foreground="gray30")
label.config(text=text)
label.pack()

file_path = askopenfilename()
lenFP = len(file_path)

if lenFP > 0:
    img = PIL.Image.open(file_path)

    height, width = img.size

    img = img.resize((height, width), PIL.Image.ANTIALIAS)
    new_file = asksaveasfilename()
    img.save(new_file + " (SimpComp).png")
else:
    root.quit()
