FROM python:3.8-buster

COPY app /app
WORKDIR /app

COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "ch4.py"]