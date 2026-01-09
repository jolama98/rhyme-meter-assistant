<template>
  <div class="rhyme-finder">
    <h3>Rhyme Finder</h3>
    <input
      v-model="searchWord"
      @input="findRhymes"
      placeholder="Enter a word..."
      class="rhyme-input"
    />
    <div class="rhyme-results">
      <div v-if="loading">Loading...</div>
      <div v-else-if="rhymes.length">
        <div
          v-for="rhyme in rhymes"
          :key="rhyme"
          class="rhyme-item"
          @click="$emit('insert-word', rhyme)"
        >
          {{ rhyme }}
        </div>
      </div>
      <div v-else-if="searchWord">No rhymes found</div>
    </div>
  </div>
</template>

<script>
import api from '../services/api'

export default {
  name: 'RhymeFinder',
  data() {
    return {
      searchWord: '',
      rhymes: [],
      loading: false
    }
  },
  methods: {
    async findRhymes() {
      if (!this.searchWord) {
        this.rhymes = []
        return
      }
      
      this.loading = true
      try {
        const response = await api.findRhymes(this.searchWord)
        this.rhymes = response.rhymes
      } catch (error) {
        console.error('Error finding rhymes:', error)
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.rhyme-finder {
  padding: 1rem;
}

.rhyme-input {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.rhyme-results {
  max-height: 400px;
  overflow-y: auto;
}

.rhyme-item {
  padding: 0.5rem;
  cursor: pointer;
  border-bottom: 1px solid #eee;
}

.rhyme-item:hover {
  background: #f5f5f5;
}
</style>
