# AI News Gopher – Full Stack Deployment

This project combines:

- ✅ Astro frontend with working blog and layout
- ✅ FastAPI backend for serving AI news data
- ✅ Fly.io + Docker deployment for simple, scalable hosting

---

## 🔧 Local Setup

1. **Unzip this project**  
   You should see folders like `src/`, `backend/`, and files like `Dockerfile`, `fly.toml`.

2. **Initialize Git (if pushing to GitHub)**:
   ```bash
   git init
   git remote add origin https://github.com/YOUR_USERNAME/ai-news-gopher.git
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

---

## 🐳 Requirements

- [Docker](https://www.docker.com/products/docker-desktop)
- [Fly CLI](https://fly.io/docs/hands-on/install-flyctl/)
- Git + GitHub account

---

## 🚀 Deploying to Fly.io

1. **Authenticate & launch**
   ```bash
   fly auth login
   fly launch
   ```

   Accept default `tobori` app name, or change as needed.

2. **Deploy**
   ```bash
   fly deploy
   ```

Your blog + API will be live on your Fly.io domain!

---

## 🧪 Testing

- Blog: `https://your-app.fly.dev/blog/keeping-up-with-ai-news`
- API: `https://your-app.fly.dev/api/articles/today`

---

## 📦 Structure Overview

```
ai-news-gopher/
├── src/            ← Astro blog (unchanged from working version)
├── backend/        ← FastAPI backend
├── public/         ← Static assets (images, favicon)
├── Dockerfile      ← Unified deploy config
├── fly.toml        ← Fly.io deployment config
```