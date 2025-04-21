from confluent_kafka import Consumer, KafkaException
import json
import time

class InvoiceProducer:
    def __init__(self):
        self.topic = ["sample_data_users"]
        self.conf = {
            'bootstrap.servers' : 'p.......3.us-east1.gcp.confluent.cloud:9092',
            'security.protocol' : 'SASL_SSL',
            'sasl.mechanism' : 'PLAIN',
            'sasl.username' : '7J..........D7',
            'sasl.password' : 'IBf......................KbW',
            'client.id' : "Tushar’s MacBook Air",
            'group.id' : "Tushar's Kafka Consumer Group",
            'auto.offset.reset' : 'earliest',
            'enable.auto.commit' : False,
            'fetch.min.bytes' : 1024
        }

    def consume_invoices(self, consumer):
        try:
            while True:
                msg = consumer.poll(1)
                time.sleep(0.5)
                if msg is None:
                    continue
                if msg.error():
                    raise KafkaException(msg.error())

                print(f"Received message key = {msg.key().decode('utf-8')}, value = {msg.value()}")
                consumer.commit(msg)

        except KafkaException as e:
            print(f"Kafka error occurred : {e}")
        except KeyboardInterrupt:
            print("Consumer interrupted by user.")
        finally:
            consumer.close()
            print("Consumer closed.")


    def start(self):
        kafka_consumer = Consumer(self.conf)
        kafka_consumer.subscribe(self.topic)
        self.consume_invoices(kafka_consumer)

if __name__ == '__main__':
    invoice_consumer = InvoiceProducer()
    invoice_consumer.start()
