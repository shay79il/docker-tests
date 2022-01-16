FROM python:alpine
WORKDIR /app
RUN pip install Flask
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY flask_server.py /app/
CMD python flask_server.py

