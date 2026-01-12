<template>
  <div class="scheme-display">
    <h3>Rhyme Scheme</h3>
    <div class="scheme-pattern " > 
      {{ scheme || 'Type to detect rhyme scheme' }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'SchemeDisplay',
  props: {
    scheme: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped>
.scheme-display {
  padding: 1rem;
}

.scheme-pattern {
  font-size: 1.5rem;
  font-weight: bold;
  font-family: monospace;
  padding: 1rem;
  background: #9e9b9b;
  border-radius: 4px;
  text-align: center;
}
</style>
