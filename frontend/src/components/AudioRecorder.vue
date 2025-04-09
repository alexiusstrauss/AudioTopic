<template>
  <div class="container py-5">
    <div class="row justify-content-center">
      <div class="col-lg-10">
        <div class="audio-card mb-4">
          <div class="card-tabs">
            <button 
              class="tab-button" 
              :class="{ active: activeTab === 'record' }" 
              @click="activeTab = 'record'"
            >
              <i class="bi bi-mic-fill me-2"></i>Gravar áudio
            </button>
            <button 
              class="tab-button" 
              :class="{ active: activeTab === 'upload' }" 
              @click="activeTab = 'upload'"
            >
              <i class="bi bi-upload me-2"></i>Enviar arquivo
            </button>
          </div>

          <div class="card-content">
            <!-- Aba de Gravação -->
            <div v-if="activeTab === 'record'" class="p-4">
              <div class="d-flex flex-column align-items-center">
                <div class="recording-container mb-4">
                  <div class="recording-indicator" :class="{ 'recording': isRecording }">
                    <i class="bi" :class="isRecording ? 'bi-mic-fill' : 'bi-mic'"></i>
                    <div class="recording-waves" v-if="isRecording">
                      <span></span>
                      <span></span>
                      <span></span>
                      <span></span>
                      <span></span>
                      <span></span>
                    </div>
                  </div>
                  <div class="timer mt-3" v-if="isRecording || recordingTime > 0">
                    {{ formatTime(recordingTime) }}
                  </div>
                </div>
                
                <div class="d-flex gap-3 mb-4 w-100 justify-content-center">
                  <button v-if="!isRecording && !audioURL" class="btn-record" @click="startRecording">
                    <i class="bi bi-record-circle me-2"></i>Iniciar Gravação
                  </button>
                  <button v-if="isRecording" class="btn-stop" @click="stopRecording">
                    <i class="bi bi-stop-circle me-2"></i>Parar Gravação
                  </button>
                  <button v-if="audioURL" class="btn-reset" @click="resetRecording">
                    <i class="bi bi-arrow-counterclockwise me-2"></i>Nova Gravação
                  </button>
                </div>
                
                <div v-if="audioURL" class="mt-3 w-100">
                  <div class="audio-player">
                    <audio controls class="w-100" :src="audioURL"></audio>
                  </div>
                  <button class="btn-submit mt-4" @click="sendRecordedAudio">
                    <i class="bi bi-send-fill me-2"></i>Enviar Gravação
                  </button>
                </div>
              </div>
            </div>

            <!-- Aba de Upload -->
            <div v-if="activeTab === 'upload'" class="p-4">
              <div class="upload-container">
                <div class="file-drop-area" 
                  @dragover.prevent="onDragOver" 
                  @dragleave.prevent="onDragLeave" 
                  @drop.prevent="onFileDrop"
                  :class="{ 'is-active': isDragging }">
                  <div class="file-message">
                    <i class="bi bi-cloud-arrow-up mb-3"></i>
                    <p>Arraste e solte seu arquivo de áudio aqui</p>
                    <p class="text-smaller">ou</p>
                    <label for="audioFile" class="file-select-button">
                      Selecionar arquivo
                    </label>
                    <input
                      id="audioFile"
                      type="file"
                      @change="handleFileUpload"
                      accept=".mp3, .wav"
                      class="hidden-input"
                    />
                  </div>
                  <div v-if="audioFile" class="file-info">
                    <i class="bi bi-file-earmark-music me-2"></i>
                    <span>{{ audioFile.name }}</span>
                    <button class="file-clear-button" @click="clearFile">
                      <i class="bi bi-x-circle"></i>
                    </button>
                  </div>
                </div>
                <button class="btn-submit mt-4" @click="sendAudioFile" :disabled="!audioFile">
                  <i class="bi bi-send-fill me-2"></i>Processar Arquivo
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Área de Processamento e Resultados -->
        <div v-if="isLoading || errorMessage || apiResponse" class="results-card">
          <!-- Indicador de Carregamento -->
          <div v-if="isLoading" class="loading-container">
            <div class="loading-spinner">
              <div class="spinner"></div>
            </div>
            <p class="loading-text">Processando seu áudio...</p>
          </div>

          <!-- Mensagem de Erro -->
          <div v-if="errorMessage" class="error-message">
            <div class="error-icon">
              <i class="bi bi-exclamation-triangle-fill"></i>
            </div>
            <div class="error-content">
              <h4>Ocorreu um erro</h4>
              <p>{{ errorMessage }}</p>
            </div>
          </div>

          <!-- Sucesso e Resultados -->
          <div v-if="apiResponse && !isLoading" class="results-content">
            <div class="success-message">
              <i class="bi bi-check-circle-fill me-2"></i>
              Áudio processado com sucesso!
            </div>

            <!-- Contexto Original -->
            <div class="result-panel mb-4">
              <div class="panel-header">
                <i class="bi bi-file-text me-2"></i>
                Transcrição Original
              </div>
              <div class="panel-content">
                <p class="panel-text">{{ apiResponse.original_context }}</p>
              </div>
            </div>

            <!-- Resumo e Áudio -->
            <div v-if="apiResponse.summary_context" class="result-panel">
              <div class="panel-header">
                <i class="bi bi-journal-text me-2"></i>
                Resumo
              </div>
              <div class="panel-content">
                <p class="panel-text">{{ apiResponse.summary_context }}</p>

                <!-- Player de Áudio -->
                <div v-if="apiResponse.summary_url" class="audio-section">
                  <h6 class="audio-title"><i class="bi bi-volume-up me-2"></i>Áudio Sintetizado</h6>
                  <div class="audio-player">
                    <audio controls class="w-100" :key="apiResponse.summary_url">
                      <source :src="apiResponse.summary_url" type="audio/mpeg" />
                      Seu navegador não suporta a tag de áudio.
                    </audio>
                  </div>
                </div>
                <div v-else class="loading-audio">
                  <i class="bi bi-hourglass-split me-1"></i>
                  Carregando áudio ou áudio não disponível...
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeTab: "record",
      audioFile: null,
      apiResponse: null,
      isLoading: false,
      errorMessage: "",
      // Variáveis para gravação
      mediaRecorder: null,
      isRecording: false,
      audioChunks: [],
      audioURL: null,
      recordingTime: 0,
      timerInterval: null,
      // Variáveis para drag and drop
      isDragging: false
    };
  },
  methods: {
    // Métodos de drag and drop
    onDragOver() {
      this.isDragging = true;
    },
    
    onDragLeave() {
      this.isDragging = false;
    },
    
    onFileDrop(event) {
      this.isDragging = false;
      const files = event.dataTransfer.files;
      if (files.length && (files[0].type === 'audio/wav' || files[0].type === 'audio/mpeg')) {
        this.audioFile = files[0];
      } else {
        this.errorMessage = "Por favor, solte apenas arquivos de áudio (.mp3, .wav)";
        setTimeout(() => { this.errorMessage = ""; }, 3000);
      }
    },
    
    clearFile() {
      this.audioFile = null;
      // Limpar o input file
      const fileInput = document.getElementById('audioFile');
      if (fileInput) fileInput.value = '';
    },
    
    // Métodos de upload de arquivo
    handleFileUpload(event) {
      this.audioFile = event.target.files[0];
    },

    // Formatar o tempo de gravação
    formatTime(seconds) {
      const mins = Math.floor(seconds / 60);
      const secs = seconds % 60;
      return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    },

    // Métodos de gravação
    async startRecording() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        this.audioChunks = [];
        this.mediaRecorder = new MediaRecorder(stream);
        
        this.mediaRecorder.ondataavailable = (event) => {
          this.audioChunks.push(event.data);
        };
        
        this.mediaRecorder.onstop = () => {
          const audioBlob = new Blob(this.audioChunks, { type: 'audio/wav' });
          this.audioURL = URL.createObjectURL(audioBlob);
          this.isRecording = false;
          clearInterval(this.timerInterval);
        };
        
        this.mediaRecorder.start();
        this.isRecording = true;
        this.recordingTime = 0;
        this.timerInterval = setInterval(() => {
          this.recordingTime++;
        }, 1000);
        
      } catch (error) {
        this.errorMessage = "Erro ao acessar o microfone. Verifique as permissões.";
        console.error("Erro ao iniciar gravação:", error);
      }
    },
    
    stopRecording() {
      if (this.mediaRecorder && this.isRecording) {
        this.mediaRecorder.stop();
        // A faixa de áudio é encerrada para liberar o microfone
        this.mediaRecorder.stream.getTracks().forEach(track => track.stop());
      }
    },
    
    resetRecording() {
      this.audioURL = null;
      this.audioChunks = [];
      this.recordingTime = 0;
    },
    
    async sendRecordedAudio() {
      if (!this.audioURL) return;
      
      try {
        // Converter o Blob para um arquivo .wav
        const audioBlob = await fetch(this.audioURL).then(r => r.blob());
        const audioFile = new File([audioBlob], "recorded-audio.wav", { type: 'audio/wav' });
        
        // Enviar o arquivo
        await this.processAudioFile(audioFile);
      } catch (error) {
        this.errorMessage = "Erro ao processar o áudio gravado.";
        console.error("Erro ao enviar áudio gravado:", error);
      }
    },

    async sendAudioFile() {
      if (this.audioFile) {
        await this.processAudioFile(this.audioFile);
      } else {
        this.errorMessage = "Por favor, selecione um arquivo de áudio.";
      }
    },
    
    async processAudioFile(file) {
      let formData = new FormData();
      formData.append("audio_file", file);

      this.errorMessage = "";
      this.isLoading = true;
      this.apiResponse = null;
      
      try {
        const response = await fetch("https://api.altsystems.com.br/process-audio/", {
          method: "POST",
          body: formData,
        });

        if (!response.ok) {
          const errorResponse = await response.json();
          throw new Error(
            errorResponse.detail || "Erro ao processar a requisição."
          );
        }

        this.apiResponse = await response.json();
        console.log("Resposta da API:", this.apiResponse);
        
        // Emitir evento para o componente pai
        this.$emit('audio-uploaded', this.apiResponse);
        
      } catch (error) {
        this.errorMessage = error.message;
      } finally {
        this.isLoading = false;
      }
    }
  }
};
</script>

