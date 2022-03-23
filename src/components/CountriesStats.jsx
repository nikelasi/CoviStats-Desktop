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
      <span>{country.cases.toLocaleString('en')} cases</span>
    </div>
  )
}

const CountriesStats = () => {
  const [searchTerm, setSearchTerm] = useState('')
  const [sort, setSort] = useState('aToZ')
  const countries = useData(api.getCountries)
  let displayedCountries = null
  if (countries !== null) {
    displayedCountries = countries.filter(country => country.name.toLowerCase().includes(searchTerm.toLowerCase()))
    switch (sort) {
      case 'aToZ':
        displayedCountries = displayedCountries.sort(({ name: n1 }, { name: n2 }) => (n1 < n2) ? -1 : (n1 > n2) ? 1 : 0)
        break;
      case 'zToA':
        displayedCountries = displayedCountries.sort(({ name: n1 }, { name: n2 }) => (n1 < n2) ? 1 : (n1 > n2) ? -1 : 0)
        break;
      case 'asc':
        displayedCountries = displayedCountries.sort(({ cases: c1 }, { cases: c2 }) => c1 - c2)
        break;
      case 'desc':
        displayedCountries = displayedCountries.sort(({ cases: c1 }, { cases: c2 }) => c2 - c1)
    }
  }
  

  return (
    <div className="countries-stats">
      <div>
        <span>Countries</span>
        <span>
          <img src={ascIcon} draggable='false' onClick={() => setSort('asc')} />
          <img src={descIcon} draggable='false' onClick={() => setSort('desc')} />
          <img src={aToZIcon} draggable='false' onClick={() => setSort('aToZ')} />
          <img src={zToAIcon} draggable='false' onClick={() => setSort('zToA')} />
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