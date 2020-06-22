from tkinter import *
from tkinter import ttk
from methods import Mytranslator
app= Tk()
app.geometry('350x520')
app.title('Google Translate')
app.resizable(0,0)
app.config(bg='black')
#app.wm_iconbitmap('icon.ico')


def get():
    s=srcLangs.get()
    d=destLangs.get()
    message=sourceText.get(1.0,END)
    translator=Mytranslator()
    text=translator.run(txt=message,src=s,dest=d)
    destText.delete(1.0,END)
    destText.insert(END,text)

appName=Label(app,text='Language Translator',font=('arial',20),bg='black',fg='white',height=2)
appName.pack(side=TOP,fill=BOTH,pady=0)
version=Label(app,text='beta',bg='black',fg='white').place(x=250,y=43)
frame=Frame(app).pack(side=BOTTOM)
sourceText = Text(frame,font=('arial',10),height=13,wrap=WORD)
sourceText.pack(side=TOP,padx=5,pady=5)
transBtn=Button(frame,text='Translate',font=('arial',10,'bold'),fg='white',bg='green',activebackground='green',relief=GROOVE,command=get)
transBtn.pack(side=TOP,pady=15)
langs=Mytranslator().langs
srcLangs=ttk.Combobox(frame,values=langs,width=10)
srcLangs.place(x=30,y=265)
srcLangs.set('english')

destLangs=ttk.Combobox(frame,values=langs,width=10)
destLangs.place(x=240,y=265)
destLangs.set('hindi')


destText = Text(frame,font=('arial',10),height=13,wrap=WORD)
destText.pack(side=TOP,padx=5,pady=5)


append=Label(app,text='Thank You:Sakib Shabir',font=('arial',10),bg='black',fg='white',height=2)
append.pack(side=TOP,fill=BOTH,pady=0)

app.mainloop()
