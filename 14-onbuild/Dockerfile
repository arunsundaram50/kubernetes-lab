FROM python:alpine

EXPOSE 8000
COPY requirements.txt .
COPY webapp.py .

RUN pip install -r requirements.txt

ONBUILD COPY db-config.json .

CMD ["uvicorn", "webapp:app", "--reload", "--host=0.0.0.0"]

