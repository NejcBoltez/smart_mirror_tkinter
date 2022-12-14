import subprocess
import os
from face_recognize import User_auth_GUI
from speech_listen import Listening
from working_with_files import Work_with_files
import tkinter as tk
from tkinter import *
from tkinter import ttk

class new_user_GUI():
	def main(self, tabcontrol):
		self.Frame=Frame(self, background="black")
		self.Frame.pack(fill=BOTH, expand= TRUE)
		users_c=check_for_users(self)
		
		create_new_user_tab = ttk.Frame(tabcontrol)
		tabcontrol.add(self.Frame, text ="CREATING NEW USER")
		tabcontrol.select(len(tabcontrol.tabs())-1)
		if (users_c < 0):
			self.auth_label=Label(self.Frame, font=("Helvetica", 30), fg="white", bg="black", text="")
			self.auth_label.pack(side=TOP,fill=BOTH, expand= TRUE)
			self.say_new_user_name=Label(self.Frame, font=("Helvetica", 30), fg="white", bg="black", text="")
			self.say_new_user_name.pack(fill=BOTH, expand= TRUE)
			self.get_new_user_name=Label(self.Frame, font=("Helvetica", 30), fg="white", bg="black", text="")
			self.get_new_user_name.pack(fill=BOTH, expand= TRUE)
			self.update()
			new_user_create(self, tabcontrol)
		else:
			self.auth_frame=Frame(self.Frame, background="Black")
			self.auth_frame.pack(fill=BOTH, expand= TRUE)
			get_user=User_auth_GUI.main(self.auth_frame)
			self.auth_frame.pack_forget()
			self.auth_label=Label(self.Frame, font=("Helvetica", 30), fg="white", bg="black", text="User authontication")
			self.auth_label.pack(side=TOP,fill=BOTH, expand= TRUE)
			self.say_new_user_name=Label(self.Frame, font=("Helvetica", 30), fg="white", bg="black", text="")
			self.say_new_user_name.pack(fill=BOTH, expand= TRUE)
			self.get_new_user_name=Label(self.Frame, font=("Helvetica", 30), fg="white", bg="black", text="")
			self.get_new_user_name.pack(fill=BOTH, expand= TRUE)
			self.update()
			if (len(get_user)>0):
				new_user_create(self, tabcontrol)

def check_for_users(self):
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	users_dir=os.path.join(BASE_DIR, "../Users")
	path, dirs, files = next(os.walk(users_dir))
	count_users= len(dirs)
	return count_users
	
def new_user_create(self,tabcontrol):
	self.auth_label.config(text="Plase say your name without spaces")
	self.update()
	while (True):
		new_user=Listening.listening_function()
		if (new_user is not None or new_user != ""):
			self.say_new_user_name.config(text="Your new name would be " + new_user.replace(" ","") + ". IS THAT OK?")
			self.update()
			user_ok=Listening.listening_function()
			if ("yes" in user_ok.lower()):
				Work_with_files.create_dir_for_user(new_user.replace(" ",""))
				subprocess.Popen(["python3","take_picture.py", new_user.replace(" ","")])
				break
			elif ("yes" not in user_ok.lower()):
				#print("USER_OK: "+user_ok)
				self.auth_label.config(text="Plase say your name again without spaces")
				self.say_new_user_name.config(text="")
				self.update()
			else:
				continue
	tabcontrol.forget(len(tabcontrol.tabs())-1)
#new_user_name()
#new_user_GUI()
