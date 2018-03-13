FROM heroku/heroku:16

ADD . /opt
WORKDIR /opt

RUN apt-get update && apt-get install -y python3-pip libsm6

#RUN pip3 install opencv-python flask keras numpy pillow tensorflow
#
#RUN useradd -m myuser
#USER myuser
#
#CMD python3 app.py $PORT

# Install dependencies
ADD ./requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Add our code
#ADD ./webapp /opt/webapp/
#WORKDIR /opt/webapp


# Run the image as a non-root user
RUN useradd -m myuser
USER myuser

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
CMD gunicorn --bind 0.0.0.0:$PORT wsgi