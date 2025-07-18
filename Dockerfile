# Use official Node image to build Astro frontend
FROM node:18 AS frontend

WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# Use Python image for backend
FROM python:3.10-slim AS backend

# Install backend dependencies
WORKDIR /app
COPY --from=frontend /app /app
RUN pip install --no-cache-dir -r backend/requirements.txt

# Expose FastAPI app
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]