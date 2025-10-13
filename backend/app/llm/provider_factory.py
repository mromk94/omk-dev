"""
LLM Provider Factory - Multi-LLM support
"""
import os
from typing import Optional
import structlog

logger = structlog.get_logger(__name__)


class BaseLLMProvider:
    """Base class for LLM providers"""
    
    async def generate(self, prompt: str, **kwargs) -> str:
        raise NotImplementedError


class GeminiProvider(BaseLLMProvider):
    """Google Gemini provider"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found")
    
    async def generate(self, prompt: str, **kwargs) -> str:
        """Generate response using Gemini"""
        try:
            import google.generativeai as genai
            genai.configure(api_key=self.api_key)
            
            model = genai.GenerativeModel('gemini-pro')
            response = await model.generate_content_async(prompt)
            
            return response.text
        except Exception as e:
            logger.error(f"Gemini generation failed: {e}")
            raise


class OpenAIProvider(BaseLLMProvider):
    """OpenAI GPT provider"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found")
    
    async def generate(self, prompt: str, **kwargs) -> str:
        """Generate response using GPT-4"""
        try:
            from openai import AsyncOpenAI
            client = AsyncOpenAI(api_key=self.api_key)
            
            response = await client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI generation failed: {e}")
            raise


class ClaudeProvider(BaseLLMProvider):
    """Anthropic Claude provider"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not found")
    
    async def generate(self, prompt: str, **kwargs) -> str:
        """Generate response using Claude"""
        try:
            from anthropic import AsyncAnthropic
            client = AsyncAnthropic(api_key=self.api_key)
            
            message = await client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return message.content[0].text
        except Exception as e:
            logger.error(f"Claude generation failed: {e}")
            raise


async def get_llm_provider() -> BaseLLMProvider:
    """Get LLM provider based on environment"""
    provider_name = os.getenv("DEFAULT_LLM_PROVIDER", "gemini").lower()
    
    providers = {
        "gemini": GeminiProvider,
        "openai": OpenAIProvider,
        "claude": ClaudeProvider,
        "anthropic": ClaudeProvider,
    }
    
    provider_class = providers.get(provider_name)
    if not provider_class:
        raise ValueError(f"Unknown LLM provider: {provider_name}")
    
    try:
        provider = provider_class()
        logger.info(f"✅ Initialized {provider_name} LLM provider")
        return provider
    except ValueError as e:
        # Try fallback providers
        logger.warning(f"⚠️  {provider_name} not available: {e}. Trying fallbacks...")
        
        for fallback_name, fallback_class in providers.items():
            if fallback_name == provider_name:
                continue
            try:
                provider = fallback_class()
                logger.info(f"✅ Using fallback provider: {fallback_name}")
                return provider
            except ValueError:
                continue
        
        raise RuntimeError("No LLM provider available. Please set API keys.")
