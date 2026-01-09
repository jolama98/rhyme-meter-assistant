<template>
  <div class="main-editor">
    <div class="editor-section">
      <TextEditor @text-changed="handleTextChange" />
    </div>
    <div class="sidebar">
      <SyllableCounter :lines="syllableData" />
      <SchemeDisplay :scheme="rhymeScheme" />
      <RhymeFinder />
      <FormBrowser />
    </div>
  </div>
</template>

<script>
import TextEditor from '../components/TextEditor.vue'
import SyllableCounter from '../components/SyllableCounter.vue'
import SchemeDisplay from '../components/SchemeDisplay.vue'
import RhymeFinder from '../components/RhymeFinder.vue'
import FormBrowser from '../components/FormBrowser.vue'
import api from '../services/api'

export default {
  name: 'MainEditor',
  components: {
    TextEditor,
    SyllableCounter,
    SchemeDisplay,
    RhymeFinder,
    FormBrowser
  },
  data() {
    return {
      syllableData: [],
      rhymeScheme: ''
    }
  },
  methods: {
    async handleTextChange(text) {
      // Debounce API calls
      clearTimeout(this.debounceTimer)
      this.debounceTimer = setTimeout(async () => {
        await this.analyzeText(text)
      }, 500)
    },
    async analyzeText(text) {
      try {
        const syllables = await api.countSyllables(text)
        this.syllableData = syllables
        
        const scheme = await api.detectScheme(text)
        this.rhymeScheme = scheme
      } catch (error) {
        console.error('Error analyzing text:', error)
      }
    }
  }
}
</script>

<style scoped>
.main-editor {
  display: flex;
  height: 100vh;
}

.editor-section {
  flex: 2;
  border-right: 1px solid #ddd;
}

.sidebar {
  flex: 1;
  overflow-y: auto;
}
</style>
