from tkinter import *
from tkinter import font
from tkinter import messagebox
import requests
import webbrowser
import json
from bs4 import BeautifulSoup

globalstats_running = False
leaderboard_running = False

updateURL = "https://github.com/NicholasJohansan/COVID-19-Stats-Program-/raw/master/COVID19-STATS.exe"

version = "v3.10"

latest = version

main = Tk()
main.title("COVID-19")
main.geometry("+0+40")

titleFont = font.Font(family="times", size=20, weight="bold")
mainFont = font.Font(family="times", size=12)

class SG_Card:

	def __init__(self):
		self.cfmcasesLbl = Label(main, text="Cases:", font=mainFont, padx=10, pady=5)
		self.cfmcasesLbl.grid(row=1, column=0, sticky=W)
		self.cfmcasesInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
		self.cfmcasesInt.grid(row=1, column=1, sticky=W)

		self.dischargedLbl = Label(main, text="Recovered:", font=mainFont, padx=10, pady=5)
		self.dischargedLbl.grid(row=2, column=0, sticky=W)
		self.dischargedInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
		self.dischargedInt.grid(row=2, column=1, sticky=W)

		self.hospitalisedLbl = Label(main, text="Active Cases:", font=mainFont, padx=10, pady=5)
		self.hospitalisedLbl.grid(row=3, column=0, sticky=W)
		self.hospitalisedInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
		self.hospitalisedInt.grid(row=3, column=1, sticky=W)

		self.stableLbl = Label(main, text="Stable Cases:", font=mainFont, padx=10, pady=5)
		self.stableLbl.grid(row=4, column=0, sticky=W)
		self.stableInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
		self.stableInt.grid(row=4, column=1, sticky=W)

		self.criticalLbl = Label(main, text="Critical Cases:", font=mainFont, padx=10, pady=5)
		self.criticalLbl.grid(row=5, column=0, sticky=W)
		self.criticalInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
		self.criticalInt.grid(row=5, column=1, sticky=W)

		self.deathLbl = Label(main, text="Deaths:", font=mainFont, padx=10, pady=5)
		self.deathLbl.grid(row=6, column=0, sticky=W)
		self.deathInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
		self.deathInt.grid(row=6, column=1, sticky=W)

		self.TodayLbl = Label(main, text="Today (Included)", font=mainFont, padx=10, pady=5, width=45, background="#d3d3d3")
		self.TodayLbl.grid(row=7, column=0, columnspan=2)

		self.newCasesLbl = Label(main, text="New Cases:", font=mainFont, padx=10, pady=5)
		self.newCasesLbl.grid(row=8, column=0, sticky=W)
		self.newCasesInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
		self.newCasesInt.grid(row=8, column=1, sticky=W)

		self.newDeathsLbl = Label(main, text="New Deaths:", font=mainFont, padx=10, pady=5)
		self.newDeathsLbl.grid(row=9, column=0, sticky=W)
		self.newDeathsInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
		self.newDeathsInt.grid(row=9, column=1, sticky=W)

		self.DORSCONLbl = Label(main, text="DORSCON", font=mainFont, padx=10, pady=5, width=45)
		self.DORSCONLbl.grid(row=10, column=0, columnspan=2)

	def update(self, d1, d2, d3, d4, d5, d6, d7, d8, d9):

		try:
			self.cfmcasesInt.config(text=f"{int(d1):,}")
			self.dischargedInt.config(text=f"{int(d2):,}")
			self.hospitalisedInt.config(text=f"{int(d3):,}")
			self.stableInt.config(text=f"{int(d4):,}")
			self.criticalInt.config(text=f"{int(d5):,}")
			self.deathInt.config(text=f"{int(d6):,}")
			self.DORSCONLbl.config(background=d7)
			self.newCasesInt.config(text=f"{int(d8):,}")
			self.newDeathsInt.config(text=f"{int(d9):,}")
		except:
			self.cfmcasesInt.config(text=f"{d1}")
			self.dischargedInt.config(text=f"{d2}")
			self.hospitalisedInt.config(text=f"{d3}")
			self.stableInt.config(text=f"{d4}")
			self.criticalInt.config(text=f"{d5}")
			self.deathInt.config(text=f"{d6}")
			self.DORSCONLbl.config(background=d7)
			self.newCasesInt.config(text=f"{d8}")
			self.newDeathsInt.config(text=f"{d9}")

