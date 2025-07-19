FROM node:18-bullseye as frontend
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

FROM python:3.11-slim as backend
WORKDIR /app
COPY backend backend
RUN pip install -r backend/requirements.txt

FROM node:18-bullseye as runner
WORKDIR /app
COPY --from=frontend /app .
COPY --from=backend /app/backend ./backend
EXPOSE 8080
CMD ["node", "dist/server/entry.mjs"]