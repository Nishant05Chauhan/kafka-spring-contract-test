"""
kafka_spring_contract_test - Contract-test Kafka producers/consumers with schema validation and Spring Boot test helpers.
"""

__version__ = "0.1.0"

from .schemadriven_message_validatio import KafkaSpringContractTest
from .types import KafkaSpringContractTestOptions, KafkaSpringContractTestResult
from .exceptions import KafkaSpringContractTestError, ConfigurationError, ValidationError

__all__ = [
    "KafkaSpringContractTest",
    "KafkaSpringContractTestOptions",
    "KafkaSpringContractTestResult",
    "KafkaSpringContractTestError",
    "ConfigurationError",
    "ValidationError",
]
