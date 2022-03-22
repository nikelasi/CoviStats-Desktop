import React from 'react'
import ReactDOM from 'react-dom'
import './styles/index.css'
import App from './App'

window.addEventListener('contextmenu', event => event.preventDefault());

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
)
