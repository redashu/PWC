FROM oraclelinux:8.3
MAINTAINER ashutoshh@linux.com
RUN yum  install  java-1.8.0-openjdk.x86_64     -y
RUN yum install  java-1.8.0-openjdk-devel.x86_64  -y
RUN mkdir /mydata
COPY while.java /mydata/while.java
WORKDIR /mydata
RUN javac while.java
CMD ["java","myclass"]

