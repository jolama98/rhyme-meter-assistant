<template>
  <div id="app">
    <header class="app-header">
      <h1>Rhyme & Meter Assistant</h1>
    </header>
    <MainEditor />
  </div>
</template>

<script>
import MainEditor from './views/MainEditor.vue'

export default {
  name: 'App',
  components: {
    MainEditor
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-header {
  background: #2c3e50;
  color: white;
  padding: 1rem 2rem;
}

.app-header h1 {
  font-size: 1.5rem;
}
</style>
