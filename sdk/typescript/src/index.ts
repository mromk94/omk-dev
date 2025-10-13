/**
 * OMK DEV TypeScript SDK
 * AI-powered autonomous development assistant
 */

export interface BugFixRequest {
  error_log: string;
  file_path?: string;
  code_context?: string;
  test_file?: string;
}

export interface BugFixResponse {
  success: boolean;
  fixed_code?: string;
  explanation: string;
  confidence: number;
  tests?: string;
}

export interface CodeAnalysisRequest {
  code: string;
  language?: string;
  focus?: string[];
}

export interface CodeAnalysisResponse {
  issues: Array<{
    severity: string;
    line: number;
    description: string;
    type: string;
  }>;
  suggestions: Array<{
    improvement: string;
    impact: string;
  }>;
  metrics: {
    complexity: number;
    maintainability: string;
    security_score?: number;
  };
}

export interface FeatureGenerationRequest {
  description: string;
  framework?: string;
  language?: string;
  include_tests?: boolean;
}

export interface FeatureGenerationResponse {
  code: string;
  tests?: string;
  documentation: string;
  dependencies: string[];
}

export interface OMKDevConfig {
  apiUrl?: string;
  apiKey?: string;
  timeout?: number;
}

export class OMKDev {
  private apiUrl: string;
  private apiKey?: string;
  private timeout: number;

  constructor(config: OMKDevConfig = {}) {
    this.apiUrl = config.apiUrl?.replace(/\/$/, '') || 'http://localhost:8080';
    this.apiKey = config.apiKey;
    this.timeout = config.timeout || 60000;
  }

  /**
   * Analyze and fix a bug
   */
  async fixBug(request: BugFixRequest): Promise<BugFixResponse> {
    const response = await fetch(`${this.apiUrl}/api/v1/fix-bug`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...(this.apiKey && { 'Authorization': `Bearer ${this.apiKey}` })
      },
      body: JSON.stringify(request),
      signal: AbortSignal.timeout(this.timeout)
    });

    if (!response.ok) {
      throw new Error(`API error: ${response.statusText}`);
    }

    return response.json();
  }

  /**
   * Analyze code for issues and improvements
   */
  async analyzeCode(request: CodeAnalysisRequest): Promise<CodeAnalysisResponse> {
    const response = await fetch(`${this.apiUrl}/api/v1/analyze`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...(this.apiKey && { 'Authorization': `Bearer ${this.apiKey}` })
      },
      body: JSON.stringify(request),
      signal: AbortSignal.timeout(this.timeout)
    });

    if (!response.ok) {
      throw new Error(`API error: ${response.statusText}`);
    }

    return response.json();
  }

  /**
   * Generate a feature from description
   */
  async generateFeature(request: FeatureGenerationRequest): Promise<FeatureGenerationResponse> {
    const response = await fetch(`${this.apiUrl}/api/v1/generate-feature`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...(this.apiKey && { 'Authorization': `Bearer ${this.apiKey}` })
      },
      body: JSON.stringify(request),
      signal: AbortSignal.timeout(this.timeout)
    });

    if (!response.ok) {
      throw new Error(`API error: ${response.statusText}`);
    }

    return response.json();
  }

  /**
   * Check if service is healthy
   */
  async healthCheck(): Promise<any> {
    const response = await fetch(`${this.apiUrl}/health`, {
      signal: AbortSignal.timeout(5000)
    });

    if (!response.ok) {
      throw new Error(`Health check failed: ${response.statusText}`);
    }

    return response.json();
  }
}

export default OMKDev;
