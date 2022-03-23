import { useState, useEffect } from 'react'

const useData = (fetchFunction) => {
  const [data, setData] = useState(null)

  useEffect(async () => {
    setData(await fetchFunction())
    const interval = setInterval(async () => {
      setData(await fetchFunction())
    }, 1000*10)
    return () => clearInterval(interval)
  }, [])
  useEffect(() => console.log(data), [data])

  return data
}

export default useData