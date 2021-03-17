import tkinter as tk
from config.colours import *
from config.fonts import SIDEBAR_STAT_FONT, SIDEBAR_LABEL_FONT, COUNTRIES_FONT

class ImageLabel(tk.Label):
	def __init__(self, parent, *args, **kwargs):
		tk.Label.__init__(self, parent, *args, **kwargs)
		self.image = kwargs['image']

class ImageButton(tk.Button):
	def __init__(self, parent, bg, *args, **kwargs):
		tk.Button.__init__(self, parent, *args, **kwargs)
		self.image = kwargs['image']
		self.config(
			relief=tk.FLAT,
			bg=bg,
			activebackground=bg,
			borderwidth=0,
		)

class StatLabel(tk.Frame):
	def __init__(self, parent, number, name):
		tk.Frame.__init__(self, parent)
		self['bg'] = GLOBAL_SIDEBAR_BG
		self['highlightthickness'] = 0
		self.pack(side="top")

		self.number_label = tk.Label(self, text=number, highlightthickness=0, bg=GLOBAL_SIDEBAR_BG, fg=GLOBAL_SIDEBAR_STAT_FG, font=SIDEBAR_STAT_FONT)
		self.number_label.grid(row=0, column=0, sticky=tk.S)

		self.name_label = tk.Label(self, text=name, highlightthickness=0, bg=GLOBAL_SIDEBAR_BG, fg=GLOBAL_SIDEBAR_NAME_FG, font=SIDEBAR_LABEL_FONT)
		self.name_label.grid(row=1, column=0, sticky=tk.N)

		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=1)

	def update(self, number):
		self.number_label.config(
			text=number
		)

class CountrySearch(tk.Entry):
	def __init__(self, *args, **kwargs):
		tk.Entry.__init__(self, *args, **kwargs)
		self.config(
			fg=SEARCHBAR_HINT_COLOR,
			bg=SEARCHBAR_BG_COLOR,
			bd=5,
			selectforeground=SEARCHBAR_BG_COLOR,
			selectbackground=SEARCHBAR_TXT_COLOR,
			justify="left",
			disabledbackground="#303030",
			disabledforeground=SEARCHBAR_TXT_COLOR,
			relief=tk.FLAT,
			insertbackground=SEARCHBAR_TXT_COLOR,
			insertborderwidth=1
		)
		self.placeholder = "Search"
		self.insert("0", self.placeholder)
		self.bind("<FocusIn>", self._clear_placeholder)
		self.bind("<FocusOut>", self._add_placeholder)

	def _clear_placeholder(self, e=None):
		if self["fg"] == SEARCHBAR_HINT_COLOR:
			self.delete("0", "end")
			self["fg"] = SEARCHBAR_TXT_COLOR

	def _add_placeholder(self, e=None):
		if not self.get():
			self.insert("0", self.placeholder)
			self["fg"] = SEARCHBAR_HINT_COLOR

class CountryFrame(tk.Frame):
	def __init__(self, country_box, app, data, *args, **kwargs):
		tk.Frame.__init__(self, country_box, bg=COUNTRYBOX_BG_COLOR, *args, **kwargs)
		self.data = data
		self.country_button = tk.Button(self, fg=COUNTRIES_TEXT_COLOR, justify="left", bg=SEARCHBAR_BG_COLOR, activebackground=COUNTRY_FRAME_ACTIVE_BG, borderwidth=0,relief=tk.FLAT, text="", font=COUNTRIES_FONT, command=lambda: app.show_country_details(data.name))
		self.country_button.pack(side="left", padx=8, pady=4, fill="x", expand=True)
		cases_frame = tk.Frame(self, bg=COUNTRYBOX_BG_COLOR, width=15)
		cases_frame.pack(side="right", padx=8)
		self.cases_label = tk.Label(cases_frame, fg=COUNTRIES_TEXT_COLOR, bg=COUNTRYBOX_BG_COLOR, width=15, text="", font=COUNTRIES_FONT)
		self.cases_label.pack(side="right", padx=8)

	def update_values(self, country_data):
		self.data = country_data
		self.country_button.config(
			text=country_data.name
		)
		self.cases_label.config(
			text=f"{country_data.cases:,} cases"
		)

class ScrollableFrame(tk.Frame):
	def __init__(self, container):
		tk.Frame.__init__(self, container)
		self.container = container
		self.container['bg'] = COUNTRYBOX_BG_COLOR
		self['bg'] = COUNTRYBOX_BG_COLOR
		self['bd'] = 0
		self._setup_scrollable_frame()

	def _setup_scrollable_frame(self):
		self.canv = tk.Canvas(self, bg=COUNTRYBOX_BG_COLOR, bd=0, highlightthickness=0)
		self.canv.config(bg=COUNTRYBOX_BG_COLOR)
		scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canv.yview, bg=COUNTRYBOX_BG_COLOR, troughcolor=COUNTRYBOX_BG_COLOR)
		self.scrollable_frame = tk.Frame(self.canv, bg=COUNTRYBOX_BG_COLOR, bd=0)

		self.scrollable_frame.bind(
			"<Configure>",
			lambda e: self.canv.configure(
				scrollregion=self.canv.bbox("all")
			)
		)

		self.canvas_frame = self.canv.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

		self.canv.configure(yscrollcommand=scrollbar.set)

		self.grid(row=0, column=0, sticky="nesw")
		self.container.grid_rowconfigure(0, minsize=400, weight=2)
		self.container.grid_columnconfigure(0, minsize=450, weight=2)
		self.canv.pack(side="left", fill="both", expand=1)
		scrollbar.pack(side="right", fill="y")
 
		self.bind('<Enter>', self._bound_to_mousewheel)
		self.bind('<Leave>', self._unbound_to_mousewheel)
		self.scrollable_frame.bind("<Configure>", self._frame_configure)
		self.canv.bind("<Configure>", self._on_frame_configure)

	def _frame_configure(self, event):
		self.canv.configure(scrollregion=self.canv.bbox("all"))
		self.after(1000, lambda: self._frame_configure(event))

	def _on_frame_configure(self, event):
		canvas_width = event.width
		self.canv.itemconfig(self.canvas_frame, width=canvas_width)

	def _bound_to_mousewheel(self, event):
		self.canv.bind_all("<MouseWheel>", self._on_mousewheel)   

	def _unbound_to_mousewheel(self, event):
		self.canv.unbind_all("<MouseWheel>") 

	def _on_mousewheel(self, event):
		visible_children = filter(lambda x: x, map(lambda child: child.winfo_ismapped(), self.scrollable_frame.winfo_children()))
		if len(list(visible_children)) < 7:
			self.canv.yview_scroll(0, "units")
		else:
			self.canv.yview_scroll(int(-1*(event.delta/50)), "units")

	def _reset(self):
		for child in self.scrollable_frame.winfo_children():
			child.pack_forget()