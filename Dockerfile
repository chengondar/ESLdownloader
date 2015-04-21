FROM python:2.7

MAINTAINER <liumengxinfly@gmail.com>

RUN apt-get update && apt-get install axel -y
RUN pip install requests
COPY * /root/workspace/
WORKDIR /root/workspace/
RUN tar zxvf oss.tar
RUN python setup.py install

ENV OSS_ACCESSID=cCnGVskKMCMesLye
ENV OSS_ACCESSKEY=PK9VZ6GQIHt9P0pPoBedtv7PuXBLGJ
ENV MESSAGE=个人失效AK安全同学绕行

CMD python downloader.py
