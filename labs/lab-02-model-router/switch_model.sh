#!/usr/bin/env bash
# Switch the default model by deploying a new AppConfig configuration version.
# Usage: ./switch_model.sh <model-id-or-inference-profile-id>
set -euo pipefail
NEW_MODEL="${1:?Usage: ./switch_model.sh <model-id>}"
STACK=Lab02ModelRouter
out() { aws cloudformation describe-stacks --stack-name "$STACK" \
  --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
APP_ID=$(out AppId); ENV_ID=$(out EnvId); PROFILE_ID=$(out ProfileId)

cat > /tmp/lab02-config.json <<JSON
{"default": {"modelId": "$NEW_MODEL", "temperature": 0.2, "maxTokens": 400},
 "summarize": {"modelId": "$NEW_MODEL", "temperature": 0.0, "maxTokens": 200}}
JSON

VERSION=$(aws appconfig create-hosted-configuration-version \
  --application-id "$APP_ID" --configuration-profile-id "$PROFILE_ID" \
  --content-type application/json --content fileb:///tmp/lab02-config.json \
  /tmp/lab02-version-out.json --query VersionNumber --output text)

aws appconfig start-deployment \
  --application-id "$APP_ID" --environment-id "$ENV_ID" \
  --configuration-profile-id "$PROFILE_ID" --configuration-version "$VERSION" \
  --deployment-strategy-id AppConfig.AllAtOnce \
  --query "[DeploymentNumber,State]" --output text

echo "Deployed configuration version $VERSION with model $NEW_MODEL"
