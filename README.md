# OMK DEV 🛠️

> **AI-Powered Development Assistant** - Autonomous bug fixing, code analysis, and feature generation for any project

[![Python](https://img.shields.io/badge/Python-3.13-green)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-blue)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 What is OMK DEV?

OMK DEV is an autonomous AI development assistant extracted from the OMK Hive project. It can:

- 🐛 **Auto-fix bugs** by analyzing error logs and applying fixes
- 🔍 **Deep code analysis** to understand your entire codebase
- 💡 **Generate features** from natural language descriptions
- 🧪 **Validate changes** before they break your code
- 🤖 **Self-improving** - learns from your project patterns

**Use it as:**
- ☁️ Cloud service (API endpoints)
- 📦 Python package (local integration)
- 🔌 SDK for any project

## 🚀 Quick Start

### As a Cloud Service

```bash
# Call the API
curl -X POST https://omk-dev-api.run.app/analyze \
  -H "Content-Type: application/json" \
  -d '{"repo_url": "github.com/your/project", "issue": "Bug in auth flow"}'
```

### As a Python Package

```bash
pip install omk-dev
```

```python
from omk_dev import OMKDev

# Initialize
dev = OMKDev(api_key="your-llm-key")

# Analyze a bug
fix = await dev.analyze_and_fix(
    code="your_buggy_code.py",
    error="TypeError: expected string, got None"
)

print(fix.suggested_code)
```

### As a TypeScript SDK

```bash
npm install @omk/dev-sdk
```

```typescript
import { OMKDev } from '@omk/dev-sdk';

const dev = new OMKDev({ apiKey: 'your-key' });

const fix = await dev.analyzeBug({
  file: 'src/auth.ts',
  error: 'Cannot read property of undefined'
});
```

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│         Your Project                    │
│  (Python, JS, Go, anything)             │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│      OMK DEV API / SDK                  │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │   Queen Orchestrator            │   │
│  │   (AI Decision Engine)          │   │
│  └─────────────────────────────────┘   │
│           │                             │
│  ┌────────┴────────┐                    │
│  │                 │                    │
│  ▼                 ▼                    │
│ ┌──────────┐  ┌──────────┐             │
│ │Multi-LLM │  │Dev Bees  │             │
│ │ Gemini   │  │ Logic    │             │
│ │ GPT-4    │  │ Security │             │
│ │ Claude   │  │ Pattern  │             │
│ │ Grok     │  │ Maths    │             │
│ └──────────┘  └──────────┘             │
└─────────────────────────────────────────┘
```

## 🛠️ Core Features

### 1. Autonomous Bug Fixing
```python
result = await dev.fix_bug(
    error_log="TypeError at line 42",
    context="auth.py",
    test_file="test_auth.py"
)
# Returns: fixed code + explanation + tests
```

### 2. Code Analysis
```python
analysis = await dev.analyze_codebase(
    path="./src",
    focus="security vulnerabilities"
)
# Returns: issues, suggestions, severity levels
```

### 3. Feature Generation
```python
feature = await dev.generate_feature(
    description="Add user authentication with JWT",
    framework="FastAPI",
    tests=True
)
# Returns: complete implementation + tests
```

### 4. Code Review
```python
review = await dev.review_code(
    files=["auth.py", "models.py"],
    standards="PEP 8"
)
# Returns: issues, improvements, best practices
```

## 📦 Project Structure

```
omk-dev/
├── backend/              # FastAPI service
│   ├── app/
│   │   ├── api/         # API endpoints
│   │   ├── core/        # Orchestrator, analyzers, fixers
│   │   ├── llm/         # Multi-LLM abstraction
│   │   ├── bees/        # Specialized AI agents
│   │   └── utils/       # Utilities
│   ├── main.py          # FastAPI app
│   ├── requirements.txt
│   └── Dockerfile
├── sdk/
│   ├── python/          # Python SDK
│   └── typescript/      # TypeScript SDK
└── docs/                # Documentation
```

## 🚢 Deployment

### Google Cloud Run (Free Tier)

```bash
# Build and deploy
cd backend
gcloud builds submit --tag=gcr.io/YOUR_PROJECT/omk-dev
gcloud run deploy omk-dev \
  --image gcr.io/YOUR_PROJECT/omk-dev \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 512Mi \
  --cpu 1
```

**Free Tier Limits:**
- 2 million requests/month
- 360k GiB-seconds/month
- 180k vCPU-seconds/month

## 🔐 Environment Setup

```bash
# Required API keys (choose one or more)
export GEMINI_API_KEY="your-gemini-key"
export OPENAI_API_KEY="your-openai-key"
export ANTHROPIC_API_KEY="your-claude-key"
export GROK_API_KEY="your-grok-key"

# Optional
export DEFAULT_LLM_PROVIDER="gemini"  # or openai, anthropic, grok
```

## 🧪 Examples

### Fix a Bug
```python
from omk_dev import OMKDev

dev = OMKDev()

# Paste your error
error = """
Traceback (most recent call last):
  File "app.py", line 23, in process_user
    return user.email.upper()
AttributeError: 'NoneType' object has no attribute 'upper'
"""

fix = await dev.fix_bug(error_log=error, file="app.py")
print(fix.explanation)
print(fix.fixed_code)
```

### Analyze Security
```python
security_scan = await dev.analyze_security(
    path="./src",
    check_for=["sql_injection", "xss", "hardcoded_secrets"]
)

for issue in security_scan.critical:
    print(f"🚨 {issue.file}:{issue.line} - {issue.description}")
```

### Generate Tests
```python
tests = await dev.generate_tests(
    file="user_service.py",
    framework="pytest",
    coverage_target=90
)
# Writes test_user_service.py automatically
```

## 💰 Pricing

**Cloud Service:**
- **Free Tier**: 1000 requests/month
- **Pro**: $29/month - 10k requests
- **Enterprise**: Custom pricing

**Self-Hosted:**
- Free (MIT License)
- Bring your own LLM API keys

## 📚 Documentation

- [Full API Docs](./docs/api.md)
- [Python SDK Guide](./docs/python-sdk.md)
- [TypeScript SDK Guide](./docs/typescript-sdk.md)
- [Deployment Guide](./docs/deployment.md)
- [Contributing](./CONTRIBUTING.md)

## 🤝 Contributing

OMK DEV is open source! Contributions welcome.

## 📄 License

MIT License - Use it anywhere, build anything.

## 🔗 Links

- **Docs**: [omk.dev/docs](https://omk.dev/docs)
- **GitHub**: [github.com/mromk94/omk-dev](https://github.com/mromk94/omk-dev)
- **Parent Project**: [OMK Hive](https://github.com/mromk94/omakh-Hive)

---

**Built with ❤️ by the OMK Hive team**
