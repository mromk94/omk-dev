# OMK DEV TypeScript SDK

TypeScript/JavaScript client for OMK DEV autonomous development assistant.

## Installation

```bash
npm install @omk/dev-sdk
```

## Quick Start

```typescript
import OMKDev from '@omk/dev-sdk';

const dev = new OMKDev({
  apiUrl: 'https://omk-dev-api.run.app'
});

// Fix a bug
const result = await dev.fixBug({
  error_log: "TypeError: Cannot read property 'name' of undefined",
  code_context: "const user = getUser(); console.log(user.name);"
});

console.log(result.explanation);
console.log(result.fixed_code);
```

## Features

- 🐛 **Bug fixing** - Automatic bug analysis and fixes
- 🔍 **Code analysis** - Deep code review and suggestions
- 💡 **Feature generation** - Generate features from descriptions
- 🧪 **Test generation** - Automatic test generation

## API

### `fixBug(request: BugFixRequest): Promise<BugFixResponse>`

Analyze and fix a bug.

### `analyzeCode(request: CodeAnalysisRequest): Promise<CodeAnalysisResponse>`

Analyze code for issues and improvements.

### `generateFeature(request: FeatureGenerationRequest): Promise<FeatureGenerationResponse>`

Generate a feature from description.

### `healthCheck(): Promise<any>`

Check if service is healthy.

## Documentation

Full documentation: https://omk.dev/docs/typescript-sdk

## License

MIT
