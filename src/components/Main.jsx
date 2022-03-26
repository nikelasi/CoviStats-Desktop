import '../styles/main.css'
import GlobalStats from './GlobalStats'
import CountriesStats from './CountriesStats'
import CountryStat from './CountryStat'
import { useState } from 'react'

const Main = () => {
  const [displayedCountry, setDisplayedCountry] = useState(null)

  const displayCountry = (country) => {
    setDisplayedCountry(country)
  }

  const onClose = () => {
    setDisplayedCountry(null)
  }

  return (
    <main>
      <GlobalStats/>
      <CountriesStats displayCountry={country => displayCountry(country)} />
      { displayedCountry !== null && <CountryStat country={displayedCountry} onClose={onClose} /> }
    </main>
  )
}

export default Main