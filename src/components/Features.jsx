export default function Features({ isDark }) {
  const features = [
    {
      title: 'Automatic Reactions',
      description:
        'Reacts instantly to every message, making your chat more interactive and fun.',
    },
    {
      title: 'Random Emojis',
      description: 'Each reaction is unique with a wide collection of emojis!',
    },
    {
      title: 'Easy Deployment',
      description: 'Run Trixie on your local machine or VPS with tmux easily.',
    },
    {
      title: 'Lightweight',
      description:
        'Minimal resource usage ensures smooth performance without slowing down your chats.',
    },
  ]

  return (
    <section className="py-16 px-4 max-w-5xl mx-auto">
      <h2
        className={`text-3xl md:text-4xl font-bold mb-6 text-center ${
          isDark ? 'text-pink-400' : 'text-pink-500'
        }`}
      >
        Features
      </h2>
      <div className="flex flex-wrap justify-around mt-8 gap-4">
        {features.map((feature, index) => (
          <div
            key={index}
            className={`flex-1 min-w-[250px] rounded-2xl p-8 text-center transition-all duration-400 hover:-translate-y-3 hover:shadow-2xl ${
              isDark
                ? 'bg-[#1a1a2e] text-gray-200 shadow-white/5'
                : 'bg-white text-gray-900 shadow-black/5'
            }`}
          >
            <h3 className="mb-4 font-semibold text-xl">{feature.title}</h3>
            <p className="text-base opacity-85">{feature.description}</p>
          </div>
        ))}
      </div>
      <div className="text-center mt-12">
        <a
          href="https://t.me/AutoMessageReactorBot"
          target="_blank"
          rel="noopener noreferrer"
          className={`inline-block px-8 py-4 rounded-full text-xl font-semibold transition-all duration-300 hover:scale-105 ${
            isDark
              ? 'bg-pink-400 text-white'
              : 'bg-pink-500 text-white'
          }`}
        >
          Add Trixie to Your Group
        </a>
      </div>
    </section>
  )
}
