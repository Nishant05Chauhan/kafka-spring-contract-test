# kafka_spring_contract_test

Contract-test Kafka producers/consumers with schema validation and Spring Boot test helpers.

## Installation

```bash
pip install kafka_spring_contract_test
```

## Quick Start

```python
from kafka_spring_contract_test import KafkaSpringContractTest

instance = KafkaSpringContractTest()
result = instance.run()
print(result)
```

## Features

- Schema-driven message validation (JSON Schema/Avro via adapters)
- JUnit-friendly fixtures for embedded Kafka and golden messages
- Producer/consumer compatibility checks across versions
- Failure diffs that pinpoint breaking field changes
- CLI to run contract suites in pipelines

## API Reference

### `KafkaSpringContractTest`

#### Constructor

```python
KafkaSpringContractTest(options: KafkaSpringContractTestOptions | None = None)
```

#### Methods

- `run()` - Execute the main operation. Returns `KafkaSpringContractTestResult`.

## Development

```bash
# Install with dev dependencies
make install

# Run tests
make test

# Lint and type-check
make lint

# Format code
make format

# Build
make build
```

## Publishing

1. Update version in `pyproject.toml` and `src/kafka_spring_contract_test/__init__.py`
2. Create a GitHub release with tag `v0.x.0`
3. The GitHub Action will automatically publish to PyPI

## License

MIT
