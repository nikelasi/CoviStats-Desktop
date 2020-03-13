from tkinter import *
from tkinter import font
from tkinter import messagebox
import requests
import webbrowser
from bs4 import BeautifulSoup

globalstats_running = False
leaderboard_running = False

updateURL = "https://github.com/NicholasJohansan/COVID-19-Stats-Program-/raw/master/COVID19-STATS.exe"

version = "v2.101"

latest = version

main = Tk()
main.title("COVID-19")
main.geometry("+0+40")

titleFont = font.Font(family="times", size=20, weight="bold")
mainFont = font.Font(family="times", size=12)

def help_info_popup():
	messagebox.showinfo("Help/Info", "This Statistics app was made by @NJ889.\n\nIn this app, you can see:\n- SG COVID19 STATS\n- Global COVID19 STATS\n- Top 5 Countries affected by COVID19\n\nIn the case where the stats shown are \"N/A\" or \"0\", it is either that the website source does not exist anymore (possibly due to its irrelevancy in the future) or the source code of the websites has been changed and require new code.\n\nIn this event, you may contact me at \"ncov19.gspread@gmail.com\" to fix the problem or evaluate the issue.\n\n\nNicholas Johansan © 2020")

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
		result = requests.get("https://ncov2019.live/")
		src = result.content
		soup = BeautifulSoup(src, 'html.parser')


		temptags = []
		intdata = []
		DORSCON_color = ""

		##CONFIRMED [0]
		temptags.append(soup.findAll("p", {"style": "color: rgb(101, 221, 155); font-weight: bold; text-align: center; border-bottom: 0; font-size: 50px; margin-bottom: 0px;"})[0])

		#DEATHS [1]
		temptags.append(soup.findAll("p", {"style": "color: #F65164; font-weight: bold; text-align: center; border-bottom: 0; font-size: 50px; margin-bottom: 0px;"})[0])

		#SERIOUS [2]
		temptags.append(soup.findAll("p", {"style": "color: rgb(248, 245, 64); font-weight: bold; text-align: center; border-bottom: 0; font-size: 50px; margin-bottom: 0px;"})[0])

		#RECOVERED [3]
		temptags.append(soup.findAll("p", {"style": "color: rgb(68, 155, 226); font-weight: bold; text-align: center; border-bottom: 0; font-size: 50px; margin-bottom: 0px;"})[0])

		#COUNTRIES [4]
		temptags.append(soup.findAll("p", {"style": "color: #DFDFEF; font-weight: bold; text-align: center; border-bottom: 0; font-size: 50px; margin-bottom: 0px;"})[0].sup)

		##Integer Stats
		for tag in temptags:
			try:
				intdata.append(int(("".join((tag.text).split())).replace(',', '')))
			except:
				pass

		try:
			confirmed = intdata[0]
			death = intdata[1]
			critical = intdata[2]
			recovered = intdata[3]
			countries = intdata[4]
			hospitalised = confirmed - death - recovered
			stable = hospitalised - critical
		except:
			confirmed = "N/A"
			death = "N/A"
			critical = "N/A"
			recovered = "N/A"
			countries = "N/A"
			hospitalised = "N/A"
			stable = "N/A"
	except:
		confirmed = "N/A"
		death = "N/A"
		critical = "N/A"
		recovered = "N/A"
		countries = "N/A"
		hospitalised = "N/A"
		stable = "N/A"

	g_cfmcasesInt.config(text=f"{confirmed:,}")

	g_dischargedInt.config(text=f"{recovered:,}")

	g_hospitalisedInt.config(text=f"{hospitalised:,}")

	g_stableInt.config(text=f"{stable:,}")

	g_criticalInt.config(text=f"{critical:,}")

	g_deathInt.config(text=f"{death:,}")

	g_countriesInt.config(text=f"{countries}/195")

