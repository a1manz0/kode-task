FROM python:3.12.4-slim

WORKDIR /app


COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD alembic revision -m "init db" && alembic upgrade head && sleep 10 && uvicorn main:app --host=0.0.0.0
