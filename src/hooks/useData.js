import { useState, useEffect } from 'react'
const REFRESH_INTERVAL = 1000*60

const useData = (fetchFunction) => {
  const [data, setData] = useState(null)

  useEffect(() => {
    const updateData = async () => setData(await fetchFunction())
    updateData()
    const interval = setInterval(async () => await updateData(), REFRESH_INTERVAL)
    return () => clearInterval(interval)
  }, [])
  // useEffect(() => console.log(data), [data])

  return data
}

export default useData