class G_Card:

	def __init__(self):

		self.cfmcasesLbl = Label(globalstats, text="Cases:", font=("times", 12), padx=10, pady=5)
		self.cfmcasesLbl.grid(row=1, column=0, sticky=W)
		self.cfmcasesInt = Label(globalstats, text="Number", font=("times", 12), padx=10, pady=5)
		self.cfmcasesInt.grid(row=1, column=1, sticky=W)

		self.dischargedLbl = Label(globalstats, text="Recovered:", font=("times", 12), padx=10, pady=5)
		self.dischargedLbl.grid(row=2, column=0, sticky=W)
		self.dischargedInt = Label(globalstats, text="Number", font=("times", 12), padx=10, pady=5)
		self.dischargedInt.grid(row=2, column=1, sticky=W)

		self.hospitalisedLbl = Label(globalstats, text="Active Cases:", font=("times", 12), padx=10, pady=5)
		self.hospitalisedLbl.grid(row=3, column=0, sticky=W)
		self.hospitalisedInt = Label(globalstats, text="Number", font=("times", 12), padx=10, pady=5)
		self.hospitalisedInt.grid(row=3, column=1, sticky=W)

		self.stableLbl = Label(globalstats, text="Stable Cases:", font=("times", 12), padx=10, pady=5)
		self.stableLbl.grid(row=4, column=0, sticky=W)
		self.stableInt = Label(globalstats, text="Number", font=("times", 12), padx=10, pady=5)
		self.stableInt.grid(row=4, column=1, sticky=W)

		self.criticalLbl = Label(globalstats, text="Critical Cases:", font=("times", 12), padx=10, pady=5)
		self.criticalLbl.grid(row=5, column=0, sticky=W)
		self.criticalInt = Label(globalstats, text="Number", font=("times", 12), padx=10, pady=5)
		self.criticalInt.grid(row=5, column=1, sticky=W)

		self.deathLbl = Label(globalstats, text="Deaths:", font=("times", 12), padx=10, pady=5)
		self.deathLbl.grid(row=6, column=0, sticky=W)
		self.deathInt = Label(globalstats, text="Number", font=("times", 12), padx=10, pady=5)
		self.deathInt.grid(row=6, column=1, sticky=W)

		self.TodayLbl = Label(globalstats, text="Today (Included)", font=("times", 12), padx=10, pady=5, width=45, background="#d3d3d3")
		self.TodayLbl.grid(row=7, column=0, columnspan=2)

		self.newCasesLbl = Label(globalstats, text="New Cases:", font=("times", 12), padx=10, pady=5)
		self.newCasesLbl.grid(row=8, column=0, sticky=W)
		self.newCasesInt = Label(globalstats, text="Number", font=("times", 12), padx=10, pady=5)
		self.newCasesInt.grid(row=8, column=1, sticky=W)

		self.newDeathsLbl = Label(globalstats, text="New Deaths:", font=("times", 12), padx=10, pady=5)
		self.newDeathsLbl.grid(row=9, column=0, sticky=W)
		self.newDeathsInt = Label(globalstats, text="Number", font=("times", 12), padx=10, pady=5)
		self.newDeathsInt.grid(row=9, column=1, sticky=W)

	def update(self, d1, d2, d3, d4, d5, d6, d7, d8):

		try:
			self.cfmcasesInt.config(text=f"{int(d1):,}")
			self.dischargedInt.config(text=f"{int(d2):,}")
			self.hospitalisedInt.config(text=f"{int(d3):,}")
			self.stableInt.config(text=f"{int(d4):,}")
			self.criticalInt.config(text=f"{int(d5):,}")
			self.deathInt.config(text=f"{int(d6):,}")
			self.newCasesInt.config(text=f"{int(d7):,}")
			self.newDeathsInt.config(text=f"{int(d8):,}")
		except:
			self.cfmcasesInt.config(text=f"{d1}")
			self.dischargedInt.config(text=f"{d2}")
			self.hospitalisedInt.config(text=f"{d3}")
			self.stableInt.config(text=f"{d4}")
			self.criticalInt.config(text=f"{d5}")
			self.deathInt.config(text=f"{d6}")
			self.newCasesInt.config(text=f"{d7}")
			self.newDeathsInt.config(text=f"{d8}")

class L_Card:

	def __init__(self, row):
		self.name = "Country"
		self.cases = "Cases"
		self.hospitalised = "Active"
		self.discharged = "Recovered"
		self.deaths = "Deaths"

		self.countryLbl = Label(leaderboard, text=self.name, font=("times", 12), padx=10, pady=5)
		self.countryLbl.grid(row=row, column=0, sticky=W)
		self.casesLbl = Label(leaderboard, text=self.cases, font=("times", 12), padx=10, pady=5)
		self.casesLbl.grid(row=row, column=1, sticky=W)
		self.hospitalisedLbl = Label(leaderboard, text=self.hospitalised, font=("times", 12), padx=10, pady=5)
		self.hospitalisedLbl.grid(row=row, column=2, sticky=W)
		self.dischargedLbl = Label(leaderboard, text=self.discharged, font=("times", 12), padx=10, pady=5)
		self.dischargedLbl.grid(row=row, column=3, sticky=W)
		self.deathsLbl = Label(leaderboard, text=self.deaths, font=("times", 12), padx=10, pady=5)
		self.deathsLbl.grid(row=row, column=4, sticky=W)

	def update(self, index, dataset):

		self.countryLbl.config(text=f"{dataset[index][0]}")
		self.casesLbl.config(text=f"{int(dataset[index][1]):,}")
		self.hospitalisedLbl.config(text=f"{int(dataset[index][2]):,}")
		self.dischargedLbl.config(text=f"{int(dataset[index][3]):,}")
		self.deathsLbl.config(text=f"{int(dataset[index][4]):,}")

