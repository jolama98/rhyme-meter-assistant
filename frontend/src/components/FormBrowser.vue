<template>
  <div class="form-browser">
    <h3>Poetry Forms</h3>
    <div class="forms-list">
      <div
        v-for="form in forms"
        :key="form.id"
        class="form-item"
        @click="selectForm(form)"
      >
        <h4>{{ form.name }}</h4>
        <p>{{ form.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../services/api'

export default {
  name: 'FormBrowser',
  data() {
    return {
      forms: []
    }
  },
  async mounted() {
    await this.loadForms()
  },
  methods: {
    async loadForms() {
      try {
        const response = await api.getForms()
        this.forms = response.forms
      } catch (error) {
        console.error('Error loading forms:', error)
      }
    },
    selectForm(form) {
      this.$emit('form-selected', form)
    }
  }
}
</script>

<style scoped>
.form-browser {
  padding: 1rem;
}

.forms-list {
  margin-top: 1rem;
}

.form-item {
  padding: 1rem;
  margin-bottom: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  cursor: pointer;
}

.form-item:hover {
  background: #f5f5f5;
}

.form-item h4 {
  margin: 0 0 0.5rem 0;
}

.form-item p {
  margin: 0;
  color: #666;
  font-size: 0.9rem;
}
</style>
