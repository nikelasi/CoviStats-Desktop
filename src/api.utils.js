
const api = (() => {
  const BASE_URL = 'https://disease.sh/v3/covid-19/'
  const GLOBAL_URL = BASE_URL + 'all'
  const COUNTRIES_URL = BASE_URL + 'countries'

  const fetch_data = async (url) => {
    const response = await fetch(url)
    return await response.json()
  }

  const get_global_data = async () => {
    return await fetch_data(GLOBAL_URL)
  }

  const get_countries_data = async () => {
    return await fetch_data(COUNTRIES_URL)
  }

  const get_country_data = async (country) => {
    const url = COUNTRIES_URL + `/${encodeURIComponent(country.toLowerCase())}`
    return await fetch_data(url)
  }
  
  return {
    get_global_data,
    get_countries_data,
    get_country_data
  }
})()

export default api