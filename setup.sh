#!/bin/bash
rm -rf /app/data/*
cd /app/kafka_2.13-3.4.0
sed -i "s|KFK_NODE_ID|${KFK_NODE_ID}|g" config/kraft/server.properties
sed -i "s|KFK_QUORUM_VOTERS|${KFK_QUORUM_VOTERS}|g" config/kraft/server.properties
sed -i "s|KFK_ADV_LISTENERS|${KFK_ADV_LISTENERS}|g" config/kraft/server.properties
sed -i "s|KFK_LOG_DIRS|${KFK_LOG_DIRS}|g" config/kraft/server.properties
bin/kafka-storage.sh format -t $KFK_CLUSTER_ID -c config/kraft/server.properties
bin/kafka-server-start.sh config/kraft/server.properties