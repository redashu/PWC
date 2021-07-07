FROM python
# we are gonna pull image of python from docker hub 
MAINTAINER  ashutoshh@linux.com
RUN mkdir /code
COPY task1.py  /code/task1.py

