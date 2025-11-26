export default function About({ isDark }) {
  return (
    <section className="py-16 px-4 max-w-5xl mx-auto">
      <h2
        className={`text-3xl md:text-4xl font-bold mb-6 text-center ${
          isDark ? 'text-pink-400' : 'text-pink-500'
        }`}
      >
        About Trixie
      </h2>
      <p className="text-center max-w-3xl mx-auto mt-4 text-base md:text-lg opacity-85">
        Trixie is a smart Telegram bot that automatically reacts to every
        message in your groups or private chats using a variety of fun emojis.
        It keeps conversations lively, engaging, and full of surprises!
      </p>
    </section>
  )
}
