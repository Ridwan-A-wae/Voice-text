from tkinter import *
from gtts import gTTS

root = Tk()
root.title("แอปสร้างเสียงจากข้อความ")
canvas = Canvas(root,width=400,height=300)
canvas.pack()

def convertToMP3():
    word = text_entry.get()
    language = 'th'
    output = gTTS(text=word,lang=language,slow=False)
    output.save("sound.mp3")



app_header = Label(root,text="แปลงข้อความเป็นเสียง",font=("Arial",20,"bold"))
canvas.create_window(200,100,window=app_header)

text_entry = Entry(root)
canvas.create_window(200,180,window=text_entry)


btn = Button(root,text="แปลงเป็นเสียง",command=convertToMP3)
canvas.create_window(200,230,window=btn)

root.mainloop()