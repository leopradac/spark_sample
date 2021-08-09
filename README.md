# spark_sample

## Execute
`spark-submit main.py`
or
`python3 main.py`

## Docker Env - manual installation
`docker run -i -t ubuntu:latest /bin/bash`
`apt-get update`
`apt install -y python3-pip`
`apt install -y python3-venv`
`apt install -y vim`
`apt install -y curl`
`apt-get install -y openssh-client`
`apt-get install -y git`
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
<!-- COPY . /app -->
`pip3 install -r /app/requirements.txt`
`sudo docker ps –l`
`sudo docker commit <CONTAINER_ID> ubuntu:base`
`sudo docker run -it ubuntu:base`

# spark install:
# Java:
`sudo apt install curl mlocate default-jdk -y`
# Spark:
`curl -O https://archive.apache.org/dist/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz`
`tar xvf spark-3.1.1-bin-hadoop3.2.tgz`
`sudo mv spark-3.1.1-bin-hadoop3.2/ /opt/spark `
`vim ~/.bashrc`
    ### add
    # export SPARK_HOME=/opt/spark
    # export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
`source ~/.bashrc`
