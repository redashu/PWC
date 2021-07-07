FROM ubuntu
MAINTAINER ashutoshh@linux.com
RUN apt update 
RUN apt install python3 python3-pip  -y
RUN pip3 install pandas  requests numpy 
RUN mkdir /test
COPY web.py /test/web.py
CMD ["/bin/bash"]

