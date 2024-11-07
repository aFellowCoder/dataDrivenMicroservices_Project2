FROM python:3.8-slim-buster

WORKDIR /app
COPY . /app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -r requirements.txt

EXPOSE 50051

CMD ["python", "data_stream_server.py"]
