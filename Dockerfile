FROM heroku/heroku:16

ADD . /opt
WORKDIR /opt

RUN apt-get update && apt-get install -y python3-pip libsm6

RUN pip3 install opencv-python flask tensorflow keras pillow

RUN useradd -m myuser
USER myuser

CMD python3 app.py $PORT