def help_info_popup():
	messagebox.showinfo("Help/Info", "This Statistics app was made by @NJ889.\n\nIn this app, you can see:\n- SG COVID19 STATS\n- Global COVID19 STATS\n- Countries Leaderboard\n\nIn the case where the stats shown are \"N/A\" or \"0\", it is probable that the website source does not exist anymore (possibly due to its irrelevancy in the future).\n\nHowever if you think that shouldn\'t have been an error, you may contact me at \"ncov19.gspread@gmail.com\" to fix the problem or evaluate the issue.\n\nSource Data from \"https://coronavirus-19-api.herokuapp.com/countries\", a stats API.\n\n\nNicholas Johansan © 2020")

def l_close():
	global leaderboard_running
	leaderboard_running = False
	leaderboard.destroy()

def g_close():
	global globalstats_running
	globalstats_running = False
	globalstats.destroy()

def close():
	try:
		globalstats.destroy()
	except:
		pass

	try:
		leaderboard.destroy()
	except:
		pass

	main.destroy()

def on_closing():
	pass

def getGlobal():

	try:
		result = requests.get("https://coronavirus-19-api.herokuapp.com/countries")
		listdata = json.loads(result.content.decode())

		cases = listdata[0]['cases']
		active = listdata[0]['active']
		deaths = listdata[0]['deaths']
		recovered = listdata[0]['recovered']
		critical = listdata[0]['critical']
		stable = active - critical
		newCases = listdata[0]['todayCases']
		newDeaths = listdata[0]['todayDeaths']

	except:
		cases = "N/A"
		active = "N/A"
		deaths = "N/A"
		recovered = "N/A"
		critical = "N/A"
		stable = "N/A"
		newCases = "N/A"
		newDeaths = "N/A"

	globalCard.update(cases, recovered, active, stable, critical, deaths, newCases, newDeaths)

def globalStats():

	global globalstats_running
	global globalstats
	global globalCard

	if globalstats_running:
		return
	else:
		globalstats_running = True

	globalstats = Tk()
	globalstats.title("Global Stats")
	globalstats.geometry("+440+40")

	g_titleLbl = Label(globalstats, text="Global COVID-19 Statistics", font=("times", 20, "bold"), padx=10, pady=10)
	g_titleLbl.grid(row=0, column=0, columnspan=2)

	globalCard = G_Card()

	g_updateBtn = Button(globalstats, text="Update Stats", font=("times", 12), padx=10, pady=5, command=getGlobal, width=45)
	g_updateBtn.grid(row=10, column=0, columnspan=2)

	g_closeBtn = Button(globalstats, text="Close", font=("times", 12), padx=10, pady=5, command=g_close, width=45)
	g_closeBtn.grid(row=11, column=0, columnspan=2)

	getGlobal()

	globalstats.protocol("WM_DELETE_WINDOW", on_closing)
	globalstats.resizable(False, False)

def getLeaderboard():
	try:
		result = requests.get("https://coronavirus-19-api.herokuapp.com/countries")
		listdata = json.loads(result.content.decode())

		top5tags = []

		for i in range(1,4):
			try:
				name = listdata[i]['country']
				cases = listdata[i]['cases']
				active = listdata[i]['active']
				deaths = listdata[i]['deaths']
				recovered = listdata[i]['recovered']
				critical = listdata[i]['critical']
				stable = active - critical
				top5tags.append([name, cases, active, recovered, deaths])
			except:
				top5tags.append(["N/A", 0, 0, 0, 0])
	except:
		top5tags = []
		for i in range(0, 5):
			top5tags.append(["N/A", 0, 0, 0, 0])

	c1.update(0, top5tags)
	c2.update(1, top5tags)
	c3.update(2, top5tags)

