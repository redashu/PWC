FROM ubuntu
# required OS --and ubuntu docker image will be pulled from 
# docker hub 
MAINTAINER ashutoshh@linux.com
# image developer info its optional keyword  
RUN mkdir  /mycode
# RUN is giving us the terminal during the build process
COPY test.sh  /mycode/test.sh
# copy code from OS to new docker image 
WORKDIR /mycode
# changing directory inside docker image 
# its same like cd command in linux

CMD  ["bash","test.sh"]
# this is default parent process for my docker image 
# once you create container the script will automatically start running


