FROM oraclelinux:8.3
MAINTAINER ashutoshh@linux.com
RUN  dnf install  java-1.8.0-openjdk.x86_64  -y
RUN dnf install java-1.8.0-openjdk-devel.x86_64  -y
RUN dnf install maven -y 
RUN mkdir /javawebapp
COPY . /javawebapp/
# all data from current location where dockerfile is present
WORKDIR  /javawebapp/
RUN  mvn clean package
# this step will use maven to build a .war file 
