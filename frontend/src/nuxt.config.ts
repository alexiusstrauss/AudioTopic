// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: false },
  
  css: ["bootstrap/dist/css/bootstrap.min.css"],
  server: {
    host: process.env.HOST || "localhost",
    port: process.env.PORT || 8080,
  },  
});
