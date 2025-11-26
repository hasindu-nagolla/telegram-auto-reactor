import { useState, useEffect } from 'react'
import ThemeToggle from './components/ThemeToggle'
import Header from './components/Header'
import About from './components/About'
import Features from './components/Features'
import HowItWorks from './components/HowItWorks'
import Footer from './components/Footer'
import FloatingEmojis from './components/FloatingEmojis'

function App() {
  const [isDark, setIsDark] = useState(false)

  useEffect(() => {
    if (isDark) {
      document.documentElement.classList.add('dark')
    } else {
      document.documentElement.classList.remove('dark')
    }
  }, [isDark])

  return (
    <div className={`min-h-screen transition-all duration-400 ${
      isDark 
        ? 'bg-[#0d0d1a] text-gray-200' 
        : 'bg-gradient-to-br from-pink-50 to-blue-50 text-gray-900'
    }`}>
      <ThemeToggle isDark={isDark} setIsDark={setIsDark} />
      <FloatingEmojis />
      <Header isDark={isDark} />
      <About isDark={isDark} />
      <Features isDark={isDark} />
      <HowItWorks isDark={isDark} />
      <Footer isDark={isDark} />
    </div>
  )
}

export default App
