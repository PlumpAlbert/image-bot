FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ARG KEY_ID
ARG KEY_SECRET
ARG KEY_TG
ARG KEY_OLLAMA
ARG OLLAMA_HOST
ARG TELEGRAM_CHAT
WORKDIR /app
COPY requirements.txt requirements.txt
RUN python3 -m venv .venv
RUN source .venv/bin/activate
RUN pip install -r requirements.txt
COPY *.py ./
CMD ["python3", "main.py"]
