# docker run -i -t ubuntu:latest /bin/bash
FROM ubuntu:latest
RUN apt-get update
RUN apt install -y python3-pip
RUN apt install -y python3-venv
RUN apt install -y vim
RUN apt install -y curl
RUN apt-get install -y openssh-client
RUN apt-get install -y git
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
COPY . /app
# RUN pip3 install -r /app/requirements.txt
WORKDIR /app
CMD cd /app
CMD /bin/bash

# sudo docker ps –l
# sudo docker commit <CONTAINER_ID> ubuntu:base
# sudo docker run -it ubuntu:base

# spark install:
# Java:
# sudo apt install curl mlocate default-jdk -y
# Spark:
# curl -O https://archive.apache.org/dist/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz
# tar xvf spark-3.1.1-bin-hadoop3.2.tgz
# sudo mv spark-3.1.1-bin-hadoop3.2/ /opt/spark 
# vim ~/.bashrc
    # add
    # export SPARK_HOME=/opt/spark
    # export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
# source ~/.bashrc