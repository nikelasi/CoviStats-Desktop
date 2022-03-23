import GlobalIcon from '../assets/icons/global_heading_image.png'
import api from '../api.utils'
import '../styles/global-stats.css'
import StatLabel from './StatLabel'
import useData from '../hooks/useData'

const GlobalStats = () => {
  const stats = useData(api.getGlobalData)
  const DISPLAYED_DATA = ['cases', 'active', 'recovered', 'deaths']

  return (
    <div className="global-stats">
      <div>
        <span>Global</span>
        <img src={GlobalIcon} />
      </div>
      { stats === null ? 'loading...' : DISPLAYED_DATA.map(data => 
        <StatLabel label={data} stat={stats[data].toLocaleString('en')}/>
      ) }
    </div>
  )
}

export default GlobalStats