# Project Udaan - Language Translator

Project Udaan is a simple language translation microservice built using **FastAPI** for the backend and **Streamlit** for the frontend. The application is fully containerized using **Docker** and managed via **Docker Compose**.

---

## Features

- Translate text between multiple languages
- Auto-detect source language
- View translation statistics per language
- View and download logs of past translations
- Reset the database and logs from the frontend or API
- Fully Dockerized — no manual setup needed

---

## Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** Streamlit
- **Database:** SQLite
- **Translation Engine:** `deep_translator` (Google Translate)
- **Containerization:** Docker & Docker Compose
- **Language Support:** English, Hindi, Tamil, Kannada, Bengali, French, Arabic (and more)

---

## Setup Instructions

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running
- Internet access for translation API calls

> No need to install Python or any libraries manually — everything runs in containers.

---

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/neilmathewjosephrenju/udaan.git
cd udaan

# 2. Build and run the project
docker compose up --build