<style scoped>
.audio-card {
  background: white;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
  overflow: hidden;
  transition: var(--transition);
}

.card-tabs {
  display: flex;
  background: linear-gradient(to right, var(--primary-dark), var(--primary));
  padding: 1rem 1rem 0;
}

.tab-button {
  background: none;
  border: none;
  color: rgba(255, 255, 255, 0.7);
  padding: 0.75rem 1.5rem;
  font-size: 0.95rem;
  font-weight: 500;
  border-radius: var(--radius-md) var(--radius-md) 0 0;
  cursor: pointer;
  transition: var(--transition);
  display: flex;
  align-items: center;
  margin-right: 0.5rem;
}

.tab-button:hover {
  color: white;
  background-color: rgba(255, 255, 255, 0.1);
}

.tab-button.active {
  background-color: white;
  color: var(--primary);
  font-weight: 600;
}

.card-content {
  padding: 1rem;
  background-color: white;
}

/* Botões estilizados */
.btn-record, .btn-submit, .btn-stop, .btn-reset {
  padding: 0.75rem 1.5rem;
  border-radius: var(--radius-md);
  border: none;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: var(--transition);
}

.btn-record {
  background: linear-gradient(135deg, var(--primary), var(--primary-light));
  color: white;
  box-shadow: var(--shadow-sm);
}

