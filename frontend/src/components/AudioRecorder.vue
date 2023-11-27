<template>
  <div class="container mt-4">
    <h1 class="mb-4">Audio Topic App</h1>

    <!-- Painel com Abas -->
    <ul class="nav nav-tabs">
      <li class="nav-item">
        <a
          class="nav-link"
          :class="{ active: activeTab === 'upload' }"
          href="#"
          @click="activeTab = 'upload'"
          >Enviar audio</a
        >
      </li>
    </ul>

    <!-- Formulário de Upload -->
    <div class="tab-content p-3" v-if="activeTab === 'upload'">
      <input
        class="form-control mb-2"
        type="file"
        @change="handleFileUpload"
        accept=".mp3, .wav"
      />
      <button
        class="btn btn-success"
        @click="sendAudioFile"
        :disabled="!audioFile"
      >
        Enviar Arquivo
      </button>
    </div>

    <div class="container">
      <!-- Mensagem de Processamento -->
      <div v-if="isLoading" class="alert alert-info">
        Processando seu áudio...
      </div>

      <!-- Mensagem de Erro -->
      <div v-if="errorMessage" class="alert alert-danger">
        {{ errorMessage }}
      </div>    
    
      <!-- Spinner de Carregamento -->
      <div v-if="isLoading" class="d-flex justify-content-center">
        <div class="spinner-border" role="status">
          <span class="visually-hidden">Carregando...</span>
        </div>
      </div>

      <!-- Mensagem de Erro -->
      <div v-if="apiResponse" class="alert alert-success">
        Audio carregado com sucesso
      </div>   

      <!-- Resposta da API -->
      <div v-if="apiResponse" class="mt-4">
        <div class="card mb-3">
          <div class="card-body">
            <h5 class="card-title">Contexto Original</h5>
            <p class="card-text">{{ apiResponse.original_context }}</p>
          </div>
        </div>

        <!-- Div para o Resumo e Reprodução do Áudio -->
        <div v-if="apiResponse.summary_context" class="card mb-3">
          <div class="card-body">
            <h5 class="card-title">Resumo</h5>
            <p class="card-text">{{ apiResponse.summary_context }}</p>

            <!-- Player de Áudio -->
            <div v-if="apiResponse.summary_url">
              <audio controls :key="apiResponse.summary_url">
                <source
                  :src="apiResponse.summary_url"
                  type="audio/mpeg"
                />
                Seu navegador não suporta a tag de áudio.
              </audio>
            </div>
            <div v-else>Carregando áudio ou áudio não disponível...</div>
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
      activeTab: "upload", // Controle de qual aba está ativa
      audioFile: null, // O arquivo de áudio selecionado
      apiResponse: null, // Resposta da API
      isLoading: false,
      showToast: false,
      errorMessage: "",
      relativeUrl: "",
    };
  },
  methods: {
    handleFileUpload(event) {
      this.audioFile = event.target.files[0];
    },

    showAndAutoHideToast() {
      this.showToast = true;
      setTimeout(() => {
        this.showToast = false;
      }, 5000);
    },

    hideToast() {
      this.showToast = false;
    },

    async sendAudioFile() {
      if (this.audioFile) {
        let formData = new FormData();
        formData.append("audio_file", this.audioFile);

        this.errorMessage = "";
        this.isLoading = true;
        this.apiResponse = null;
        try {
          const response = await fetch("http://localhost:8000/process-audio/", {
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
        } catch (error) {
          this.errorMessage = error.message;
        } finally {
          this.isLoading = false;
        }
      } else {
        console.error("Nenhum arquivo selecionado para enviar.");
      }
    },
  },
};
</script>

<style>
.block-ui {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}
</style>
