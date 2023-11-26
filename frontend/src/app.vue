<template>
  <div>
    <audio-recorder @audio-uploaded="handleAudioUploaded" />
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
