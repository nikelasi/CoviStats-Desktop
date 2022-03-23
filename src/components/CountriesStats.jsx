import aToZIcon from '../assets/filter_buttons/a_to_z_alphabetical_filter_icon.png'
import zToAIcon from '../assets/filter_buttons/z_to_a_alphabetical_filter_icon.png'
import ascIcon from '../assets/filter_buttons/ascending_cases_filter_icon.png'
import descIcon from '../assets/filter_buttons/descending_cases_filter_icon.png'
import searchIcon from '../assets/icons/searchbar_icon.png'
import '../styles/countries-stats.css'
import api from '../api.utils'
import { useState, useEffect} from 'react'

const CountryEntry = () => {
  return (
    <div className="country-entry">

    </div>
  )
}

const CountriesStats = () => {
  const [searchTerm, setSearchTerm] = useState('')
  const [countries, setCountries] = useState(null)

  useEffect(async () => {
    setCountries(await api.get_countries())
    const interval = setInterval(async () => {
      setCountries(await api.get_countries())
    }, 1000*10)
    return () => clearInterval(interval)
  }, [])

  useEffect(() => console.log(countries), [countries])

  return (
    <div className="countries-stats">
      <div>
        <span>Countries</span>
        <span>
          <img src={ascIcon} />
          <img src={descIcon} />
          <img src={aToZIcon} />
          <img src={zToAIcon} />
        </span>
      </div>
      <div className="search-bar">
        <img src={searchIcon} />
        <input type="text" placeholder='Search' spellCheck='false' value={searchTerm} onChange={({ target }) => setSearchTerm(target.value)} />
      </div>
    </div>
  )
}

export default CountriesStats