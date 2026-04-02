"""Type definitions for kafka_spring_contract_test."""

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class KafkaSpringContractTestOptions:
    """Configuration options for KafkaSpringContractTest.

    Attributes:
        verbose: Enable verbose logging for debugging.
        feature_1: Configuration for: Schema-driven message validation (JSON Schema/Avro via adapters)
        feature_2: Configuration for: JUnit-friendly fixtures for embedded Kafka and golden messages
        feature_3: Configuration for: Producer/consumer compatibility checks across versions
        feature_4: Configuration for: Failure diffs that pinpoint breaking field changes
        feature_5: Configuration for: CLI to run contract suites in pipelines
    """

    verbose: bool = False
    feature_1: Optional[dict[str, Any]] = None
    feature_2: Optional[dict[str, Any]] = None
    feature_3: Optional[dict[str, Any]] = None
    feature_4: Optional[dict[str, Any]] = None
    feature_5: Optional[dict[str, Any]] = None


@dataclass
class KafkaSpringContractTestResult:
    """Result returned by KafkaSpringContractTest operations.

    Attributes:
        success: Whether the operation succeeded.
        data: The result data, if successful.
        error: Error message, if the operation failed.
    """

    success: bool
    data: Any = field(default=None)
    error: Optional[str] = None
