#!/bin/bash
rm -rf /app/data/*
cd /app/kafka_2.13-3.4.0
cp server-$KAFKA_SERVER_NO.properties config/kraft/server.properties
bin/kafka-storage.sh format -t Ih86aAleRGuNJuV0Tt6gew -c config/kraft/server.properties
bin/kafka-server-start.sh config/kraft/server.properties