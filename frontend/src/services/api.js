import axios from 'axios'

const API_BASE = 'http://localhost:5000/api'

const api = {
  async countSyllables(text) {
    const response = await axios.post(`${API_BASE}/syllables`, { text })
    return response.data
  },

  async findRhymes(word) {
    const response = await axios.post(`${API_BASE}/rhymes`, { word })
    return response.data
  },

  async detectScheme(text) {
    const response = await axios.post(`${API_BASE}/scheme`, { text })
    return response.data.scheme
  },

  async getForms() {
    const response = await axios.get(`${API_BASE}/forms`)
    return response.data
  }
}

export default api
