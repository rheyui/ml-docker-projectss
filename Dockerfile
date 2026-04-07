FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirments.txt

CMD ["python", "app.py"]