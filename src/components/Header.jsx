import '../styles/header.css'
import titlebar_icon from '../assets/icons/titlebar_icon.svg'
import { appWindow } from '@tauri-apps/api/window'

const Header = () => {
  return (
    <header data-tauri-drag-region>
      <div data-tauri-drag-region className="left">
        CoviStats
        <img data-tauri-drag-region src={titlebar_icon} />
      </div>
      <div data-tauri-drag-region className="right">
        <span onClick={() => appWindow.minimize()}>🗕</span>
        <span onClick={() => appWindow.toggleMaximize()}>🗖</span>
        <span onClick={() => appWindow.close()}>✕</span>
      </div>
    </header>
  )
}

export default Header