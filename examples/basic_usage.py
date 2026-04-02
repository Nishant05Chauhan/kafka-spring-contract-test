#!/usr/bin/env python3
"""Basic usage example for kafka_spring_contract_test."""

from kafka_spring_contract_test import KafkaSpringContractTest, KafkaSpringContractTestOptions


def main() -> None:
    # Create with default options
    instance = KafkaSpringContractTest()
    result = instance.run()
    print(f"Default run: success={result.success}, data={result.data}")

    # Create with custom options
    options = KafkaSpringContractTestOptions(verbose=True)
    instance = KafkaSpringContractTest(options)
    result = instance.run()
    print(f"Verbose run: success={result.success}, data={result.data}")


if __name__ == "__main__":
    main()
