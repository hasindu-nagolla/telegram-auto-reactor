export default function Footer({ isDark }) {
  return (
    <footer
      className={`text-center py-8 px-4 text-sm relative ${
        isDark ? 'bg-[#11111f] text-gray-400' : 'bg-gray-100 text-gray-600'
      }`}
    >
      &copy; 2025 Trixie Bot | Developed for Telegram by{' '}
      <a
        href="https://github.com/hasindu-nagolla"
        target="_blank"
        rel="noopener noreferrer"
        className="underline hover:opacity-80"
      >
        Hasindu
      </a>{' '}
      |{' '}
      <a
        href="https://t.me/AutoMessageReactorBot"
        target="_blank"
        rel="noopener noreferrer"
        className="hover:opacity-80"
      >
        @AutoMessageReactorBot
      </a>
    </footer>
  )
}
