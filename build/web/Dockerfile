FROM python:3.10
RUN mkdir /www
WORKDIR /www
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install ffmpeg
COPY python-api ./python-api/
COPY requirements.txt ./
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
CMD [ "python", "/www/app.py" ]