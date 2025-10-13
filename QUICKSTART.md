# OMK DEV Quick Start 🚀

## 1. Local Development

### Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your LLM API key (Gemini, OpenAI, Claude, or Grok)

# Run
python main.py
```

Visit: http://localhost:8080/docs

### Test the API
```bash
# Health check
curl http://localhost:8080/health

# Fix a bug
curl -X POST http://localhost:8080/api/v1/fix-bug \
  -H "Content-Type: application/json" \
  -d '{
    "error_log": "TypeError: expected string, got None",
    "code_context": "def process(data): return data.upper()"
  }'
```

## 2. Deploy to Google Cloud Run (FREE TIER)

### Prerequisites
- Google Cloud account
- `gcloud` CLI installed
- API keys stored in Secret Manager

### Create Secrets (one-time setup)
```bash
# Create secrets for your API keys
echo -n "YOUR_GEMINI_KEY" | gcloud secrets create gemini-api-key --data-file=-
echo -n "YOUR_OPENAI_KEY" | gcloud secrets create openai-api-key --data-file=-
echo -n "YOUR_ANTHROPIC_KEY" | gcloud secrets create anthropic-api-key --data-file=-
```

### Deploy
```bash
chmod +x deploy.sh
./deploy.sh YOUR_PROJECT_ID us-central1
```

**Free Tier Limits:**
- 2 million requests/month
- 360k GiB-seconds/month
- 180k vCPU-seconds/month

**Cost**: $0 (stays within free tier for moderate usage)

## 3. Use Python SDK

```bash
pip install ./sdk/python
```

```python
from omk_dev import OMKDev
import asyncio

async def main():
    dev = OMKDev(api_url="http://localhost:8080")
    
    # Fix a bug
    result = await dev.fix_bug(
        error_log="AttributeError: 'NoneType' object has no attribute 'email'",
        code_context="user = get_user()\nprint(user.email)"
    )
    
    print("✅ Fix:", result["explanation"])
    print("📝 Code:", result["fixed_code"])

asyncio.run(main())
```

## 4. Use TypeScript SDK

```bash
cd sdk/typescript
npm install
npm run build
```

```typescript
import OMKDev from './dist/index';

const dev = new OMKDev({
  apiUrl: 'http://localhost:8080'
});

const result = await dev.fixBug({
  error_log: "Cannot read property 'name' of undefined",
  code_context: "const user = getUser(); console.log(user.name);"
});

console.log('✅ Fix:', result.explanation);
```

## 5. Integrate into Any Project

### As API
```bash
curl -X POST https://your-omk-dev.run.app/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{"code": "def buggy(): pass", "language": "python"}'
```

### As Python Package
```python
from omk_dev import OMKDev
dev = OMKDev(api_url="https://your-omk-dev.run.app")
```

### As TypeScript Package
```typescript
import OMKDev from '@omk/dev-sdk';
const dev = new OMKDev({ apiUrl: 'https://your-omk-dev.run.app' });
```

## Next Steps

- 📚 Read [full documentation](./README.md)
- 🔧 Customize orchestrator logic
- 🐝 Add specialized bee agents
- 🌐 Connect to your projects
- 🚀 Scale with Cloud Run

---

**Need help?** Open an issue on GitHub