.btn-record:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.btn-stop {
  background: linear-gradient(135deg, var(--error), #FF6B6B);
  color: white;
  box-shadow: var(--shadow-sm);
}

.btn-stop:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.btn-reset {
  background: var(--neutral-lighter);
  color: var(--neutral-dark);
  box-shadow: var(--shadow-sm);
}

.btn-reset:hover {
  background: var(--neutral-light);
  color: white;
  transform: translateY(-2px);
}

.btn-submit {
  background: linear-gradient(135deg, var(--primary), var(--primary-dark));
  color: white;
  box-shadow: var(--shadow-sm);
  width: 100%;
}

.btn-submit:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.btn-submit:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

/* Área de gravação */
.recording-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem 0;
}

.recording-indicator {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--neutral-lighter);
  border: 2px solid var(--primary-light);
  transition: var(--transition);
  position: relative;
  box-shadow: var(--shadow-sm);
}

.recording-indicator i {
  font-size: 40px;
  color: var(--primary);
  z-index: 2;
}

.recording-indicator.recording {
  background-color: rgba(255, 64, 129, 0.1);
  border-color: var(--accent);
  animation: pulse 1.5s infinite;
}

.recording-indicator.recording i {
  color: var(--accent);
}

.recording-waves {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.recording-waves span {
  display: block;
  position: absolute;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  border: 2px solid var(--accent);
  animation: waves 2s linear infinite;
  opacity: 0;
}

.recording-waves span:nth-child(1) { animation-delay: 0s; }
.recording-waves span:nth-child(2) { animation-delay: 0.3s; }
.recording-waves span:nth-child(3) { animation-delay: 0.6s; }
.recording-waves span:nth-child(4) { animation-delay: 0.9s; }
.recording-waves span:nth-child(5) { animation-delay: 1.2s; }
.recording-waves span:nth-child(6) { animation-delay: 1.5s; }

@keyframes waves {
  0% {
    transform: scale(1);
    opacity: 0.7;
  }
  100% {
    transform: scale(1.5);
    opacity: 0;
  }
}

.timer {
  font-size: 28px;
  font-weight: 700;
  font-family: 'SF Mono', 'Plus Jakarta Sans', monospace;
  color: var(--primary-dark);
  background: linear-gradient(to right, var(--primary), var(--accent));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(255, 64, 129, 0.5);
  }
  70% {
    box-shadow: 0 0 0 15px rgba(255, 64, 129, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(255, 64, 129, 0);
  }
}

/* Área de upload */
.upload-container {
  padding: 1rem 0;
}

.file-drop-area {
  border: 2px dashed var(--neutral-light);
  border-radius: var(--radius-md);
  padding: 3rem 2rem;
  text-align: center;
  transition: var(--transition);
  background-color: var(--neutral-lighter);
  position: relative;
}

.file-drop-area.is-active {
  border-color: var(--primary);
  background-color: rgba(63, 81, 181, 0.05);
}

.file-message {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: var(--text-medium);
}

.file-message i {
  font-size: 48px;
  color: var(--primary);
  margin-bottom: 1rem;
}

.file-message p {
  margin-bottom: 0.75rem;
}

.text-smaller {
  font-size: 0.85rem;
  opacity: 0.7;
}

.file-select-button {
  margin-top: 1rem;
  padding: 0.75rem 1.5rem;
  background: var(--primary);
  color: white;
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: var(--transition);
  display: inline-block;
}

.file-select-button:hover {
  background: var(--primary-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-sm);
}

.hidden-input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}

