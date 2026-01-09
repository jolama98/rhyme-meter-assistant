# Rhyme & Meter Assistant

A technical toolkit for poets - helps with structure without AI-generated content.

## Quick Start

### Backend
```bash
cd backend
source venv/bin/activate
python app.py
```

Backend runs on http://localhost:5000

### Frontend
```bash
cd frontend
npm run dev
```

Frontend runs on http://localhost:5173

## Project Structure

- `backend/` - Flask API (Python)
  - `models/` - Business logic
  - `controllers/` - Route handlers
  - `data/` - CMU Dictionary, poetry forms
  
- `frontend/` - Vue.js UI
  - `src/components/` - Reusable components
  - `src/views/` - Page components
  - `src/services/` - API calls

## Features (MVP)

- [x] Project setup
- [ ] Syllable counter
- [ ] Rhyme finder
- [ ] Rhyme scheme detector
- [ ] Poetry forms library (5-10 forms)
- [ ] Save/load poems locally

## Development

Built with:
- Backend: Python 3, Flask, NLTK
- Frontend: Vue.js 3, Vite, Axios
- Database: SQLite

## License

MIT
