"""Custom exceptions for kafka_spring_contract_test."""

from __future__ import annotations


class KafkaSpringContractTestError(Exception):
    """Base exception for all KafkaSpringContractTest errors.

    Attributes:
        message: Human-readable error description.
        code: Optional machine-readable error code.
    """

    def __init__(self, message: str, code: str | None = None) -> None:
        super().__init__(message)
        self.code = code


class ConfigurationError(KafkaSpringContractTestError):
    """Raised when the SDK is misconfigured."""


class ValidationError(KafkaSpringContractTestError):
    """Raised when input validation fails."""


class TimeoutError(KafkaSpringContractTestError):
    """Raised when an operation exceeds its time limit."""
