from ensurepip import bootstrap

from confluent_kafka import Producer
import json
import time

class InvoiceProducer:
    def __init__(self):
        self.topic = "invoices"
        self.conf = {
            'bootstrap.servers' : 'p..-....3.us-east1.gcp.confluent.cloud:9092',
            'security.protocol' : 'SASL_SSL',
            'sasl.mechanism' : 'PLAIN',
            'sasl.username' : '7J.........PD7',
            'sasl.password' : 'IB.........................KbW',
            'client.id' : "Tushar’s MacBook Air"
        }


    def delivery_callback(self, err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            key = msg.key().decode('utf-8')
            invoice_id = json.loads(msg.value().decode('utf-8'))["InvoiceNumber"]
            print(f"Produced event to : key = {key} value = {invoice_id}")


    def produce_invoices(self, producer, counts):
        counter = 1
        with open("data/invoices.json") as lines:
            for line in lines:
                invoice = json.loads(line)
                store_id = invoice['StoreID']
                producer.produce(self.topic, key=store_id, value=line, callback=self.delivery_callback)
                time.sleep(0.5)
                producer.poll(1)
                counter += 1
                if counter == counts:
                    break


    def start(self):
        kafka_producer = Producer(self.conf)
        self.produce_invoices(kafka_producer, 70)
        kafka_producer.flush(10)

if __name__ == '__main__':
    invoice_producer = InvoiceProducer()
    invoice_producer.start()