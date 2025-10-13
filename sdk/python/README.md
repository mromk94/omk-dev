# OMK DEV Python SDK

Python client for OMK DEV autonomous development assistant.

## Installation

```bash
pip install omk-dev
```

## Quick Start

### Async Usage

```python
from omk_dev import OMKDev

async def main():
    async with OMKDev(api_url="https://omk-dev-api.run.app") as dev:
        # Fix a bug
        result = await dev.fix_bug(
            error_log="TypeError: 'NoneType' object has no attribute 'upper'",
            code_context="def process(user): return user.email.upper()"
        )
        
        print(result["explanation"])
        print(result["fixed_code"])

import asyncio
asyncio.run(main())
```

### Sync Usage

```python
from omk_dev import OMKDevSync

dev = OMKDevSync(api_url="https://omk-dev-api.run.app")

# Fix a bug
result = dev.fix_bug(
    error_log="TypeError: expected string",
    file_path="app.py"
)

print(result)
```

## Features

- 🐛 **Bug fixing** - Automatic bug analysis and fixes
- 🔍 **Code analysis** - Deep code review and suggestions
- 💡 **Feature generation** - Generate features from descriptions
- 🧪 **Test generation** - Automatic test generation

## Documentation

Full documentation: https://omk.dev/docs/python-sdk

## License

MIT
