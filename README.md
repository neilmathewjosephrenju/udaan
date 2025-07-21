# 🌐 Project Udaan - Language Translator

Project Udaan is a simple language translation microservice built using **FastAPI** for the backend and **Streamlit** for the frontend. The application is containerized using **Docker** and managed via Docker Compose

----------------------------------------------------------

## Features

- Translate text between multiple languages
- Auto language detection
- Translation stats and health checks
- Reset translation logs and database with one click
- Fully Dockerized for easy setup

----------------------------------------------------------

## Tech Stack

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Containerization**: Docker + Docker Compose
- **Language Support**: English, Hindi, Tamil, Kannada, Bengali, French, Arabic

----------------------------------------------------------

## Setup Instructions

### Things to download before running

- [Docker](https://www.docker.com/products/docker-desktop) installed and running

> ❗ You do **NOT** need to install Python or any libraries manually. Everything is containerized.

----------------------------------------------------------

# How to Run

run these commands either in vs code or in the terminal

# clone the repository
git clone https://github.com/neilmathewjosephrenju/udaan.git
cd udaan

# build and run the project
docker compose up --build
