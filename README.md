# HackHound

Web fuzzer with a modern UI — Vite + React frontend, FastAPI engine. Built for security researchers and pentesters who want a fuzzer that doesn't fight them.

[**Live →**](https://www.aayushman.dev/hack-hound) · [**Issues →**](https://github.com/aayushman-singh/HackHound/issues)

---

## Why

Most web fuzzers ship as command-line tools with no shared state, no UI, and brittle wordlist management. HackHound treats fuzzing as an interactive workflow — you steer it from the browser, results stream live, runs are reproducible.

## Features

- **Multi-mode fuzzing** — directories, subdomains, virtual hosts, API endpoints
- **Parameter injection** — query, body, header surfaces
- **Header manipulation** + auth bypass attempts
- **Custom payloads** + wordlist management
- **Real-time UI** — results stream as they land
- **Firebase auth** — runs scoped per user

## Stack

**Frontend** — React 18 · Vite · React Router · Axios · Firebase Auth · Lucide
**Backend** — Python 3.10 · FastAPI · Pydantic · CORS

## Quick start

```bash
git clone https://github.com/aayushman-singh/HackHound.git
cd HackHound

# Frontend deps
npm install

# Backend deps
pip install -r requirements.txt

# Run both concurrently
npm start
```

Frontend: `http://localhost:5173` · API: `http://localhost:5000` · Docs: `http://localhost:5000/docs`

## API endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| `POST` | `/fuzz` | Main fuzzing endpoint |
| `GET` | `/health` | Health check |

Full schemas at `/docs` (FastAPI auto-generated).

## Development

```bash
npm run start:frontend   # Vite dev server only
npm run start:backend    # FastAPI uvicorn only
npm start                # Both concurrently
```

## Daytona one-shot

```bash
daytona create https://github.com/aayushman-singh/HackHound
```

## Author

Built by [Aayushman Singh](https://aayushman.dev) — engineer building autonomous coding agents and security tooling. Smart India Hackathon '24 winner.

## License

MIT
