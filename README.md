# KafkaPythonClient

This repository contains a self-learning project demonstrating how to implement **Kafka producers and consumers in Python**, using **Confluent Cloud** as the managed Kafka service.

## Overview

The goal of this project is to understand and implement the end-to-end workflow of producing and consuming messages to/from a Kafka topic using Python clients. This includes:

- Setting up topics in Confluent Cloud
- Producing messages using a Python Kafka producer
- Consuming messages using a Python Kafka consumer
- Understanding key configurations for security and performance

## Tech Stack

- **Language:** Python 3.x  
- **Kafka Provider:** Confluent Cloud  
- **Library:** [`confluent-kafka`](https://github.com/confluentinc/confluent-kafka-python)

## Features

- Kafka Producer that sends JSON-encoded messages to a Confluent Cloud topic
- Kafka Consumer that reads and prints messages from the same topic
- Secure connection using SASL/SSL authentication with Confluent Cloud
- Configurable topic name, key, and message payload

## Prerequisites

- Python 3.7 or above
- An active [Confluent Cloud](https://www.confluent.io/cloud/) account
- Kafka API key and secret from Confluent Cloud
- `confluent-kafka` Python package:
  ```bash
  pip install confluent-kafka
  ```
