"""
OMK DEV - Autonomous AI Development Assistant
FastAPI Service
"""
import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import structlog

# Configure logging
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.add_log_level,
        structlog.processors.JSONRenderer()
    ]
)
logger = structlog.get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup/shutdown"""
    logger.info("🚀 Starting OMK DEV API Server")
    
    # Initialize core systems in background
    app.state.orchestrator = None
    app.state.initializing = True
    
    async def init_background():
        """Initialize orchestrator in background"""
        try:
            from app.core.orchestrator import DevOrchestrator
            logger.info("🔧 Initializing Dev Orchestrator...")
            
            orchestrator = DevOrchestrator()
            await orchestrator.initialize()
            
            app.state.orchestrator = orchestrator
            logger.info("✅ OMK DEV fully operational")
        except Exception as e:
            logger.warning(f"⚠️  Orchestrator initialization failed: {e}")
        finally:
            app.state.initializing = False
    
    # Start initialization in background
    asyncio.create_task(init_background())
    
    logger.info("✅ API Server ready (orchestrator initializing in background)")
    
    yield
    
    # Shutdown
    logger.info("🛑 Shutting down OMK DEV")
    if app.state.orchestrator:
        await app.state.orchestrator.shutdown()


def create_app() -> FastAPI:
    """Create FastAPI application"""
    app = FastAPI(
        title="OMK DEV API",
        description="Autonomous AI Development Assistant",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan
    )
    
    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include routers
    from app.api import dev_router
    app.include_router(dev_router, prefix="/api/v1", tags=["Development"])
    
    # Health check
    @app.get("/health")
    async def health_check():
        """Health check endpoint"""
        if getattr(app.state, "initializing", False):
            status = "initializing"
        elif app.state.orchestrator:
            status = "operational"
        else:
            status = "degraded"
        
        return {
            "service": "OMK DEV",
            "version": "1.0.0",
            "status": status,
            "orchestrator_ready": app.state.orchestrator is not None
        }
    
    # Root endpoint
    @app.get("/")
    async def root():
        """Root endpoint"""
        return {
            "service": "OMK DEV - AI Development Assistant",
            "version": "1.0.0",
            "status": "operational",
            "docs": "/docs",
            "health": "/health",
            "capabilities": [
                "bug_fixing",
                "code_analysis",
                "feature_generation",
                "code_review",
                "test_generation"
            ]
        }
    
    return app


# Create app instance
app = create_app()

if __name__ == "__main__":
    import uvicorn
    import os
    
    port = int(os.getenv("PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port)
