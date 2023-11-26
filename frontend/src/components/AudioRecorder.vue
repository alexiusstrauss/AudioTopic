<template>
  <div class="container mt-4">
    <h1 class="mb-4">Audio Topic App</h1>

    <!-- Spinner de Carregamento -->
    <div v-if="isLoading" class="d-flex justify-content-center">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Carregando...</span>
      </div>
    </div>

    <!-- Painel com Abas -->
    <ul class="nav nav-tabs">
      <li class="nav-item">
        <a
          class="nav-link"
          :class="{ active: activeTab === 'upload' }"
          href="#"
          @click="activeTab = 'upload'"
          >Gravar e Enviar</a
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

    <!-- Resposta da API -->
    <div v-if="apiResponse" class="mt-4">
      <div class="card mb-3">
        <div class="card-body">
          <h5 class="card-title">Contexto Original</h5>
          <p class="card-text">{{ apiResponse.original_context }}</p>
        </div>
      </div>

      <div class="card mb-3" v-if="apiResponse.summary_context">
        <div class="card-body">
          <h5 class="card-title">Resumo</h5>
          <p class="card-text">{{ apiResponse.summary_context }}</p>
        </div>
      </div>

      <a
        v-if="apiResponse.mp3_summary_url"
        :href="apiResponse.mp3_summary_url"
        class="btn btn-primary"
        download
        >Download do Resumo em MP3</a
      >
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

        this.isLoading = true;
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
