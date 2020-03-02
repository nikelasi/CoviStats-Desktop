from tkinter import *
from tkinter import font
import requests
import time
from bs4 import BeautifulSoup

main = Tk()
main.title("COVID-19")
main.geometry("+25+80")

titleFont = font.Font(family="times", size=15, weight="bold")
mainFont = font.Font(family="times", size=10)

def getData():

	try:
		result = requests.get("https://www.moh.gov.sg/covid-19")
		src = result.content
		soup = BeautifulSoup(src, 'html.parser')


		temptags = []
		intdata = []
		DORSCON_color = ""

		##HOSPITALISED [0] - STABLE [1] - DEATH [2] - critical [0] - [1]
		for tag in soup.select('tr > td > span > strong > span'):
			temptags.append(tag)

		##DISCHARGED [3] - total [3] + [0]
		for tag in soup.select('tr > td > strong > span'):
			temptags.append(tag)

		##Integer Stats
		for tag in temptags:
			try:
				intdata.append(int("".join((tag.text).split())))
			except:
				pass

		try:
			hospitalised = intdata[0]
			stable = intdata[1]
			critical = intdata[0] - intdata[1]
			death = intdata[2]
			discharged = intdata[3]
			total = intdata[3] + intdata[0]
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
titleLbl.grid(row=0, column=0, columnspan=3)

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

DORSCONLbl = Label(main, text="DORSCON", font=mainFont, padx=10, pady=5, width=30)
DORSCONLbl.grid(row=7, column=0, columnspan=3)

updateBtn = Button(main, text="Update", font=mainFont, padx=10, pady=5, command=getData, width=30)
updateBtn.grid(row=8, column=0, columnspan=3)

getData()

main.mainloop()