from working_with_files import Work_with_files
from speech_listen import Speaking
from news import display_news
from wikipedia_window import Wikipedia_show
from youtube import yt_search
from youtube_stream import Video
from weather import weather_GUI
from create_new_user import new_user_GUI
import asyncio
import threading

		
class Do_for_command:
	def __call__(args):
			try: 
				print("dummy call")
			except:
				print("")
	def main(self, command, show_news, tabcontrol):

		numbers_int=["1","2","3","4","5","6","7","8","9","10"]
		numbers_string=["one","two","three","four","five","six","seven","eight","nine","ten"]
		position=["first", "second","thirth","fourth","fifth","sixth","seventh","eighth","nineth","tenth"]
		command=command.lower()
		command_search=""
		if (" for " in command):
			command_search=command.split(" for ")[1]
		if (command!=""):
			if("forecast" in command or "weather" in command):
				if (command_search==""):
					command_search="today"
					forecast_task=weather_GUI.main(self, command_search, tabcontrol)
					
				else:
					forecast_task=weather_GUI.main(self, command_search, tabcontrol)
					
			elif (("who" in command or "was" in command or "what" in command  or ("search" in command and "youtube" not in command)) and ("date" not in command)):
				wiki_command=""
				if ("who" in command):
					wiki_command=command.split("who was ")[1]
				elif ("what" in command):
					wiki_command=command.split("what is ")[1]
				elif ("was" in command):
					wiki_command=command.split("was ")
				elif ("for" in command):
					wiki_command=command_search
				wiki_task=Wikipedia_show.main(self, wiki_command.replace(" ","_"), tabcontrol)
				

			elif ("youtube" in command and ("play" not in command or "for" in command)):
				if ("for" in command):
					yt_task=yt_search.main(self, command_search, tabcontrol)

			elif ("new user" in command):
				calib_task = new_user_GUI.main(self, tabcontrol)

			elif ("news" in command):
				news_task=display_news.main(self, show_news, tabcontrol)
			
			elif ("home" in command):
				for t in tabcontrol.tabs():
					if (len(tabcontrol.tabs())>1):
						tabcontrol.forget(len(tabcontrol.tabs())-1)

			elif ("exit" in command):
				for t in tabcontrol.tabs():
					if (len(tabcontrol.tabs())>0):
						tabcontrol.forget(len(tabcontrol.tabs())-1)
			
			elif ("close" in command):
				tabcontrol.forget(len(tabcontrol.tabs())-1)
				try:
					last_tab=str(tabcontrol.tab(len(tabcontrol.tabs())-1, "text"))
					if (last_tab!="PLAYING YOUTUBE VIDEO"):
						self.player.stop()
						self.player=None
				except Exception as e: 
					print(e)

			elif ("next" in command):
					news_next_task=display_news.main(self, show_news, tabcontrol)
					last_tab=str(tabcontrol.tab(len(tabcontrol.tabs())-1, "text"))
					if (last_tab=="NEWS"):
						tabcontrol.forget(len(tabcontrol.tabs())-2)
						
			elif ("resum" in command):
				try:
					last_tab=str(tabcontrol.tab(len(tabcontrol.tabs())-1, "text"))
					if (last_tab=="PLAYING YOUTUBE VIDEO"):
						self.player.set_pause(0)
				except Exception as e: 
					print(e)
			
			elif ("play" in command or "video" in command):
				get_position=0
				for i in range(0,9):
					if (numbers_int[i] in command or numbers_string[i] in command or position[i] in command):
						if ("10" in command):
							get_position=9
							break 
						get_position=i
				#print(get_position)

				yt_stream_task=Video.main(self, get_position, tabcontrol)