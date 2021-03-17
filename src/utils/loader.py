import os, pyglet
import tkinter as tk
from tkinter import ttk
from config.paths import *
from config.fonts import TITLE_FONT, LOADING_FONT
from config.colours import BG_COLOR, LIGHT_RED, DARK_RED, TXT_COLOR

def passfunc():
	pass

class ResourceLoader(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.title("CoviStats Initialiser")
		self['bg'] = BG_COLOR
		try: self.iconbitmap(icon_route)
		except: pass
		self.geometry(f"400x220+0+10")
		self.resizable(False, False)
		self.protocol('WM_DELETE_WINDOW', passfunc)

		frame = tk.Frame(self, bg=BG_COLOR)
		frame.place(relx=.5, rely=.5, anchor="center")

		tk.Label(frame, text="CoviStats", font=TITLE_FONT, fg=DARK_RED, bg=LIGHT_RED).pack(pady=5, fill="both")

		self.progress_label = tk.Label(frame, text="loading.............", font=LOADING_FONT, fg=TXT_COLOR, bg=BG_COLOR)
		self.progress_label.pack(pady=5)

		self.progressbar = ttk.Progressbar(frame, orient="horizontal", mode="determinate", maximum=100, value=0)
		self.progressbar.pack(expand=True)

		self.procedures = [
			(ResourceTasks.set_paths, "setting up file routes"),
			(ResourceTasks.font_setup, "setting up font file")
		]
		self.number_of_procedures = len(self.procedures) + len(assets)

		self.after(100, self.load_resources)

		self.mainloop()

	def load_resource_with(self, function, info):
		self.progress_label.config(text=f"Task {self.progressbar['value']+1} of {self.number_of_procedures}:\n{info}...")
		try:
			function()
			self.progressbar['value'] += 1
			self.update()
		except:
			pass

	def load_resources(self):
		self.progressbar['value'] = 0
		self.progressbar['maximum'] = self.number_of_procedures

		for procedure in self.procedures:
			self.load_resource_with(procedure[0], procedure[1])

		for asset in assets:
			filename = asset[0].split('\\')[1]
			self.load_resource_with(lambda: ResourceTasks.assets_setup(asset), f"loading {filename}")

		self.quit()
		self.destroy()

class ResourceTasks:

	@staticmethod
	def set_paths():
		for path in paths:
			if path == ".": path = base_route
			else: path = os.path.join(base_route, path)

			if not os.path.exists(path):
				os.makedirs(path)

	@staticmethod
	def assets_setup(asset):
		file_route, data = asset
		route = file_route
		if not os.path.exists(route):
			with open(route, "wb") as file:
				file.write(data)
		else:
			with open(route, "rb") as file:
				local_data = file.read()
			if local_data != data:
				with open(route, "wb") as file:
					file.write(data)

	@staticmethod
	def font_setup():
		if not os.path.exists(font_route):
			with open(font_route, 'wb') as font_file:
				font_file.write(font_ttf)
		else:
			with open(font_route, 'rb') as font_file:
				local_data = font_file.read()
			if local_data != font_ttf:
				with open(font_route, 'wb') as font_file:
					font_file.write(font_ttf)

		pyglet.font.add_file(font_route)
	
