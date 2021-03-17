import tkinter as tk
from config.colours import LIGHT_RED, DARK_RED, GLOBAL_SIDEBAR_BG, HEADING_COLOR, BG_COLOR, COUNTRY_SEARCH_BG, COUNTRYBOX_BG_COLOR, COUNTRIES_TEXT_COLOR, COUNTRIES_DETAILS_BG
from config.fonts import TITLE_FONT, HEADING_FONT, SEARCHBAR_FONT, COUNTRY_NOT_FOUND_FONT
from config.paths import titlebar_icon_route, global_heading_image_route, icon_route, searchbar_icon_route, ascending_cases_icon_route, descending_cases_icon_route, a_to_z_alphabetical_icon_route, z_to_a_alphabetical_icon_route, x_icon_route
from ui.standard import ImageLabel, StatLabel, CountrySearch, ScrollableFrame, ImageButton
from utils.data_manager import DataManager
import threading
REFRESH_TIME = 5*60*1000

class AppTitleBar(tk.Frame):
	def __init__(self, app, *args, **kwargs):
		tk.Frame.__init__(self, app, *args, **kwargs)
		self['bg'] = LIGHT_RED
		self.pack(fill="both")
		tk.Label(self, text="CoviStats", font=TITLE_FONT, bg=LIGHT_RED, fg=DARK_RED).pack(side="left", padx=(10,3))
		ImageLabel(self, image=tk.PhotoImage(file=titlebar_icon_route), bg=LIGHT_RED).pack(side="left")

class AppGlobalSidebar(tk.Frame):

	def __init__(self, app, *args, **kwargs):
		tk.Frame.__init__(self, app.content_frame, *args, **kwargs)
		self['bg'] = GLOBAL_SIDEBAR_BG
		self.grid(row=0, column=0, rowspan=2, sticky="nws", ipadx=10)
		app.content_frame.grid_rowconfigure(1, weight=1)

		#heading group
		global_heading_frame = tk.Frame(self, bg=GLOBAL_SIDEBAR_BG)
		global_heading_frame.pack()
		tk.Label(global_heading_frame, text="Global", font=HEADING_FONT, fg=HEADING_COLOR, bg=GLOBAL_SIDEBAR_BG).pack(side="left", padx=(0,5))
		ImageLabel(global_heading_frame, image=tk.PhotoImage(file=global_heading_image_route), bg=GLOBAL_SIDEBAR_BG).pack(side="left")

		#stats group
		global_data = DataManager.get_global_data()
		self.stat_groups = [
			StatLabel(self, global_data.cases, "cases"),
			StatLabel(self, global_data.active, "active"),
			StatLabel(self, global_data.recoveries, "recoveries"),
			StatLabel(self, global_data.deaths, "deaths")
		]

		self.after(REFRESH_TIME, self.update)

	def update(self):
		global_data = DataManager.get_global_data()
		self.stat_groups[0].update(global_data.cases)
		self.stat_groups[1].update(global_data.active)
		self.stat_groups[2].update(global_data.recoveries)
		self.stat_groups[3].update(global_data.deaths)
		self.after(REFRESH_TIME, self.update)

