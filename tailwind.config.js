/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        'poppins': ['Poppins', 'sans-serif'],
      },
      animation: {
        'bounce-custom': 'bounce-custom 2s infinite',
        'float': 'float 6s linear infinite',
      },
      keyframes: {
        'bounce-custom': {
          '0%, 20%, 50%, 80%, 100%': { transform: 'translateY(0)' },
          '40%': { transform: 'translateY(-15px)' },
          '60%': { transform: 'translateY(-8px)' },
        },
        'float': {
          '0%': { transform: 'translateY(0) rotate(0deg)', opacity: '1' },
          '100%': { transform: 'translateY(-800px) rotate(360deg)', opacity: '0' },
        },
      },
    },
  },
  plugins: [],
}
