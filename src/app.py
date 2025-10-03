#!/usr/bin/env python3
"""
Demo Agrarian Application
Professional FastAPI application for testing the private CI/CD pipeline
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import time
import logging
from datetime import datetime
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Demo Agrarian Application",
    description="Professional Demo Application for Agrarian CI/CD Testing",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_model=Dict[str, Any])
async def root():
    """Root endpoint with application information"""
    return {
        "message": "Demo Agrarian Application",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "environment": os.getenv("ENVIRONMENT", "development"),
        "status": "running",
        "pipeline": "private-ci-cd-pipeline"
    }

@app.get("/health", response_model=Dict[str, Any])
async def health():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "uptime": time.time(),
        "version": "1.0.0",
        "pipeline": "private-ci-cd-pipeline"
    }

@app.get("/info", response_model=Dict[str, Any])
async def info():
    """Application information endpoint"""
    return {
        "app_name": "demo-agrarian-app",
        "version": "1.0.0",
        "description": "Demo Application for Private CI/CD Pipeline Testing",
        "features": [
            "FastAPI framework",
            "Docker containerized",
            "Private CI/CD pipeline",
            "Health monitoring",
            "Professional logging",
            "CORS enabled"
        ],
        "endpoints": [
            "/",
            "/health",
            "/info",
            "/docs",
            "/redoc"
        ],
        "pipeline": "private-ci-cd-pipeline"
    }

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail, "timestamp": datetime.now().isoformat()}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=3000,
        log_level="info",
        access_log=True
    )
