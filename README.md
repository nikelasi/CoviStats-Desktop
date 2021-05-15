# CoviStats
![](https://raw.githubusercontent.com/NicholasJohansan/CoviStats/master/assets/app/banner.png)

CoviStats is a improved version of its predecessor

It is just a generic app which shows the number of the following in countries:
- Total cases
- Active cases
- Recoveries
- Deaths

It is meant to be a project for me to practice programming an app using python with tkinter and improve my skills.
## Features
- Global statistics
- Countries statistics
- Country search
- Sort data
- Latest data every 5 minutes

The data is sourced from the [disease.sh API](https://github.com/disease-sh/api) which sources data from [Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19), [New York Times](https://github.com/nytimes/covid-19-data), [Worldometers](https://www.worldometers.info/coronavirus/) and [Apple reports](https://github.com/ActiveConclusion/COVID19_mobility). As for the sources for other country-specific data, it can be found in their [README](https://github.com/disease-sh/api/blob/master/README.md).

And all the graphics used are original and made by myself while the font is [Josefin Sans](https://fonts.adobe.com/fonts/josefin-sans)
## Usage
![Screenshot](https://raw.githubusercontent.com/NicholasJohansan/CoviStats/master/assets/screenshots/country_details.png)

In the app, you can view the global statistics on the sidebar
You can also search for countries using the searchbar
To view data on a country, click on the button labelled with the country name inside the scrollbox
To close the data on a country, just click the x button next to its name on the right sidebar that opens up when you click on a country

As for sorting data,

![](https://raw.githubusercontent.com/NicholasJohansan/CoviStats/master/assets/app/filter_buttons/a_to_z_alphabetical_filter_icon.png) will sort the countries from a to z alphabetically

![](https://raw.githubusercontent.com/NicholasJohansan/CoviStats/master/assets/app/filter_buttons/z_to_a_alphabetical_filter_icon.png) will sort the countries from z to a alphabetically

![](https://raw.githubusercontent.com/NicholasJohansan/CoviStats/master/assets/app/filter_buttons/ascending_cases_filter_icon.png) will sort countries by their total cases in ascending order (low to high)

![](https://raw.githubusercontent.com/NicholasJohansan/CoviStats/master/assets/app/filter_buttons/descending_cases_filter_icon.png) will sort countries by their total cases in descending order (high to low)

Hope you have a great day ahead!

## Libraries
The libraries used are:
- [`tkinter`](https://docs.python.org/3/library/tkinter.html) (gui framework)
- [`urllib`](https://docs.python.org/3/library/urllib.html) (for url encoding)
- [`pyglet`](https://pypi.org/project/pyglet/) (for loading font)
- [`requests`](https://pypi.org/project/requests/) (for requesting data)

## License [![Unlicense](https://img.shields.io/github/license/NicholasJohansan/EP5)](LICENSE)
CoviStats is [Unlicense](https://unlicense.org/) Licensed (file [LICENSE](LICENSE)).
