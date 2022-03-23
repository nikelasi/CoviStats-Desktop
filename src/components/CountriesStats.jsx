import aToZIcon from '../assets/filter_buttons/a_to_z_alphabetical_filter_icon.png'
import zToAIcon from '../assets/filter_buttons/z_to_a_alphabetical_filter_icon.png'
import ascIcon from '../assets/filter_buttons/ascending_cases_filter_icon.png'
import descIcon from '../assets/filter_buttons/descending_cases_filter_icon.png'
import searchIcon from '../assets/icons/searchbar_icon.png'
import '../styles/countries-stats.css'
import api from '../api.utils'
import { useState } from 'react'
import useData from '../hooks/useData'

const CountryEntry = ({ country, onClick }) => {
  return (
    <div className="country-entry" onClick={onClick}>
      <span>{country.name}</span>
      <span>{country.cases} cases</span>
    </div>
  )
}

const CountriesStats = () => {
  const [searchTerm, setSearchTerm] = useState('')
  const countries = useData(api.getCountries)
  let displayedCountries = null
  if (countries !== null) {
    displayedCountries = countries.filter(country => country.name.toLowerCase().includes(searchTerm.toLowerCase()))
  }
  

  return (
    <div className="countries-stats">
      <div>
        <span>Countries</span>
        <span>
          <img src={ascIcon} draggable='false' />
          <img src={descIcon} draggable='false' />
          <img src={aToZIcon} draggable='false' />
          <img src={zToAIcon} draggable='false' />
        </span>
      </div>
      <div className="search-bar">
        <img src={searchIcon} />
        <input type="text" placeholder='Search' spellCheck='false' value={searchTerm} onChange={({ target }) => setSearchTerm(target.value)} />
      </div>
      <div className="search-result">
        { countries === null ? 'loading...' :
          displayedCountries.length === 0 ? 'No countries found' : displayedCountries.map(country => 
          <CountryEntry key={country.name} country={country} onClick={() => console.log(country.name)}/>
        )}
      </div>
    </div>
  )
}

export default CountriesStats