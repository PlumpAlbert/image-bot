FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV KEY_ID ${KEY_ID}
ENV KEY_SECRET ${KEY_SECRET}
ENV KEY_TG ${KEY_TG}
ENV KEY_OLLAMA ${KEY_OLLAMA}
ENV OLLAMA_HOST ${OLLAMA_HOST}
ENV TELEGRAM_CHAT ${TELEGRAM_CHAT}
WORKDIR /app
COPY requirements.txt requirements.txt
RUN python3 -m venv .venv
RUN source .venv/bin/activate
RUN pip install -r requirements.txt
COPY *.py ./
CMD ["python3", "main.py"]
