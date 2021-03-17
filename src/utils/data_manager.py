from .scraper import DataScraper
from ui.standard import CountryFrame

numbers = lambda number: f"{number:,}"
class GlobalDataSession:
	def __init__(self, cases, active, recoveries, deaths):
		self.cases = cases
		self.active = active
		self.recoveries = recoveries
		self.deaths = deaths

	def __eq__(self, other):
		if not isinstance(other, self.__class__): return NotImplemented
		return (self.cases == other.cases) and (self.active == other.active) and (self.recoveries == other.recoveries) and (self.deaths == other.deaths)

	def __hash__(self):
		return hash((self.cases, self.active, self.recoveries, self.deaths))

class SpecificCountryData:
	def __init__(self, name, cases, active, recoveries, deaths):
		self.name = name
		self.cases = cases
		self.active = active
		self.recoveries = recoveries
		self.deaths = deaths

class SearchCountryData:
	def __init__(self, name, cases, country_box, app):
		self.name = name
		self.cases = cases
		self.frame = CountryFrame(country_box=country_box, app=app, data=self)
		self.frame.update_values(self)

class DataManager:
	@classmethod
	def get_global_data(cls):
		global_data = DataScraper.get_global_data()
		cases = numbers(global_data['cases'])
		active = numbers(global_data['active'])
		recoveries = numbers(global_data['recovered'])
		deaths = numbers(global_data['deaths'])
		return GlobalDataSession(cases, active, recoveries, deaths)

	@classmethod
	def get_countries_data(cls, country_box, app):
		countries_data = DataScraper.get_countries_data()
		formatted_data = map(lambda data: SearchCountryData(
			name=data['country'],
			cases=data['cases'],
			country_box=country_box,
			app=app
			),
			countries_data
		)
		return list(formatted_data)

	@classmethod
	def get_country_data_for(cls, country_name):
		data = DataScraper.get_country_data_for(country_name)
		return SpecificCountryData(
			name=data['country'],
			cases=numbers(data['cases']),
			recoveries=numbers(data['recovered']),
			active=numbers(data['active']),
			deaths=numbers(data['deaths'])
		)