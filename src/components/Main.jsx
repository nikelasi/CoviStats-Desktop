import '../styles/main.css'
import GlobalStats from './GlobalStats'
import CountriesStats from './CountriesStats'
import CountryStat from './CountryStat'

const Main = () => {
  return (
    <main>
      <GlobalStats/>
      <CountriesStats/>
      <CountryStat/>
    </main>
  )
}

export default Main