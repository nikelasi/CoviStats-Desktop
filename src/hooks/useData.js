import { useState, useEffect } from 'react'
const REFRESH_INTERVAL = 1000*60

const useData = (fetchFunction) => {
  const [data, setData] = useState(null)

  useEffect(async () => {
    setData(await fetchFunction())
    const interval = setInterval(async () => {
      setData(await fetchFunction())
    }, REFRESH_INTERVAL)
    return () => clearInterval(interval)
  }, [])
  // useEffect(() => console.log(data), [data])

  return data
}

export default useData