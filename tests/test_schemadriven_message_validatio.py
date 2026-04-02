"""Tests for kafka_spring_contract_test."""

from kafka_spring_contract_test import KafkaSpringContractTest, KafkaSpringContractTestOptions


class TestKafkaSpringContractTest:
    def test_create_instance_with_defaults(self) -> None:
        instance = KafkaSpringContractTest()
        assert instance is not None

    def test_create_instance_with_options(self) -> None:
        options = KafkaSpringContractTestOptions(verbose=True)
        instance = KafkaSpringContractTest(options)
        assert instance.options.verbose is True

    def test_run_successfully(self) -> None:
        instance = KafkaSpringContractTest()
        result = instance.run()
        assert result.success is True
        assert result.data is not None

    def test_run_returns_result_type(self) -> None:
        instance = KafkaSpringContractTest()
        result = instance.run()
        assert result.error is None
