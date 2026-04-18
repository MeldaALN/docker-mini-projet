# 🚀 Docker Mini App

![Docker](https://img.shields.io/badge/Docker-✓-blue)
![Flask](https://img.shields.io/badge/Flask-API-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-DB-blue)
![Nginx](https://img.shields.io/badge/Nginx-ReverseProxy-orange)
![CI](https://img.shields.io/badge/GitHub%20Actions-CI-success) 

## Description

Projet d'application web conteneurisée avec Docker.

L'application est composée de plusieurs services :
- Nginx (frontend)
- Flask (backend API)
- PostgreSQL (base de données)

Le frontend communique avec une API qui elle-même interagit avec une base de données, le tout orchestré avec Docker Compose.

---

## Architecture

Navigateur → Nginx → Backend Flask → PostgreSQL

---

## Lancer le projet

```bash
docker compose up --build
