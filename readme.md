# Flask + Celery + Redis Email Sender 🚀

A simple, Dockerized microservice project demonstrating asynchronous task processing using **Flask**, **Celery**, and **Redis**. Tasks such as sending emails are handled in the background using Celery workers.
<br>
---
<br>
### ✨ Features
Asynchronous task handling via Celery.<br>
Redis as the message broker.<br>
Fully Dockerized.<br>
Easily extendable to real production tasks.<br>
<br>
---
<br>
## 📦 Tech Stack
<br>
- **Python 3.11**<br>
- **Flask** — Web API<br>
- **Celery** — Task Queue Manager<br>
- **Redis** — Message Broker<br>
- **Docker & Docker Compose** — Containerization<br>
- **Gmail SMTP** — Email service<br>
<br>
---
<br>
## 🚧 Project Structure
.<br>
├── app.py # Flask application <br>
├── tasks.py # Celery task definition <br>
├── Dockerfile # Dockerfile for Flask/Celery<br>
├── docker-compose.yml # Multi-container setup<br>
├── .env.example # Environment variable example<br>
├── .gitignore<br>
└── README.md # Project documentation<br>
<br>
---
<br>
## ⚙️ Setup Instructions (macOS + Docker)
<br>
### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Create .env file
```bash
cp .env.example .env
```

Fill in your SMTP credentials in .env:
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password

### 3. Build & Run with Docker Compose
```bash
docker-compose up --build
```

To end and delete the container
```bash
docker-compose down
```

Press Ctrl+C to terminate the process

✔️ Services Running:
Flask app on http://localhost:5001
Redis message broker
Celery worker for tasks

### 4. Testing the API (Example):
```bash
curl -X POST http://localhost:5001/send-email \
-H "Content-Type: application/json" \
-d '{
  "to": "recipient@example.com",
  "subject": "Test Email",
  "body": "Hello from Dockerized Flask + Celery + Redis!"
}'
```

### 🔍 Verifying Redis & Celery:
Redis logs: docker logs redis-container-name

Celery logs: docker logs celery-container-name
