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

	result = requests.get("https://www.moh.gov.sg/covid-19")
	src = result.content
	soup = BeautifulSoup(src, 'html.parser')


	temptags = []
	intdata = []
	DORSCON_color = ""

	##HOSPITALISED
	for tag in soup.select('div > div > table > tbody > tr > td > p > span > strong'):
	    temptags.append(tag)

	##DISCHARGED - TOTAL CONFIRMED
	for tag in soup.select('tr > td > p > font > b'):
	    temptags.append(tag)

	##Integer Stats
	for tag in temptags:
	    try:
	        intdata.append(int("".join((tag.text).split())))
	    except:
	        pass

	if intdata == []:
	    intdata = ["N/A", "N/A", "N/A"]

	##DORSCON COLOR
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

	if DORSCON_color == "":
	    DORSCON_color = "#D5D8D7"

	cfmcasesInt.config(text=intdata[2])

	hospitalisedInt.config(text=intdata[0])

	dischargedInt.config(text=intdata[1])

	deadInt.config(text=0)

	DORSCONLbl.config(background=DORSCON_color)


titleLbl = Label(main, text="SG COVID-19 Statistics", font=titleFont, padx=10, pady=10)
titleLbl.grid(row=0, column=0, columnspan=3)

cfmcasesLbl = Label(main, text="Confirmed Cases:", font=mainFont, padx=10, pady=5)
cfmcasesLbl.grid(row=1, column=0, sticky=W)
cfmcasesInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
cfmcasesInt.grid(row=1, column=1, sticky=W)

hospitalisedLbl = Label(main, text="Hospitalised:", font=mainFont, padx=10, pady=5)
hospitalisedLbl.grid(row=2, column=0, sticky=W)
hospitalisedInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
hospitalisedInt.grid(row=2, column=1, sticky=W)

dischargedLbl = Label(main, text="Discharged:", font=mainFont, padx=10, pady=5)
dischargedLbl.grid(row=3, column=0, sticky=W)
dischargedInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
dischargedInt.grid(row=3, column=1, sticky=W)

deadLbl = Label(main, text="Deaths:", font=mainFont, padx=10, pady=5)
deadLbl.grid(row=4, column=0, sticky=W)
deadInt = Label(main, text="Number", font=mainFont, padx=10, pady=5)
deadInt.grid(row=4, column=1, sticky=W)

DORSCONLbl = Label(main, text="DORSCON", font=mainFont, padx=10, pady=5, width=30)
DORSCONLbl.grid(row=5, column=0, columnspan=3)

updateBtn = Button(main, text="Update", font=mainFont, padx=10, pady=5, command=getData, width=30)
updateBtn.grid(row=6, column=0, columnspan=3)

getData()

main.mainloop()