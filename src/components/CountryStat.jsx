import closeIcon from '../assets/icons/x_icon.png'
import useData from '../hooks/useData'
import '../styles/country-stat.css'
import StatLabel from './StatLabel'
import api from '../api.utils'

const CountryStat = ({ country, onClose }) => {
  const DISPLAYED_DATA = ['cases', 'active', 'recovered', 'deaths']
  const stats = useData(async () => await api.getCountryData(country))

  return (
    <div className="country-stat">
      <div>
        <span><img src={closeIcon} draggable='false' onClick={onClose} /></span>
        <span>{country}</span>
      </div>
      { stats === null ? 'loading...' : DISPLAYED_DATA.map(data => 
        <StatLabel key={data} label={data} stat={stats[data].toLocaleString('en')}/>
      ) }
    </div>
  )
}

export default CountryStat