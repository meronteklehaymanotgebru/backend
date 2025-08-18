// tailwind.config.js
const defaultTheme = require('tailwindcss/defaultTheme');

module.exports = {
  content: [
    './templates/**/*.html',
    './catalogue/templates/**/*.html',
    './cart/templates/**/*.html'
  ],
  theme: {
    extend: {
      fontFamily: {
        poppins: ['Poppins', ...defaultTheme.fontFamily.sans],
      },
      colors: {
        primary: '#6366F1', 
        accent: '#06B6D4',
      },
    },
  },
  plugins: [],
};
