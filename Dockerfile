FROM python:2.7

MAINTAINER <liumengxinfly@gmail.com>

RUN apt-get update && apt-get install axel -y
RUN pip install requests
COPY * /root/workspace/
WORKDIR /root/workspace/
RUN tar zxvf oss.tar
RUN python setup.py install

CMD python downloader.py
