FROM python:3.9.5

# set up location of code
WORKDIR /opt/sde/

# lets us import from folders inside /src/
ENV PYTHONPATH=/opt/sde

# install python requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# COPY our code folder to docker
COPY ../.. /opt/sde

# keep our docker container running
CMD ["tail", "-f", "/dev/null"]
