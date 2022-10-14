FROM ubuntu:20.04

LABEL description="SchoolSchedule"
RUN apt-get update 
RUN apt-get upgrade -y
RUN apt-get install -y python3 && apt-get install -y python3-pip
RUN apt-get install -y sqlite3

#install the requirements 
ENV requirements /Docker/requirements.txt


#Copy requirements file
COPY requirements.txt ${requirements}

#install python packeges
RUN pip3 install -r /Docker/requirements.txt

#Run useradd -ms /bin/bash user
#USER user
WORKDIR /home/code  