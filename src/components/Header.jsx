export default function Header({ isDark }) {
  return (
    <header
      className={`text-center py-12 px-4 relative border-b-2 ${
        isDark
          ? 'bg-gradient-to-r from-purple-900 to-purple-700 border-purple-800/20'
          : 'bg-gradient-to-r from-pink-400 to-pink-300 border-white/10'
      } text-white`}
    >
      <img
        src="https://files.catbox.moe/c7cx29.jpg"
        alt="Trixie Bot"
        className="w-36 h-36 md:w-40 md:h-40 rounded-full border-4 border-white object-cover mb-4 mx-auto transition-transform duration-300 hover:scale-110 hover:rotate-6"
      />
      <h1 className="text-4xl md:text-5xl font-bold mb-2">Trixie ⸝⸝</h1>
      <p className="text-lg md:text-xl opacity-90">
        The Ultimate Telegram Auto Reactor Bot <br />
        <strong>@AutoMessageReactorBot</strong>
      </p>
    </header>
  )
}
