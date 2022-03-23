
const api = (() => {
  const BASE_URL = 'https://disease.sh/v3/covid-19/'
  const GLOBAL_URL = BASE_URL + 'all'
  const COUNTRIES_URL = BASE_URL + 'countries'

  const countryMaker = (data) => {
    return {
      name: data.country,
      cases: data.cases
    }
  }

  const fetchData = async (url) => {
    const response = await fetch(url)
    return await response.json()
  }

  const getGlobalData = async () => {
    return await fetchData(GLOBAL_URL)
  }

  const getCountriesData = async () => {
    return await fetchData(COUNTRIES_URL)
  }

  const getCountryData = async (country) => {
    const url = COUNTRIES_URL + `/${encodeURIComponent(country.toLowerCase())}`
    return await fetchData(url)
  }
  
  const getCountries = async () => {
    const countries = await getCountriesData()
    return countries.map(data => countryMaker(data))
  }
  
  return {
    getGlobalData,
    getCountriesData,
    getCountries,
    getCountryData
  }
})()

export default api