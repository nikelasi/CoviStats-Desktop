import '../styles/stat-label.css'

const StatLabel = ({ stat, label }) => {
  return (
    <div className='stat-label'>
      <span className='stat'>{ stat }</span>
      <span className='label'>{ label }</span>
    </div>
  )
}

export default StatLabel