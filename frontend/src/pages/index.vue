<template>
  <div>
    <section class="hero-section">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-6 hero-content">
            <h1 class="hero-title mb-3">Transforme áudio em conteúdo valioso</h1>
            <p class="hero-description mb-4">
              Extraia insights, resuma informações e economize tempo convertendo seus arquivos de áudio em resumos precisos e úteis.
            </p>
            <div class="d-flex gap-3 hero-buttons">
              <a href="#audio-tool" class="btn-primary">
                <i class="bi bi-mic-fill me-2"></i>Comece agora
              </a>
              <a href="#como-funciona" class="btn-secondary">
                <i class="bi bi-info-circle me-2"></i>Como funciona
              </a>
            </div>
          </div>
          <div class="col-lg-6 d-none d-lg-block">
            <div class="hero-image-container">
              <img src="https://images.unsplash.com/photo-1557804506-669a67965ba0?q=80&w=2074&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Pessoa ouvindo áudio resumido" class="hero-image" />
              <div class="text-overlay">
                <div class="text-line"></div>
                <div class="text-line"></div>
                <div class="text-line"></div>
                <div class="text-line"></div>
              </div>
              <div class="sound-wave-overlay">
                <div class="wave-bar"></div>
                <div class="wave-bar"></div>
                <div class="wave-bar"></div>
                <div class="wave-bar"></div>
                <div class="wave-bar"></div>
                <div class="wave-bar"></div>
                <div class="wave-bar"></div>
              </div>
              <div class="hero-shape-1"></div>
              <div class="hero-shape-2"></div>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <section id="como-funciona" class="features-section">
      <div class="container">
        <h2 class="section-title text-center mb-5">Como funciona</h2>
        <div class="row g-4">
          <div class="col-md-4">
            <div class="feature-card">
              <div class="feature-icon">
                <i class="bi bi-upload"></i>
              </div>
              <h3 class="feature-title">Envie seu áudio</h3>
              <p class="feature-description">
                Faça upload de arquivos MP3, WAV ou grave diretamente com seu microfone.
              </p>
            </div>
          </div>
          <div class="col-md-4">
            <div class="feature-card">
              <div class="feature-icon">
                <i class="bi bi-cpu"></i>
              </div>
              <h3 class="feature-title">Processamento IA</h3>
              <p class="feature-description">
                Nossa inteligência artificial analisa e extrai as informações mais relevantes.
              </p>
            </div>
          </div>
          <div class="col-md-4">
            <div class="feature-card">
              <div class="feature-icon">
                <i class="bi bi-journal-text"></i>
              </div>
              <h3 class="feature-title">Obtenha resumos</h3>
              <p class="feature-description">
                Receba resumos precisos e objetivos em texto e áudio sintetizado.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <section id="audio-tool" class="recorder-section">
      <div class="container">
        <h2 class="section-title text-center mb-4">Comece agora mesmo</h2>
        <p class="section-description text-center mb-5">
          Envie seu arquivo de áudio ou grave diretamente usando seu microfone
        </p>
        <audio-recorder @audio-uploaded="handleAudioUploaded" />
      </div>
    </section>
  </div>
</template>

<script>
import AudioRecorder from '~/components/AudioRecorder.vue';

export default {
  components: {
    AudioRecorder
  },
  methods: {
    handleAudioUploaded(responseData) {
      this.$router.push({
        name: 'summary-context',
        params: {
          fileData: responseData
        }
      });
    }
  }
};
</script>

<style scoped>
/* Hero Section */
.hero-section {
  padding: 5rem 0 4rem;
  background: linear-gradient(180deg, var(--bg-light) 0%, var(--neutral-lighter) 100%);
  overflow: hidden;
  position: relative;
}

