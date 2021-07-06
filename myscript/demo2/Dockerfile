FROM openjdk
MAINTAINER ashutoshh@linux.com
RUN mkdir /code
COPY while.java /code/while.java
WORKDIR /code
# compiling the code
RUN  javac  while.java
# default parent process -- during container creation time code will
CMD ["java","myclass"]


