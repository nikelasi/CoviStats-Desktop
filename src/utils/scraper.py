import requests, json, urllib.parse

class DataScraper:
	base_url = "https://disease.sh/v3/covid-19/"
	global_url = base_url + "all"
	countries_url = base_url + "countries"

	@classmethod
	def get_global_data(cls):
		return cls.fetch_data(cls.global_url)

	@classmethod
	def get_countries_data(cls):
		return cls.fetch_data(cls.countries_url)

	@classmethod
	def get_country_data_for(cls, country):
		formatted_country_name = urllib.parse.quote(country.lower())
		url = cls.countries_url + f"/{formatted_country_name}"
		return cls.fetch_data(url)

	@classmethod
	def fetch_data(cls, url):
		data = requests.get(url)
		return json.loads(data.content)