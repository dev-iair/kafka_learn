#!/bin/bash
cd /app/kafka_2.13-3.5.0
if [ ! -f "/app/data/meta.properties" ]; then
  sed -i "s|KFK_NODE_ID|${KFK_NODE_ID}|g" config/kraft/server.properties
  sed -i "s|KFK_QUORUM_VOTERS|${KFK_QUORUM_VOTERS}|g" config/kraft/server.properties
  sed -i "s|KFK_ADV_LISTENERS|${KFK_ADV_LISTENERS}|g" config/kraft/server.properties
  sed -i "s|KFK_LOG_DIRS|${KFK_LOG_DIRS}|g" config/kraft/server.properties
  bin/kafka-storage.sh format -t $KFK_CLUSTER_ID -c config/kraft/server.properties
fi
bin/kafka-server-start.sh config/kraft/server.properties