def globalStats():

	global globalstats_running
	global globalstats
	global g_cfmcasesInt
	global g_deathInt
	global g_stableInt
	global g_criticalInt
	global g_hospitalisedInt
	global g_dischargedInt
	global g_countriesInt

	if globalstats_running:
		return
	else:
		globalstats_running = True

	globalstats = Tk()
	globalstats.title("Global Stats")
	globalstats.geometry("+440+40")

	g_titleLbl = Label(globalstats, text="Global COVID-19 Statistics", font=("times", 20, "bold"), padx=10, pady=10)
	g_titleLbl.grid(row=0, column=0, columnspan=2)

	g_cfmcasesLbl = Label(globalstats, text="Confirmed Cases:", font=("times", 12), padx=10, pady=5)
	g_cfmcasesLbl.grid(row=1, column=0, sticky=W)
	g_cfmcasesInt = Label(globalstats, text="Number", font=("times", 12), padx=10, pady=5)
	g_cfmcasesInt.grid(row=1, column=1, sticky=W)

	g_dischargedLbl = Label(globalstats, text="Discharged:", font=("times", 12), padx=10, pady=5)
	g_dischargedLbl.grid(row=2, column=0, sticky=W)
	g_dischargedInt = Label(globalstats, text="Number", font=("times", 12), padx=10, pady=5)
	g_dischargedInt.grid(row=2, column=1, sticky=W)

	g_hospitalisedLbl = Label(globalstats, text="Hospitalised:", font=("times", 12), padx=10, pady=5)
	g_hospitalisedLbl.grid(row=3, column=0, sticky=W)
	g_hospitalisedInt = Label(globalstats, text="Number", font=("times", 12), padx=10, pady=5)
	g_hospitalisedInt.grid(row=3, column=1, sticky=W)

	g_stableLbl = Label(globalstats, text="Stable Cases:", font=("times", 12), padx=10, pady=5)
	g_stableLbl.grid(row=4, column=0, sticky=W)
	g_stableInt = Label(globalstats, text="Number", font=("times", 12), padx=10, pady=5)
	g_stableInt.grid(row=4, column=1, sticky=W)

	g_criticalLbl = Label(globalstats, text="Critical Cases:", font=("times", 12), padx=10, pady=5)
	g_criticalLbl.grid(row=5, column=0, sticky=W)
	g_criticalInt = Label(globalstats, text="Number", font=("times", 12), padx=10, pady=5)
	g_criticalInt.grid(row=5, column=1, sticky=W)

	g_deathLbl = Label(globalstats, text="Deaths:", font=("times", 12), padx=10, pady=5)
	g_deathLbl.grid(row=6, column=0, sticky=W)
	g_deathInt = Label(globalstats, text="Number", font=("times", 12), padx=10, pady=5)
	g_deathInt.grid(row=6, column=1, sticky=W)

	g_countriesLbl = Label(globalstats, text="Countries:", font=("times", 12), padx=10, pady=5)
	g_countriesLbl.grid(row=7, column=0, sticky=W)
	g_countriesInt = Label(globalstats, text="Number", font=("times", 12), padx=10, pady=5)
	g_countriesInt.grid(row=7, column=1, sticky=W)

	g_updateBtn = Button(globalstats, text="Update Stats", font=("times", 12), padx=10, pady=5, command=getGlobal, width=45)
	g_updateBtn.grid(row=8, column=0, columnspan=2)

	g_closeBtn = Button(globalstats, text="Close", font=("times", 12), padx=10, pady=5, command=g_close, width=45)
	g_closeBtn.grid(row=9, column=0, columnspan=2)

	getGlobal()

	globalstats.protocol("WM_DELETE_WINDOW", on_closing)
	globalstats.resizable(False, False)

def getLeaderboard():
	try:
		result = requests.get("https://ncov2019.live/")
		src = result.content
		soup = BeautifulSoup(src, 'html.parser')


		temptags = []
		top5tags = []
		DORSCON_color = ""

		for i in range(2, 7):
			temptags.append(soup.findAll("div", {"class":"container--wrap col "})[0].findAll("tr")[i])

		try:
			for tag in temptags:
				name = tag.findAll("span")[0].text
				cases = int(("".join((tag.findAll("span")[1].text).split())).replace(',', ''))
				deaths = int(("".join((tag.findAll("span")[2].text).split())).replace(',', ''))
				recovered = int(("".join((tag.findAll("span")[3].text).split())).replace(',', ''))
				hospitalised = cases - deaths - recovered
				top5tags.append([name, cases, hospitalised, recovered, deaths])
		except:
			top5tags = []
			for i in range(0, 5):
				top5tags.append(["N/A", 0, 0, 0, 0])

	except:
		top5tags = []
		for i in range(0, 5):
			top5tags.append(["N/A", 0, 0, 0, 0])

	c1_nameLbl.config(text=f"{top5tags[0][0]}")
	c1_casesLbl.config(text=f"{top5tags[0][1]:,}")
	c1_hospitalisedLbl.config(text=f"{top5tags[0][2]:,}")
	c1_dischargedLbl.config(text=f"{top5tags[0][3]:,}")
	c1_deathsLbl.config(text=f"{top5tags[0][4]:,}")

	c2_nameLbl.config(text=f"{top5tags[1][0]}")
	c2_casesLbl.config(text=f"{top5tags[1][1]:,}")
	c2_hospitalisedLbl.config(text=f"{top5tags[1][2]:,}")
	c2_dischargedLbl.config(text=f"{top5tags[1][3]:,}")
	c2_deathsLbl.config(text=f"{top5tags[1][4]:,}")

	c3_nameLbl.config(text=f"{top5tags[2][0]}")
	c3_casesLbl.config(text=f"{top5tags[2][1]:,}")
	c3_hospitalisedLbl.config(text=f"{top5tags[2][2]:,}")
	c3_dischargedLbl.config(text=f"{top5tags[2][3]:,}")
	c3_deathsLbl.config(text=f"{top5tags[2][4]:,}")

	c4_nameLbl.config(text=f"{top5tags[3][0]}")
	c4_casesLbl.config(text=f"{top5tags[3][1]:,}")
	c4_hospitalisedLbl.config(text=f"{top5tags[3][2]:,}")
	c4_dischargedLbl.config(text=f"{top5tags[3][3]:,}")
	c4_deathsLbl.config(text=f"{top5tags[3][4]:,}")

	c5_nameLbl.config(text=f"{top5tags[4][0]}")
	c5_casesLbl.config(text=f"{top5tags[4][1]:,}")
	c5_hospitalisedLbl.config(text=f"{top5tags[4][2]:,}")
	c5_dischargedLbl.config(text=f"{top5tags[4][3]:,}")
	c5_deathsLbl.config(text=f"{top5tags[4][4]:,}")

