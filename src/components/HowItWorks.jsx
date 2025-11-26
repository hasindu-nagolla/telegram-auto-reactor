export default function HowItWorks({ isDark }) {
  const emojis = ['🎉', '🔥', '😂', '😍', '🤯', '👏']

  return (
    <section className="py-16 px-4 max-w-5xl mx-auto">
      <h2
        className={`text-3xl md:text-4xl font-bold mb-6 text-center ${
          isDark ? 'text-pink-400' : 'text-pink-500'
        }`}
      >
        How It Works
      </h2>
      <p className="text-center max-w-3xl mx-auto mt-4 text-base md:text-lg opacity-85">
        Trixie listens to all messages in a chat and reacts automatically with
        fun, animated emojis. Perfect for groups that want to stay active and
        entertained without lifting a finger!
      </p>
      <div className="text-center mt-8 text-4xl">
        {emojis.map((emoji, index) => (
          <span
            key={index}
            className="inline-block mx-1 animate-bounce-custom"
            style={{ animationDelay: `${index * 0.2}s` }}
          >
            {emoji}
          </span>
        ))}
      </div>
    </section>
  )
}