.file-info {
  margin-top: 1rem;
  padding: 0.75rem;
  background: white;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  box-shadow: var(--shadow-sm);
}

.file-info i {
  font-size: 1.2rem;
  color: var(--primary);
}

.file-info span {
  margin-left: 0.5rem;
  flex: 1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.file-clear-button {
  background: none;
  border: none;
  color: var(--neutral);
  cursor: pointer;
  transition: var(--transition);
  padding: 0.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.file-clear-button:hover {
  color: var(--error);
}

/* Audio player */
.audio-player {
  background-color: var(--neutral-lighter);
  border-radius: var(--radius-md);
  padding: 1rem;
  box-shadow: var(--shadow-sm);
}

.audio-player audio {
  width: 100%;
}

/* Resultados */
.results-card {
  background: white;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
  overflow: hidden;
  transition: var(--transition);
  padding: 1.5rem;
}

.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 3rem 0;
}

.loading-spinner {
  width: 80px;
  height: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 1.5rem;
}

.spinner {
  width: 60px;
  height: 60px;
  border: 4px solid rgba(63, 81, 181, 0.2);
  border-radius: 50%;
  border-top: 4px solid var(--primary);
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-text {
  color: var(--text-medium);
  font-size: 1.1rem;
}

.error-message {
  display: flex;
  align-items: flex-start;
  background-color: rgba(244, 67, 54, 0.1);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  margin-bottom: 1rem;
}

.error-icon {
  font-size: 2rem;
  color: var(--error);
  margin-right: 1rem;
}

.error-content h4 {
  color: var(--error);
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}

.success-message {
  background-color: rgba(76, 175, 80, 0.1);
  color: var(--success);
  padding: 1rem;
  border-radius: var(--radius-md);
  margin-bottom: 1.5rem;
  font-weight: 500;
  display: flex;
  align-items: center;
}

.result-panel {
  border: 1px solid var(--neutral-lighter);
  border-radius: var(--radius-md);
  overflow: hidden;
  margin-bottom: 1.5rem;
  box-shadow: var(--shadow-sm);
}

.panel-header {
  padding: 1rem 1.25rem;
  background: linear-gradient(to right, var(--primary-dark), var(--primary));
  color: white;
  font-weight: 600;
  display: flex;
  align-items: center;
}

.panel-content {
  padding: 1.5rem;
  background-color: white;
}

.panel-text {
  line-height: 1.6;
  color: var(--text-dark);
}

.audio-section {
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--neutral-lighter);
}

.audio-title {
  display: flex;
  align-items: center;
  color: var(--primary-dark);
  font-weight: 600;
  margin-bottom: 1rem;
}

.loading-audio {
  color: var(--text-medium);
  margin-top: 1rem;
  font-style: italic;
}

/* Responsive */
@media (max-width: 768px) {
  .card-tabs {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
  
  .tab-button {
    padding: 0.6rem 1rem;
    font-size: 0.85rem;
  }
  
  .recording-indicator {
    width: 80px;
    height: 80px;
  }
  
  .recording-indicator i {
    font-size: 30px;
  }
  
  .timer {
    font-size: 22px;
  }
  
  .file-drop-area {
    padding: 2rem 1rem;
  }
  
  .file-message i {
    font-size: 36px;
  }
  
  .panel-header {
    padding: 0.75rem 1rem;
  }
  
  .panel-content {
    padding: 1rem;
  }
}
</style>