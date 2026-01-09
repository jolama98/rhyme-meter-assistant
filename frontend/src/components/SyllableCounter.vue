<template>
  <div class="syllable-counter">
    <h3>Syllable Count</h3>
    <div class="line-counts">
      <div v-for="(line, index) in lines" :key="index" class="line-count">
        Line {{ index + 1 }}: {{ line.syllables }} syllables
      </div>
    </div>
    <div class="total-count">
      Total: {{ totalSyllables }} syllables
    </div>
  </div>
</template>

<script>
export default {
  name: 'SyllableCounter',
  props: {
    lines: {
      type: Array,
      default: () => []
    }
  },
  computed: {
    totalSyllables() {
      return this.lines.reduce((sum, line) => sum + line.syllables, 0)
    }
  }
}
</script>

<style scoped>
.syllable-counter {
  padding: 1rem;
}

.line-counts {
  margin: 1rem 0;
}

.line-count {
  padding: 0.25rem 0;
  font-family: monospace;
}

.total-count {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 2px solid #333;
  font-weight: bold;
}
</style>