.hero-title {
  font-size: 2.75rem;
  font-weight: 700;
  color: var(--primary-dark);
  margin-bottom: 1.5rem;
  line-height: 1.2;
  background: linear-gradient(90deg, var(--primary-dark), var(--primary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-description {
  font-size: 1.1rem;
  color: var(--text-medium);
  max-width: 90%;
  margin-bottom: 2rem;
}

.hero-buttons {
  margin-top: 2rem;
}

.btn-primary {
  background: linear-gradient(135deg, var(--primary), var(--primary-dark));
  color: white;
  padding: 0.75rem 2rem;
  border-radius: var(--radius-md);
  text-decoration: none;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  box-shadow: var(--shadow-md);
  transition: var(--transition);
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.9);
  color: var(--primary);
  padding: 0.75rem 2rem;
  border-radius: var(--radius-md);
  text-decoration: none;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
  border: 1px solid var(--primary-light);
}

.btn-secondary:hover {
  background: white;
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}

.hero-image-container {
  position: relative;
  padding: 2rem;
}

.hero-image {
  width: 100%;
  height: auto;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  z-index: 2;
  position: relative;
}

/* Texto sobreposto animado */
.text-overlay {
  position: absolute;
  top: 25%;
  right: 10%;
  width: 40%;
  z-index: 3;
}

.text-line {
  height: 8px;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 4px;
  margin-bottom: 12px;
  opacity: 0;
  transform: translateX(20px);
  animation: textFadeInOut 5s infinite;
}

.text-line:nth-child(1) {
  width: 90%;
  animation-delay: 0s;
}

.text-line:nth-child(2) {
  width: 70%;
  animation-delay: 0.4s;
}

.text-line:nth-child(3) {
  width: 85%;
  animation-delay: 0.8s;
}

.text-line:nth-child(4) {
  width: 60%;
  animation-delay: 1.2s;
}

@keyframes textFadeInOut {
  0% {
    opacity: 0;
    transform: translateX(20px);
  }
  20% {
    opacity: 0.9;
    transform: translateX(0);
  }
  80% {
    opacity: 0.9;
    transform: translateX(0);
  }
  100% {
    opacity: 0;
    transform: translateX(-20px);
  }
}

/* Ondas sonoras animadas */
.sound-wave-overlay {
  position: absolute;
  bottom: 20%;
  left: 10%;
  display: flex;
  align-items: center;
  gap: 6px;
  height: 50px;
  z-index: 3;
}

.wave-bar {
  width: 6px;
  background-color: var(--accent);
  border-radius: 3px;
  opacity: 0.8;
  animation: waveAnimation 1.5s infinite ease-in-out alternate;
}

.wave-bar:nth-child(1) { height: 15px; animation-delay: 0s; }
.wave-bar:nth-child(2) { height: 25px; animation-delay: 0.2s; }
.wave-bar:nth-child(3) { height: 35px; animation-delay: 0.4s; }
.wave-bar:nth-child(4) { height: 45px; animation-delay: 0.6s; }
.wave-bar:nth-child(5) { height: 35px; animation-delay: 0.8s; }
.wave-bar:nth-child(6) { height: 25px; animation-delay: 1s; }
.wave-bar:nth-child(7) { height: 15px; animation-delay: 1.2s; }

@keyframes waveAnimation {
  from {
    transform: scaleY(0.5);
  }
  to {
    transform: scaleY(1.2);
  }
}

.hero-shape-1 {
  position: absolute;
  width: 200px;
  height: 200px;
  background: var(--accent);
  border-radius: 50%;
  opacity: 0.1;
  top: -30px;
  right: -30px;
  z-index: 1;
}

.hero-shape-2 {
  position: absolute;
  width: 300px;
  height: 300px;
  background: var(--primary);
  border-radius: 50%;
  opacity: 0.1;
  bottom: -50px;
  left: -100px;
  z-index: 1;
}

/* Features Section */
.features-section {
  padding: 5rem 0;
  background-color: white;
}

.section-title {
  font-size: 2.25rem;
  font-weight: 700;
  color: var(--primary-dark);
  margin-bottom: 0.5rem;
}

.section-description {
  font-size: 1.1rem;
  color: var(--text-medium);
  max-width: 700px;
  margin: 0 auto 3rem;
}

.feature-card {
  background: white;
  border-radius: var(--radius-md);
  padding: 2rem;
  height: 100%;
  transition: var(--transition);
  border: 1px solid var(--neutral-lighter);
  box-shadow: var(--shadow-sm);
  text-align: center;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-md);
  border-color: var(--primary-light);
}

.feature-icon {
  width: 70px;
  height: 70px;
  background: var(--neutral-lighter);
  border-radius: 50%;
  margin: 0 auto 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 30px;
  color: var(--primary);
  transition: var(--transition);
}

.feature-card:hover .feature-icon {
  background: var(--primary);
  color: white;
  transform: scale(1.1);
}

.feature-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: var(--primary-dark);
}

.feature-description {
  color: var(--text-medium);
  font-size: 0.95rem;
  line-height: 1.6;
}

/* Recorder Section */
.recorder-section {
  padding: 5rem 0;
  background: linear-gradient(180deg, white, var(--neutral-lighter));
}

/* Responsive adjustments */
@media (max-width: 992px) {
  .hero-title {
    font-size: 2.25rem;
  }
  
  .hero-description {
    max-width: 100%;
  }
  
  .hero-section {
    padding: 3rem 0;
  }
  
  .feature-card {
    padding: 1.5rem;
  }
  
  .section-title {
    font-size: 1.75rem;
  }
}

@media (max-width: 768px) {
  .btn-primary, .btn-secondary {
    padding: 0.6rem 1.25rem;
    font-size: 0.9rem;
  }
  
  .hero-buttons {
    flex-direction: column;
    gap: 1rem;
  }
  
  .btn-primary, .btn-secondary {
    width: 100%;
    justify-content: center;
  }
}
</style>