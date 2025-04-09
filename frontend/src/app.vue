<template>
  <div class="app">
    <header class="app-header">
      <div class="container">
        <div class="d-flex justify-content-between align-items-center py-3">
          <div class="d-flex align-items-center">
            <div class="app-logo me-3">
              <svg width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg" class="logo-svg">
                <circle cx="18" cy="18" r="18" fill="url(#paint0_linear)" />
                <path d="M11 12C11 10.8954 11.8954 10 13 10H14C15.1046 10 16 10.8954 16 12V24C16 25.1046 15.1046 26 14 26H13C11.8954 26 11 25.1046 11 24V12Z" fill="white" />
                <path d="M18 8C18 6.89543 18.8954 6 20 6H21C22.1046 6 23 6.89543 23 8V28C23 29.1046 22.1046 30 21 30H20C18.8954 30 18 29.1046 18 28V8Z" fill="white" />
                <path d="M25 14C25 12.8954 25.8954 12 27 12H28C29.1046 12 30 12.8954 30 14V22C30 23.1046 29.1046 24 28 24H27C25.8954 24 25 23.1046 25 22V14Z" fill="white" />
                <path d="M7 16C7 14.8954 7.89543 14 9 14H9.5C10.6046 14 11.5 14.8954 11.5 16V20C11.5 21.1046 10.6046 22 9.5 22H9C7.89543 22 7 21.1046 7 20V16Z" fill="white" />
                <path d="M9 13.5L27 9M27 26.5L9 22M18 4.5V31.5" stroke="white" stroke-width="0.75" stroke-dasharray="1 2" />
                <defs>
                  <linearGradient id="paint0_linear" x1="0" y1="0" x2="36" y2="36" gradientUnits="userSpaceOnUse">
                    <stop stop-color="#2D3047" />
                    <stop offset="1" stop-color="#7986CB" />
                  </linearGradient>
                </defs>
              </svg>
            </div>
            <h1 class="app-title mb-0">AudioTopic</h1>
          </div>
          <div class="app-header-actions">
            <a href="https://github.com/alexiusstrauss/AudioTopic" target="_blank" class="app-icon-button me-3">
              <i class="bi bi-github"></i>
            </a>
            <button class="app-icon-button me-3">
              <i class="bi bi-question-circle"></i>
            </button>
            <button class="app-icon-button">
              <i class="bi bi-person-circle"></i>
            </button>
          </div>
        </div>
      </div>
    </header>
    
    <main class="app-main">
      <NuxtPage />
    </main>
    
    <footer class="app-footer">
      <div class="container">
        <div class="d-flex justify-content-between align-items-center py-3">
          <div class="app-footer-copyright">
            <small>&copy; 2025 AudioTopic</small>
          </div>
          <div class="app-footer-links">
            <a href="#" class="app-footer-link me-3">Privacidade</a>
            <a href="#" class="app-footer-link me-3">Termos</a>
            <a href="#" class="app-footer-link">Contato</a>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<style>
/* Importação de fontes */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

:root {
  /* Cores primárias */
  --primary-dark: #2D3047;   /* Azul escuro elegante */
  --primary: #3F51B5;        /* Indigo moderno */
  --primary-light: #7986CB;  /* Indigo claro */
  
  /* Cores de destaque */
  --accent: #FF4081;         /* Rosa vibrante */
  --accent-light: #FF80AB;   /* Rosa claro */
  
  /* Cores neutras */
  --neutral-dark: #37474F;   /* Cinza azulado escuro */
  --neutral: #607D8B;        /* Cinza azulado médio */
  --neutral-light: #B0BEC5;  /* Cinza azulado claro */
  --neutral-lighter: #ECEFF1; /* Cinza muito claro */
  
  /* Cores funcionais */
  --success: #4CAF50;        /* Verde */
  --warning: #FFC107;        /* Amarelo */
  --error: #F44336;          /* Vermelho */
  
  /* Cores de texto */
  --text-dark: #263238;      /* Quase preto */
  --text-medium: #546E7A;    /* Cinza médio */
  --text-light: #B0BEC5;     /* Cinza claro */
  
  /* Cores de fundo */
  --bg-light: #FAFAFA;       /* Quase branco */
  --bg-dark: #2D3047;        /* Azul escuro */
  
  /* Sombras */
  --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  
  /* Arredondamentos */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
  
  /* Transições */
  --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

body {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  color: var(--text-dark);
  background-color: var(--bg-light);
  margin: 0;
  padding: 0;
  line-height: 1.5;
}

/* Layout da aplicação */
.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-main {
  flex: 1;
  padding-top: 1rem;
  padding-bottom: 2rem;
}

/* Header */
.app-header {
  background: linear-gradient(135deg, var(--primary-dark), var(--primary));
  color: white;
  box-shadow: var(--shadow-md);
  position: sticky;
  top: 0;
  z-index: 100;
}

.app-logo {
  font-size: 28px;
  animation: pulse 3s infinite alternate;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-svg {
  width: 36px;
  height: 36px;
  animation: spin 24s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes pulse {
  0% { transform: scale(1); opacity: 0.8; }
  100% { transform: scale(1.05); opacity: 1; }
}

.app-title {
  font-size: 22px;
  font-weight: 700;
  letter-spacing: 0.5px;
  background: linear-gradient(90deg, #fff, #e0e0ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.app-icon-button {
  background: none;
  border: none;
  color: white;
  font-size: 20px;
  padding: 6px;
  cursor: pointer;
  border-radius: 50%;
  transition: var(--transition);
  width: 40px;
  height: 40px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.app-icon-button:hover {
  background-color: rgba(255, 255, 255, 0.15);
  transform: translateY(-2px);
}

/* Footer */
.app-footer {
  background-color: var(--primary-dark);
  color: var(--text-light);
  font-size: 14px;
  padding: 0.5rem 0;
}

.app-footer-link {
  color: var(--neutral-light);
  text-decoration: none;
  font-size: 14px;
  transition: var(--transition);
}

.app-footer-link:hover {
  color: white;
  text-decoration: none;
}

/* Para garantir que os inputs tenham estilo consistente */
input, select, textarea, button {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
  color: var(--text-dark);
  font-weight: 600;
  line-height: 1.2;
}

/* Estilos para scrollbar personalizada */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: var(--neutral-lighter);
}

::-webkit-scrollbar-thumb {
  background: var(--neutral-light);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: var(--neutral);
}
</style>