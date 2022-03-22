import GlobalIcon from '../assets/icons/global_heading_image.png'
import api from '../api.utils'
import '../styles/global-stats.css'
import { useState, useEffect } from 'react'

const StatLabel = ({ stat, label }) => {
  return (
    <div className='stat-label'>
      <span className='stat'>{ stat }</span>
      <span className='label'>{ label }</span>
    </div>
  )
}

const GlobalStats = () => {
  const [stats, setStats] = useState(null)
  const DISPLAYED_DATA = ['cases', 'active', 'recovered', 'deaths']

  useEffect(async () => {
    setStats(await api.get_global_data())
    const interval = setInterval(async () => {
      setStats(await api.get_global_data())
    }, 1000*10)
    return () => clearInterval(interval)
  }, [])

  useEffect(() => console.log(stats), [stats])

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