def leaderboardStats():

	global leaderboard_running
	global leaderboard

	global c1, c2, c3, c4, c5
	if leaderboard_running:
		return
	else:
		leaderboard_running = True

	leaderboard = Tk()
	leaderboard.title("Leaderboard")
	leaderboard.geometry("+880+40")

	l_titleLbl = Label(leaderboard, text="Countries Leaderboard", font=("times", 20, "bold"), padx=10, pady=10)
	l_titleLbl.grid(row=0, column=0, columnspan=5)

	l_header = L_Card(1)

	c1 = L_Card(2)
	c2 = L_Card(3)
	c3 = L_Card(4)

	l_updateBtn = Button(leaderboard, text="Update Stats", font=("times", 12), padx=10, pady=5, command=getLeaderboard, width=46)
	l_updateBtn.grid(row=5, column=0, columnspan=5)

	l_closeBtn = Button(leaderboard, text="Close", font=("times", 12), padx=10, pady=5, command=l_close, width=46)
	l_closeBtn.grid(row=6, column=0, columnspan=5)

	getLeaderboard()

	leaderboard.protocol("WM_DELETE_WINDOW", on_closing)
	leaderboard.resizable(False, False)

def getWeb():
	global updateURL
	webbrowser.open_new(updateURL)

def getData():

	global latest
	global version

	try:
		result = requests.get("https://github.com/NicholasJohansan/COVID-19-Stats-Program-/blob/master/version.txt")
		src = result.content
		soup = BeautifulSoup(src, 'html.parser')

		latest = soup.findAll("td", {"class": "blob-code blob-code-inner js-file-line"})[0].text

		if version == latest:
			versionLbl.config(text=f"Version: {version}, You are on the latest version!")
		elif version != latest:
			updatBtn.config(state="normal")
			versionLbl.config(text=f"Version: {version}, version {latest} is available. Please update!")
	except:
		versionLbl.config(text=f"Version: {version}")
	try:
		result = requests.get("https://coronavirus-19-api.herokuapp.com/countries")
		listdata = json.loads(result.content.decode())

		for i in range(len(listdata)):
			if listdata[i]['country'] == "Singapore":
				cases = listdata[i]['cases']
				active = listdata[i]['active']
				deaths = listdata[i]['deaths']
				recovered = listdata[i]['recovered']
				critical = listdata[i]['critical']
				stable = active - critical
				newCases = listdata[i]['todayCases']
				newDeaths = listdata[i]['todayDeaths']

		try:
			result = requests.get("https://www.moh.gov.sg/covid-19")
			src = result.content
			soup = BeautifulSoup(src, 'html.parser')
			DORSCON_color = ""
			for tag in soup.select('div > table > tbody > tr > td > h4 > strong > span')[1:]:
				if tag.text == "Green":
					DORSCON_color = "#ABE553"
				elif tag.text == "Yellow":
					DORSCON_color = "#FFCD00"
				elif tag.text == "Orange":
					DORSCON_color = "#FF7D01"
				elif tag.text == "Red":
					DORSCON_color = "#F85A4F"
				else:
					DORSCON_color = "#D5D8D7"
		except:
			DORSCON_color = "#D5D8D7"
	except:
		cases = "N/A"
		active = "N/A"
		deaths = "N/A"
		recovered = "N/A"
		critical = "N/A"
		stable = "N/A"
		newCases = "N/A"
		newDeaths = "N/A"

		DORSCON_color = "#D5D8D7"

	sgCard.update(cases, recovered, active, stable, critical, deaths, DORSCON_color, newCases, newDeaths)




titleLbl = Label(main, text="SG COVID-19 Statistics", font=titleFont, padx=10, pady=10)
titleLbl.grid(row=0, column=0, columnspan=2)

sgCard = SG_Card()

updateBtn = Button(main, text="Update Stats", font=mainFont, padx=10, pady=5, command=getData, width=45)
updateBtn.grid(row=11, column=0, columnspan=2)

versionLbl = Label(main, text=f"Version: {version}, receiving latest version...", font=mainFont, padx=10, pady=5, width=45)
versionLbl.grid(row=12, column=0, columnspan=2)

updatBtn = Button(main, text="Update App", font=mainFont, padx=10, pady=5, command=getWeb, width=21, state=DISABLED)
updatBtn.grid(row=13, column=0)

infoBtn = Button(main, text="Info/Help", font=mainFont, padx=10, pady=5, command=help_info_popup, width=21)
infoBtn.grid(row=13, column=1)

globalBtn = Button(main, text="Global Stats", font=mainFont, padx=10, pady=5, command=globalStats, width=21)
globalBtn.grid(row=14, column=0)

leaderboardBtn = Button(main, text="Countries Leaderboard", font=mainFont, padx=10, pady=5, command=leaderboardStats, width=21)
leaderboardBtn.grid(row=14, column=1)

closeBtn = Button(main, text="Close", font=mainFont, padx=10, pady=5, command=close, width=45)
closeBtn.grid(row=15, column=0, columnspan=2)

getData()

main.protocol("WM_DELETE_WINDOW", on_closing)
main.resizable(False, False)
main.mainloop()