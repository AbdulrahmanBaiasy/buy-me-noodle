/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],

  theme: {
    extend: {
      fontFamily: {
        palanquin: ["Palanquin", "sans-serif"],
        montserrat: ["Montserrat", "sans-serif"],
      },

      colors: {
        "primary-color": "#FA991C",
        "secondary-color": "#032539",
        fantasy: "#FBF3F2",
      },
    },
  },
  plugins: [],
};
