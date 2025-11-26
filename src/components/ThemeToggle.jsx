export default function ThemeToggle({ isDark, setIsDark }) {
  return (
    <div className="fixed top-4 right-4 z-50">
      <div
        className={`relative w-[60px] h-[30px] rounded-full cursor-pointer flex items-center p-1 shadow-lg transition-all duration-300 ${
          isDark ? 'bg-gray-800' : 'bg-white'
        }`}
        onClick={() => setIsDark(!isDark)}
      >
        <div
          className={`w-6 h-6 rounded-full bg-yellow-400 text-gray-900 flex items-center justify-center text-sm transition-transform duration-300 ${
            isDark ? 'translate-x-7' : 'translate-x-0'
          }`}
        >
          {isDark ? '🌙' : '☀️'}
        </div>
      </div>
    </div>
  )
}
