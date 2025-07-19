# Stage 1: Build Astro site
FROM node:20 AS frontend-builder
WORKDIR /app
COPY ./package.json ./package-lock.json* ./src ./public ./astro.config.mjs ./
RUN npm install
RUN npm run build

# Stage 2: Final image with FastAPI
FROM python:3.11-slim
WORKDIR /app

# Install FastAPI deps
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy FastAPI backend and built Astro site
COPY backend /app/backend
COPY --from=frontend-builder /app/dist /app/dist

# Optional: Add .env
COPY .env /app/.env

# Expose port
EXPOSE 8080

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]
