FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3 python3-pip

COPY requirements.txt /app/
WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
