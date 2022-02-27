import tkinter
from tkinter import *

root = Tk()
root.title("Faculté des sciences et technique-SmartBot")
root.geometry("1000x707+50+50")
root.resizable(width=FALSE, height=FALSE)
root.configure(background='#fff')

		#Chatbot

principale=Label(root,text="SmartBot",fg='#fff',bg="#15a6f0",
	font=("ubuntu 60 bold"))


#Create Chat window
ChatBox = Text(root, bg="#fff", height="8", width="50", font="Arial")

ChatBox.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(root, command=ChatBox.yview, cursor="heart")
ChatBox['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(root, font=("Verdana",14,'bold'), text="Envoyer", width="8", height=4,
                  bg="#15a6f0", activebackground="#347d9f",fg='#fff',relief='flat')

#Create the box to enter message
EntryBox = Text(root, bg="#fff",width="29", height="5", font="Arial",relief='flat')
#EntryBox.bind("<Return>", send)


#Place all components on the screen
principale.place(x=0,y=0,width=1000,height=100)
scrollbar.place(x=980,y=102, height=531)
ChatBox.place(x=5,y=102, height=531, width=975)
EntryBox.place(x=5, y=639, height=60, width=840)
SendButton.place(x=852, y=639, height=60,width=140)

root.mainloop()