def leaderboardStats():

	global leaderboard_running
	global leaderboard

	global c1_nameLbl
	global c1_casesLbl
	global c1_hospitalisedLbl
	global c1_dischargedLbl
	global c1_deathsLbl

	global c2_nameLbl
	global c2_casesLbl
	global c2_hospitalisedLbl
	global c2_dischargedLbl
	global c2_deathsLbl

	global c3_nameLbl
	global c3_casesLbl
	global c3_hospitalisedLbl
	global c3_dischargedLbl
	global c3_deathsLbl

	global c4_nameLbl
	global c4_casesLbl
	global c4_hospitalisedLbl
	global c4_dischargedLbl
	global c4_deathsLbl

	global c5_nameLbl
	global c5_casesLbl
	global c5_hospitalisedLbl
	global c5_dischargedLbl
	global c5_deathsLbl

	if leaderboard_running:
		return
	else:
		leaderboard_running = True

	leaderboard = Tk()
	leaderboard.title("Top 5 Countries")
	leaderboard.geometry("+880+40")

	l_titleLbl = Label(leaderboard, text="Top 5 Countries with COVID-19", font=("times", 20, "bold"), padx=10, pady=10)
	l_titleLbl.grid(row=0, column=0, columnspan=5)

	l_countryLbl = Label(leaderboard, text="Country", font=("times", 12), padx=10, pady=5)
	l_countryLbl.grid(row=1, column=0, sticky=W)
	l_casesLbl = Label(leaderboard, text="Cases", font=("times", 12), padx=10, pady=5)
	l_casesLbl.grid(row=1, column=1, sticky=W)
	l_hospitalisedLbl = Label(leaderboard, text="Hospitalised", font=("times", 12), padx=10, pady=5)
	l_hospitalisedLbl.grid(row=1, column=2, sticky=W)
	l_dischargedLbl = Label(leaderboard, text="Discharged", font=("times", 12), padx=10, pady=5)
	l_dischargedLbl.grid(row=1, column=3, sticky=W)
	l_deathsLbl = Label(leaderboard, text="Deaths", font=("times", 12), padx=10, pady=5)
	l_deathsLbl.grid(row=1, column=4, sticky=W)

	c1_nameLbl = Label(leaderboard, text="Country", font=("times", 12), padx=10, pady=5)
	c1_nameLbl.grid(row=2, column=0, sticky=W)
	c1_casesLbl = Label(leaderboard, text="Cases", font=("times", 12), padx=10, pady=5)
	c1_casesLbl.grid(row=2, column=1, sticky=W)
	c1_hospitalisedLbl = Label(leaderboard, text="Hospitalised", font=("times", 12), padx=10, pady=5)
	c1_hospitalisedLbl.grid(row=2, column=2, sticky=W)
	c1_dischargedLbl = Label(leaderboard, text="Discharged", font=("times", 12), padx=10, pady=5)
	c1_dischargedLbl.grid(row=2, column=3, sticky=W)
	c1_deathsLbl = Label(leaderboard, text="Deaths", font=("times", 12), padx=10, pady=5)
	c1_deathsLbl.grid(row=2, column=4, sticky=W)

	c2_nameLbl = Label(leaderboard, text="Country", font=("times", 12), padx=10, pady=5)
	c2_nameLbl.grid(row=3, column=0, sticky=W)
	c2_casesLbl = Label(leaderboard, text="Cases", font=("times", 12), padx=10, pady=5)
	c2_casesLbl.grid(row=3, column=1, sticky=W)
	c2_hospitalisedLbl = Label(leaderboard, text="Hospitalised", font=("times", 12), padx=10, pady=5)
	c2_hospitalisedLbl.grid(row=3, column=2, sticky=W)
	c2_dischargedLbl = Label(leaderboard, text="Discharged", font=("times", 12), padx=10, pady=5)
	c2_dischargedLbl.grid(row=3, column=3, sticky=W)
	c2_deathsLbl = Label(leaderboard, text="Deaths", font=("times", 12), padx=10, pady=5)
	c2_deathsLbl.grid(row=3, column=4, sticky=W)

	c3_nameLbl = Label(leaderboard, text="Country", font=("times", 12), padx=10, pady=5)
	c3_nameLbl.grid(row=4, column=0, sticky=W)
	c3_casesLbl = Label(leaderboard, text="Cases", font=("times", 12), padx=10, pady=5)
	c3_casesLbl.grid(row=4, column=1, sticky=W)
	c3_hospitalisedLbl = Label(leaderboard, text="Hospitalised", font=("times", 12), padx=10, pady=5)
	c3_hospitalisedLbl.grid(row=4, column=2, sticky=W)
	c3_dischargedLbl = Label(leaderboard, text="Discharged", font=("times", 12), padx=10, pady=5)
	c3_dischargedLbl.grid(row=4, column=3, sticky=W)
	c3_deathsLbl = Label(leaderboard, text="Deaths", font=("times", 12), padx=10, pady=5)
	c3_deathsLbl.grid(row=4, column=4, sticky=W)

	c4_nameLbl = Label(leaderboard, text="Country", font=("times", 12), padx=10, pady=5)
	c4_nameLbl.grid(row=5, column=0, sticky=W)
	c4_casesLbl = Label(leaderboard, text="Cases", font=("times", 12), padx=10, pady=5)
	c4_casesLbl.grid(row=5, column=1, sticky=W)
	c4_hospitalisedLbl = Label(leaderboard, text="Hospitalised", font=("times", 12), padx=10, pady=5)
	c4_hospitalisedLbl.grid(row=5, column=2, sticky=W)
	c4_dischargedLbl = Label(leaderboard, text="Discharged", font=("times", 12), padx=10, pady=5)
	c4_dischargedLbl.grid(row=5, column=3, sticky=W)
	c4_deathsLbl = Label(leaderboard, text="Deaths", font=("times", 12), padx=10, pady=5)
	c4_deathsLbl.grid(row=5, column=4, sticky=W)

	c5_nameLbl = Label(leaderboard, text="Country", font=("times", 12), padx=10, pady=5)
	c5_nameLbl.grid(row=6, column=0, sticky=W)
	c5_casesLbl = Label(leaderboard, text="Cases", font=("times", 12), padx=10, pady=5)
	c5_casesLbl.grid(row=6, column=1, sticky=W)
	c5_hospitalisedLbl = Label(leaderboard, text="Hospitalised", font=("times", 12), padx=10, pady=5)
	c5_hospitalisedLbl.grid(row=6, column=2, sticky=W)
	c5_dischargedLbl = Label(leaderboard, text="Discharged", font=("times", 12), padx=10, pady=5)
	c5_dischargedLbl.grid(row=6, column=3, sticky=W)
	c5_deathsLbl = Label(leaderboard, text="Deaths", font=("times", 12), padx=10, pady=5)
	c5_deathsLbl.grid(row=6, column=4, sticky=W)

	l_updateBtn = Button(leaderboard, text="Update Stats", font=("times", 12), padx=10, pady=5, command=getLeaderboard, width=46)
	l_updateBtn.grid(row=7, column=0, columnspan=5)

	l_closeBtn = Button(leaderboard, text="Close", font=("times", 12), padx=10, pady=5, command=l_close, width=46)
	l_closeBtn.grid(row=8, column=0, columnspan=5)

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
		result = requests.get("https://www.moh.gov.sg/covid-19")
		src = result.content
		soup = BeautifulSoup(src, 'html.parser')


		temptags = []
		intdata = []
		DORSCON_color = ""

		##HOSPITALISED [0] - Critical [1] - Stable [0] - [1]
		for tag in soup.select('tr > td > font > span > b'):
			temptags.append(tag)

		##DEATH [2]
		temptags.append(soup.select("span > strong > span > span")[0])

		##DISCHARGED [3] - total [3] + [0] + [2]
		temptags.append(soup.select("td > strong > span")[1])

		##Integer Stats
		for tag in temptags:
			try:
				intdata.append(int("".join((tag.text).split())))
			except:
				pass

		try:
			hospitalised = intdata[0]
			critical = intdata[1]
			stable = hospitalised - critical
			death = intdata[2]
			discharged = intdata[3]
			total = hospitalised + discharged + death
		except:
			hospitalised = "N/A"
			stable = "N/A"
			critical = "N/A"
			death = "N/A"
			discharged = "N/A"
			total = "N/A"

		try:
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
		hospitalised = "N/A"
		stable = "N/A"
		critical = "N/A"
		death = "N/A"
		discharged = "N/A"
		total = "N/A"

		DORSCON_color = "#D5D8D7"

	cfmcasesInt.config(text=total)

	dischargedInt.config(text=discharged)

	hospitalisedInt.config(text=hospitalised)

	stableInt.config(text=stable)

	criticalInt.config(text=critical)

	deathInt.config(text=death)

	DORSCONLbl.config(background=DORSCON_color)


