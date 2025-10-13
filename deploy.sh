#!/bin/bash
# OMK DEV Deployment Script for Google Cloud Run

set -e

PROJECT_ID=${1:-"omk-hive"}
REGION=${2:-"us-central1"}
SERVICE_NAME="omk-dev"

echo "🚀 Deploying OMK DEV to Google Cloud Run..."
echo "   Project: $PROJECT_ID"
echo "   Region: $REGION"
echo "   Service: $SERVICE_NAME"
echo ""

cd backend

# Build the container image
echo "📦 Building container image..."
gcloud builds submit --tag=gcr.io/$PROJECT_ID/$SERVICE_NAME

# Deploy to Cloud Run
echo "🌐 Deploying to Cloud Run..."
gcloud run deploy $SERVICE_NAME \
  --image gcr.io/$PROJECT_ID/$SERVICE_NAME \
  --region $REGION \
  --platform managed \
  --allow-unauthenticated \
  --memory 512Mi \
  --cpu 1 \
  --timeout 300s \
  --set-env-vars DEFAULT_LLM_PROVIDER=gemini \
  --set-secrets GEMINI_API_KEY=gemini-api-key:latest,OPENAI_API_KEY=openai-api-key:latest,ANTHROPIC_API_KEY=anthropic-api-key:latest

echo ""
echo "✅ Deployment complete!"
echo ""
echo "Service URL:"
gcloud run services describe $SERVICE_NAME --region=$REGION --format="value(status.url)"
