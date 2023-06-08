from confluent_kafka import Consumer
import time

c = Consumer({
    'bootstrap.servers': 'kafka-first:9092,kafka-second:9092,kafka-third:9092',
    'group.id': 'mygroup-2',
    'auto.offset.reset': 'earliest',
    'fetch.max.bytes': 10485760
})

c.subscribe(['test-topic'])

file_name = 0

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    # print('Received message: {}'.format(len(msg.value())))
    with open(f'{file_name}_.mp4', 'wb') as file:
        file.write(msg.value())
    print(f'[{time.time()}] {file_name}')
    file_name += 1
    c.commit(msg)

c.close()