"""API router for OMK DEV"""
from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
from typing import Optional, List, Dict
import structlog

logger = structlog.get_logger(__name__)

dev_router = APIRouter()


# Request/Response Models
class BugFixRequest(BaseModel):
    error_log: str
    file_path: Optional[str] = None
    code_context: Optional[str] = None
    test_file: Optional[str] = None


class BugFixResponse(BaseModel):
    success: bool
    fixed_code: Optional[str] = None
    explanation: str
    confidence: float
    tests: Optional[str] = None


class CodeAnalysisRequest(BaseModel):
    code: str
    language: str = "python"
    focus: Optional[List[str]] = None  # e.g., ["security", "performance"]


class CodeAnalysisResponse(BaseModel):
    issues: List[Dict]
    suggestions: List[Dict]
    metrics: Dict


class FeatureGenerationRequest(BaseModel):
    description: str
    framework: Optional[str] = None
    language: str = "python"
    include_tests: bool = True


class FeatureGenerationResponse(BaseModel):
    code: str
    tests: Optional[str] = None
    documentation: str
    dependencies: List[str]


# Endpoints
@dev_router.post("/fix-bug", response_model=BugFixResponse)
async def fix_bug(request: BugFixRequest, req: Request):
    """Analyze and fix a bug"""
    try:
        orchestrator = req.app.state.orchestrator
        if not orchestrator:
            raise HTTPException(status_code=503, detail="Orchestrator not ready")
        
        result = await orchestrator.fix_bug(
            error_log=request.error_log,
            file_path=request.file_path,
            code_context=request.code_context
        )
        
        return BugFixResponse(**result)
    except Exception as e:
        logger.error(f"Bug fix failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@dev_router.post("/analyze", response_model=CodeAnalysisResponse)
async def analyze_code(request: CodeAnalysisRequest, req: Request):
    """Analyze code for issues and improvements"""
    try:
        orchestrator = req.app.state.orchestrator
        if not orchestrator:
            raise HTTPException(status_code=503, detail="Orchestrator not ready")
        
        result = await orchestrator.analyze_code(
            code=request.code,
            language=request.language,
            focus=request.focus
        )
        
        return CodeAnalysisResponse(**result)
    except Exception as e:
        logger.error(f"Code analysis failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@dev_router.post("/generate-feature", response_model=FeatureGenerationResponse)
async def generate_feature(request: FeatureGenerationRequest, req: Request):
    """Generate a feature from description"""
    try:
        orchestrator = req.app.state.orchestrator
        if not orchestrator:
            raise HTTPException(status_code=503, detail="Orchestrator not ready")
        
        result = await orchestrator.generate_feature(
            description=request.description,
            framework=request.framework,
            language=request.language,
            include_tests=request.include_tests
        )
        
        return FeatureGenerationResponse(**result)
    except Exception as e:
        logger.error(f"Feature generation failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@dev_router.get("/status")
async def get_status(req: Request):
    """Get service status"""
    orchestrator = req.app.state.orchestrator
    
    return {
        "ready": orchestrator is not None,
        "initializing": getattr(req.app.state, "initializing", False),
        "capabilities": [
            "bug_fixing",
            "code_analysis",
            "feature_generation"
        ]
    }
