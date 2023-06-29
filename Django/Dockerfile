FROM python:3.11.4-slim-bullseye
RUN apt-get update && apt-get install build-essential -y


RUN yes | /usr/local/bin/pip --retries 10 --timeout 50 --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org install --upgrade pip
RUN yes | /usr/local/bin/pip --retries 10 --timeout 50 --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org install setuptools
RUN yes | /usr/local/bin/pip --retries 10 --timeout 50 --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org install wheel
RUN yes | /usr/local/bin/pip --retries 10 --timeout 50 --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org install django==4.2

RUN useradd ta -s /bin/bash -m 

COPY ./bashrc /home/ta/.bashrc
RUN chown -R ta:ta /home/ta && echo "ta:!xtrmAi2020" | chpasswd && chmod 755 -R /home/ta
EXPOSE 8000
USER ta
WORKDIR /home/ta

