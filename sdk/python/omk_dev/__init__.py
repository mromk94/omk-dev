"""
OMK DEV Python SDK
"""
from typing import Optional, List, Dict
import httpx
import asyncio


class OMKDev:
    """
    OMK DEV Client - Python SDK for autonomous development assistance
    
    Usage:
        dev = OMKDev(api_url="https://omk-dev-api.run.app")
        result = await dev.fix_bug(error_log="...", code="...")
    """
    
    def __init__(
        self,
        api_url: str = "http://localhost:8080",
        api_key: Optional[str] = None,
        timeout: int = 60
    ):
        self.api_url = api_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout
        self.client = httpx.AsyncClient(timeout=timeout)
    
    async def fix_bug(
        self,
        error_log: str,
        file_path: Optional[str] = None,
        code_context: Optional[str] = None,
        test_file: Optional[str] = None
    ) -> Dict:
        """
        Analyze and fix a bug
        
        Args:
            error_log: Error message/traceback
            file_path: Path to the file with the bug
            code_context: Surrounding code context
            test_file: Path to test file
        
        Returns:
            Dict with fixed_code, explanation, confidence, tests
        """
        payload = {
            "error_log": error_log,
            "file_path": file_path,
            "code_context": code_context,
            "test_file": test_file
        }
        
        response = await self.client.post(
            f"{self.api_url}/api/v1/fix-bug",
            json=payload
        )
        response.raise_for_status()
        return response.json()
    
    async def analyze_code(
        self,
        code: str,
        language: str = "python",
        focus: Optional[List[str]] = None
    ) -> Dict:
        """
        Analyze code for issues and improvements
        
        Args:
            code: Code to analyze
            language: Programming language
            focus: Specific areas to focus on (e.g., ["security", "performance"])
        
        Returns:
            Dict with issues, suggestions, metrics
        """
        payload = {
            "code": code,
            "language": language,
            "focus": focus
        }
        
        response = await self.client.post(
            f"{self.api_url}/api/v1/analyze",
            json=payload
        )
        response.raise_for_status()
        return response.json()
    
    async def generate_feature(
        self,
        description: str,
        framework: Optional[str] = None,
        language: str = "python",
        include_tests: bool = True
    ) -> Dict:
        """
        Generate a feature from description
        
        Args:
            description: Feature description
            framework: Framework to use (e.g., "FastAPI", "React")
            language: Programming language
            include_tests: Whether to include tests
        
        Returns:
            Dict with code, tests, documentation, dependencies
        """
        payload = {
            "description": description,
            "framework": framework,
            "language": language,
            "include_tests": include_tests
        }
        
        response = await self.client.post(
            f"{self.api_url}/api/v1/generate-feature",
            json=payload
        )
        response.raise_for_status()
        return response.json()
    
    async def health_check(self) -> Dict:
        """Check if service is healthy"""
        response = await self.client.get(f"{self.api_url}/health")
        response.raise_for_status()
        return response.json()
    
    async def close(self):
        """Close the HTTP client"""
        await self.client.aclose()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


# Convenience synchronous wrapper
class OMKDevSync:
    """Synchronous wrapper for OMKDev"""
    
    def __init__(self, *args, **kwargs):
        self.async_client = OMKDev(*args, **kwargs)
    
    def fix_bug(self, *args, **kwargs):
        return asyncio.run(self.async_client.fix_bug(*args, **kwargs))
    
    def analyze_code(self, *args, **kwargs):
        return asyncio.run(self.async_client.analyze_code(*args, **kwargs))
    
    def generate_feature(self, *args, **kwargs):
        return asyncio.run(self.async_client.generate_feature(*args, **kwargs))
    
    def health_check(self):
        return asyncio.run(self.async_client.health_check())


__all__ = ["OMKDev", "OMKDevSync"]