class AppCountrySearchGroup(tk.Frame):
	def __init__(self, app, *args, **kwargs):
		tk.Frame.__init__(self, app.content_frame, *args, **kwargs)
		self.app = app
		self['bg'] = COUNTRY_SEARCH_BG
		self.grid(row=0, column=1, sticky="nesw", ipadx=10)
		app.content_frame.grid_columnconfigure(1, weight=2)
		app.content_frame.grid_rowconfigure(0, weight=2)
		self.selected_sort = (lambda k: k.name, False)

		#heading group
		heading_frame = tk.Frame(self, bg=BG_COLOR)
		heading_frame.pack()
		tk.Label(heading_frame, text="Countries", justify="left", anchor="w", font=HEADING_FONT, fg=HEADING_COLOR, bg=BG_COLOR).pack(padx=(7, 0), side="left", anchor="w")
		
		#searchbar + countrybox
		self.searchbar_frame = tk.Frame(self, bg=BG_COLOR)
		self.searchbar_frame.pack(fill="x")
		ImageLabel(self.searchbar_frame, image=tk.PhotoImage(file=searchbar_icon_route), bg=BG_COLOR).pack(side="left", padx=(12, 5))

		self.search_term = tk.StringVar()
		self.search_term.trace_add('write', self.search_callback)

		self.searchbar = CountrySearch(self.searchbar_frame, font=SEARCHBAR_FONT, textvariable=self.search_term)
		self.searchbar.pack(expand=True, fill="x", padx=(5, 12))

		countries_box_frame = tk.Frame(self)
		countries_box_frame.pack(fill="both", expand=1, padx=12, pady=12)
		self.countries_box = ScrollableFrame(countries_box_frame)

		#load countries
		self.update_data()

		#sort buttons
		sort_buttons_frame = tk.Frame(heading_frame, bg=BG_COLOR)
		sort_buttons_frame.pack(side="right", padx=(15, 7), anchor="e")

		ascending_cases_sort = ImageButton(sort_buttons_frame, bg=BG_COLOR, image=tk.PhotoImage(file=ascending_cases_icon_route), command=lambda: self.sort_data("cases", False))
		ascending_cases_sort.pack(side="left", padx=3)

		descending_cases_sort = ImageButton(sort_buttons_frame, bg=BG_COLOR, image=tk.PhotoImage(file=descending_cases_icon_route), command=lambda: self.sort_data("cases", True))
		descending_cases_sort.pack(side="left", padx=3)

		a_to_z_name_sort = ImageButton(sort_buttons_frame, bg=BG_COLOR, image=tk.PhotoImage(file=a_to_z_alphabetical_icon_route), command=lambda: self.sort_data("name", False))
		a_to_z_name_sort.pack(side="left", padx=3)

		z_to_a_name_sort = ImageButton(sort_buttons_frame, bg=BG_COLOR, image=tk.PhotoImage(file=z_to_a_alphabetical_icon_route), command=lambda: self.sort_data("name", True))
		z_to_a_name_sort.pack(side="left", padx=3)

	def update_data(self):
		self.countries_data = DataManager.get_countries_data(self.countries_box.scrollable_frame, self.app)
		key, reverse = self.selected_sort
		self.countries_data.sort(key=key, reverse=reverse)
		text = self.search_term.get()
		text = "" if text == " " else text
		self.update_country_box(text)
		self.after(REFRESH_TIME, self.update_data)

	def search_callback(self, _, __, ___):
		text = self.search_term.get()
		if self.search_term.get() == " ": self.search_term.set("")
		else: self.update_country_box(text)

	def update_country_box(self, text, thread=False):
		try:
			self.countries_box._reset()
			if text == "Search": text = ""
			countries = list(filter(lambda c: text.lower() in c.name.lower(), self.countries_data))
			for country in countries:
				if thread:
					t = threading.Thread(target=lambda: country.frame.pack(anchor="w", fill="x", expand=True))
					t.setDaemon(True)
					t.start()
				else: country.frame.pack(anchor="w", fill="x", expand=True)
			if len(countries) == 0:
				tk.Label(self.countries_box.scrollable_frame, bg=COUNTRYBOX_BG_COLOR, fg=COUNTRIES_TEXT_COLOR, font=COUNTRY_NOT_FOUND_FONT, text=f"no countries with \"{text}\" found").pack(anchor="w", fill="x", expand=True)

		except AttributeError: pass

	def sort_data(self, key, reverse):
		text = self.search_term.get()
		sorting_key = {
			"cases": lambda k: k.cases,
			"name": lambda k: k.name
		}.get(key)
		self.selected_sort = (sorting_key, reverse)
		self.countries_data.sort(key=sorting_key, reverse=reverse)
		self.update_country_box(text)

class CountryDetailsGroup(tk.Frame):
	def __init__(self, app, country_name, *args, **kwargs):
		tk.Frame.__init__(self, app, *args, **kwargs)
		self.country_name = country_name
		self['bg'] = COUNTRIES_DETAILS_BG
		self.pack(side="left", expand=True, fill="both")

		#heading group
		parent_frame = tk.Frame(self, bg=COUNTRIES_DETAILS_BG)
		heading_frame = tk.Frame(parent_frame, bg=COUNTRIES_DETAILS_BG)
		heading_frame.pack()
		close_button = ImageButton(heading_frame, bg=COUNTRIES_DETAILS_BG, image=tk.PhotoImage(file=x_icon_route), command=lambda: app.hide_country_details())
		close_button.pack(side="left", padx=8)
		tk.Label(heading_frame, text=self.country_name, font=HEADING_FONT, fg=HEADING_COLOR, bg=GLOBAL_SIDEBAR_BG).pack(side="left", padx=(0,8))

		#stat groups
		self.stat_groups = [
			StatLabel(parent_frame, 0, "cases"),
			StatLabel(parent_frame, 0, "active"),
			StatLabel(parent_frame, 0, "recoveries"),
			StatLabel(parent_frame, 0, "deaths")
		]

		parent_frame.pack(expand=True)

		self.after(0, self.update)

	def update(self):
		country_data = DataManager.get_country_data_for(self.country_name)
		self.stat_groups[0].update(country_data.cases)
		self.stat_groups[1].update(country_data.active)
		self.stat_groups[2].update(country_data.recoveries)
		self.stat_groups[3].update(country_data.deaths)
		self.after(REFRESH_TIME, self.update)