titleLbl = Label(main, text="SG COVID-19 Statistics", font=titleFont, padx=10, pady=10)
titleLbl.grid(row=0, column=0, columnspan=2)

cfmcasesLbl = Label(main, text="Confirmed Cases:", font=mainFont, padx=10, pady=5)
cfmcasesLbl.grid(row=1, column=0, sticky=W)
cfmcasesInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
cfmcasesInt.grid(row=1, column=1, sticky=W)

dischargedLbl = Label(main, text="Discharged:", font=mainFont, padx=10, pady=5)
dischargedLbl.grid(row=2, column=0, sticky=W)
dischargedInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
dischargedInt.grid(row=2, column=1, sticky=W)

hospitalisedLbl = Label(main, text="Hospitalised:", font=mainFont, padx=10, pady=5)
hospitalisedLbl.grid(row=3, column=0, sticky=W)
hospitalisedInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
hospitalisedInt.grid(row=3, column=1, sticky=W)

stableLbl = Label(main, text="Stable Cases:", font=mainFont, padx=10, pady=5)
stableLbl.grid(row=4, column=0, sticky=W)
stableInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
stableInt.grid(row=4, column=1, sticky=W)

criticalLbl = Label(main, text="Critical Cases:", font=mainFont, padx=10, pady=5)
criticalLbl.grid(row=5, column=0, sticky=W)
criticalInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
criticalInt.grid(row=5, column=1, sticky=W)

