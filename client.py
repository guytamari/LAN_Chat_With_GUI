from tkinter import *
import socket
import threading
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",8267))
class TAMARI:
	def __init__(self):
		self.Window = Tk()
		self.Window.withdraw()
		self.login = Toplevel()
		self.login.title("Login")
		self.login.resizable(width=False,height=False)
		self.login.configure(width=300,height=300)
		self.req_login = Label(self.login,text="Please login to continue",justify=CENTER,font="Hebbo")
		self.req_login.place(relheight=0.15,relx=0.2,rely=0.06)
		self.name_entered = Entry(self.login,font="Hebbo")
		self.name_entered.place(relwidth=0.4,relheight=0.12,relx=0.35,rely=0.2)
		self.name_entered.focus()
		self.namelabel = Label(self.login,text="Name:",font="Hebbo")
		self.namelabel.place(relheight=0.1,relx=0.1,rely=0.2)
		self.button = Button(self.login,text="CONTINUE",font="Hebbo",command=lambda: self.stage_2(self.name_entered.get()))
		self.button.place(relx=0.4,rely=0.55)
		self.Window.mainloop()

	def stage_2(self, name):
		self.login.destroy()
		self.chat_itself(name)
		receveing = threading.Thread(target=self.receive)
		receveing.start()
	def chat_itself(self, name):
		self.name = name
		self.Window.deiconify()
		self.Window.title("Chat")
		self.Window.resizable(width=False,height=False)
		self.Window.configure(width=450,height=550,bg="#395B64")
		self.tophead = Label(self.Window,text=self.name,bg="#2C3333",fg="#F1F1F1",font="Hebbo",pady=5)
		self.tophead.place(relwidth=1)
		self.chatbox = Text(self.Window,width=20,height=3,bg="#E7F6F2",fg="#2C3333",font="Hebbo",padx=5,pady=5)
		self.chatbox.place(relheight=0.745,relwidth=1,rely=0.08)
		self.bottom_screen = Label(self.Window,height=80,bg="#395B64")
		self.bottom_screen.place(relwidth=1,rely=0.825)
		self.msg_to_send = Entry(self.bottom_screen,bg="#E7F6F2",font="Hebbo")
		self.msg_to_send.place(relwidth=0.74,relheight=0.06,rely=0.008,relx=0.011)
		self.msg_to_send.focus()
		self.msg_button = Button(self.bottom_screen,text="Send",font="Hebbo",width=20,bg="#A5C9CA",relief=FLAT,command=lambda: self.butonfunc(self.msg_to_send.get()))
		self.msg_button.place(relx=0.77,rely=0.008,relheight=0.06,relwidth=0.22)
		self.chatbox.config(cursor="arrow")
		scrollbar = Scrollbar(self.chatbox)
		scrollbar.place(relheight=1,relx=0.974)
		scrollbar.config(command=self.chatbox.yview)
		self.chatbox.config(state=DISABLED)

	def butonfunc(self, msg):
		self.msg = msg
		self.chatbox.config(state=DISABLED)
		self.msg_to_send.delete(0, END)
		sending = threading.Thread(target=self.sendingmessege)
		sending.start()
	def sendingmessege(self):
		self.chatbox.config(state=DISABLED)
		while True:
			message = ("{0}: {1}".format(self.name,self.msg))
			client.send(message.encode('utf-8'))
			break
	def receive(self):
		while True:
			message = client.recv(1024).decode('utf-8')
			if message == "What's ur name? ":
				client.send(self.name.encode('utf-8'))
			else:
				self.chatbox.config(state=NORMAL)
				self.chatbox.insert(END,message+"\n\n")
				self.chatbox.config(state=DISABLED)
				self.chatbox.see(END)


TAMARI = TAMARI()
