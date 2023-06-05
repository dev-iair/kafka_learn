from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'kafka-first:9092,kafka-second:9092,kafka-third:9092'})

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

while True:
    user_input = input("Enter something: ")
    p.poll(0)
    p.produce('test-topic', user_input.encode('utf-8'), callback=delivery_report)
# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()