FROM python:3.8

WORKDIR /opt/app

COPY main.py ./
COPY config.yaml ./
COPY requirements.txt ./

RUN pip install -r ./requirements.txt

CMD ["python", "-u", "main.py"]