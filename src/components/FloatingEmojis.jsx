import { useEffect } from 'react'

export default function FloatingEmojis() {
  const emojis = ['🎉', '🔥', '😂', '😍', '🤯', '👏', '🥳', '💯', '✨']

  useEffect(() => {
    const createEmoji = () => {
      const emoji = document.createElement('div')
      emoji.className = 'fixed pointer-events-none text-2xl md:text-4xl animate-float'
      emoji.textContent = emojis[Math.floor(Math.random() * emojis.length)]
      emoji.style.left = Math.random() * window.innerWidth + 'px'
      emoji.style.top = window.innerHeight + 'px'
      emoji.style.fontSize = 20 + Math.random() * 30 + 'px'
      document.body.appendChild(emoji)
      setTimeout(() => emoji.remove(), 6000)
    }

    const interval = setInterval(createEmoji, 800)
    return () => clearInterval(interval)
  }, [])

  return null
}
