
FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y freecad && \
    rm -rf /var/lib/apt/lists/*

COPY create_model.py /app/create_model.py
WORKDIR /app

CMD ["freecadcmd", "create_model_class.py"]