deathLbl = Label(main, text="Deaths:", font=mainFont, padx=10, pady=5)
deathLbl.grid(row=6, column=0, sticky=W)
deathInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
deathInt.grid(row=6, column=1, sticky=W)

DORSCONLbl = Label(main, text="DORSCON", font=mainFont, padx=10, pady=5, width=45)
DORSCONLbl.grid(row=7, column=0, columnspan=2)

updateBtn = Button(main, text="Update Stats", font=mainFont, padx=10, pady=5, command=getData, width=45)
updateBtn.grid(row=8, column=0, columnspan=2)

versionLbl = Label(main, text=f"Version: {version}, receiving latest version...", font=mainFont, padx=10, pady=5, width=45)
versionLbl.grid(row=9, column=0, columnspan=2)

updatBtn = Button(main, text="Update App", font=mainFont, padx=10, pady=5, command=getWeb, width=21, state=DISABLED)
updatBtn.grid(row=10, column=0)

infoBtn = Button(main, text="Info/Help", font=mainFont, padx=10, pady=5, command=help_info_popup, width=21)
infoBtn.grid(row=10, column=1)

globalBtn = Button(main, text="Global Stats", font=mainFont, padx=10, pady=5, command=globalStats, width=21)
globalBtn.grid(row=11, column=0)

leaderboardBtn = Button(main, text="Top 5 Countries", font=mainFont, padx=10, pady=5, command=leaderboardStats, width=21)
leaderboardBtn.grid(row=11, column=1)

closeBtn = Button(main, text="Close", font=mainFont, padx=10, pady=5, command=close, width=45)
closeBtn.grid(row=12, column=0, columnspan=2)

getData()

main.protocol("WM_DELETE_WINDOW", on_closing)
main.resizable(False, False)
main.mainloop()