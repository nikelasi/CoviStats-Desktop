import tkinter as tk
from config.colours import BG_COLOR
from ui.groups import AppTitleBar, AppGlobalSidebar, AppCountrySearchGroup, CountryDetailsGroup
from config.paths import icon_route

class Application(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.iconbitmap(self, icon_route)
		tk.Tk.wm_title(self, "CoviStats")

		self.minsize(1000, 620)
		self.main_frame = tk.Frame(self)
		self.main_frame.pack(side="left", expand=True, fill="both")
		self.titlebar = AppTitleBar(self.main_frame)
		self.content_frame = tk.Frame(self.main_frame, bg=BG_COLOR)
		self.content_frame.pack(fill="both", expand=True)
		self.global_sidebar = AppGlobalSidebar(self)
		self.country_search = AppCountrySearchGroup(self)
		self.country_details = None

	def show_country_details(self, country_name):
		if self.country_details is None:
			self.country_details = CountryDetailsGroup(self, country_name)
		else:
			self.hide_country_details()
			self.show_country_details(country_name)


	def hide_country_details(self):
		self.country_details.pack_forget()
		self.country_details.destroy()
		self.country_details = None

import utils.loader
utils.loader.ResourceLoader()
app = Application()
app.mainloop()
app.quit()