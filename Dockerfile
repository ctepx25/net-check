 FROM ubuntu:latest
 COPY ./init.sh /bin/
 COPY ./net-check.py /bin/
 RUN ln -fs /usr/share/zoneinfo/UTC /etc/localtime
 RUN apt-get update
 RUN apt-get install netcat nginx python3 python3-pip -y
 RUN pip3 install requests
 ENTRYPOINT ["init.sh"]
