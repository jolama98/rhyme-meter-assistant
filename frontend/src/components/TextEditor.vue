<template>
  <div class="text-editor">
    <div class="editor-header">
      <h2>Poetry Editor</h2>
    </div>
    <div class="editor-container">
      <div class="line-numbers">
        <div v-for="n in lineCount" :key="n" class="line-number">{{ n }}</div>
      </div>
      <textarea
        v-model="content"
        @input="handleInput"
        placeholder="Start writing your poem..."
        class="editor-textarea"
      ></textarea>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TextEditor',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    lineCount() {
      return this.content.split('\n').length
    }
  },
  methods: {
    handleInput() {
      this.$emit('text-changed', this.content)
    }
  }
}
</script>

<style scoped>
.text-editor {
  width: 100%;
  height: 100%;
}

.editor-header {
  padding: 1rem;
  border-bottom: 1px solid #ddd;
}

.editor-container {
  display: flex;
  height: calc(100% - 60px);
}

.line-numbers {
  background: #f5f5f5;
  padding: 1rem 0.5rem;
  text-align: right;
  user-select: none;
  min-width: 40px;
}

.line-number {
  font-family: monospace;
  color: #999;
  line-height: 1.5;
}

.editor-textarea {
  flex: 1;
  padding: 1rem;
  border: none;
  font-family: monospace;
  font-size: 16px;
  line-height: 1.5;
  resize: none;
  outline: none;
}
</style>
