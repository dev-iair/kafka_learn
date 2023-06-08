FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update && apt upgrade -y && apt install -y tzdata wget openjdk-17-jdk
RUN mkdir /app
WORKDIR /app
RUN wget https://dlcdn.apache.org/kafka/3.4.0/kafka_2.13-3.4.0.tgz
RUN tar -xzf kafka_2.13-3.4.0.tgz
COPY ./data/properties/server.properties /app/kafka_2.13-3.4.0/config/kraft/server.properties
COPY ./setup.sh /app/kafka_2.13-3.4.0
COPY ./run.sh /app/kafka_2.13-3.4.0