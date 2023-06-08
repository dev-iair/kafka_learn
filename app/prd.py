from confluent_kafka import SerializingProducer, Producer
from confluent_kafka.serialization import StringSerializer
import numpy as np
import cv2, time

# p = SerializingProducer({'bootstrap.servers': 'kafka-first:9092,kafka-second:9092,kafka-third:9092',
#                          'message.max.bytes': 10000000,
#                         'value.serializer': StringSerializer()})

p = Producer({'bootstrap.servers': 'kafka-first:9092,kafka-second:9092,kafka-third:9092',
              'message.max.bytes': 10485760,})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# some_data_source = [f'{i}' for i in range(100)]

# for data in some_data_source:
#     # Trigger any available delivery report callbacks from previous produce() calls
#     p.poll(0)

#     # Asynchronously produce a message. The delivery report callback will
#     # be triggered from the call to poll() above, or flush() below, when the
#     # message has been successfully delivered or failed permanently.
#     p.produce('test-topic', data.encode('utf-8'), callback=delivery_report)
cnt = 0
while True:
    user_input = input("Enter something: ")

    # image_path = '/app/2W6A0001.jpg'
    # image = cv2.imread(image_path)
    # _, image_jpeg = cv2.imencode('.jpg', image)
    # image_bytes = np.array(image_jpeg).tobytes()

    p.poll(0)
    with open('/app/pexels-pressmaster-3209828-1920x1080-25fps.mp4', 'rb') as file:
        file_data = file.read()
        p.produce('test-topic', file_data, callback=delivery_report)
    print(f'[{time.time()}] {cnt}')
    cnt = cnt + 1
# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()