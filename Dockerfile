FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . .
RUN pip3 install -r requirements.txt
# Launch app
ENTRYPOINT ["python3", "main.py"]