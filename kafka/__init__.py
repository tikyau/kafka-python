from __future__ import absolute_import

__title__ = 'kafka'
from .version import __version__
__author__ = 'Dana Powers'
__license__ = 'Apache License 2.0'
__copyright__ = 'Copyright 2016 Dana Powers, David Arthur, and Contributors'

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())


from kafka.client_async import KafkaClient
from kafka.consumer import KafkaConsumer
from kafka.consumer.subscription_state import ConsumerRebalanceListener
from kafka.producer import KafkaProducer
from kafka.conn import BrokerConnection
from kafka.protocol import (
    create_message, create_gzip_message, create_snappy_message)
from kafka.partitioner import RoundRobinPartitioner, HashedPartitioner, Murmur2Partitioner  # TODO Murmur2Partitioner might be removable?
from kafka.structs import TopicPartition, OffsetAndMetadata
from kafka.serializer import Serializer, Deserializer


__all__ = [
    'KafkaConsumer', 'KafkaProducer', 'KafkaClient', 'BrokerConnection',
    'RoundRobinPartitioner', 'HashedPartitioner',
    'create_message', 'create_gzip_message', 'create_snappy_message',
]
