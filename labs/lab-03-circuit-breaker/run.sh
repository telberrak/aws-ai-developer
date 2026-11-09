#!/usr/bin/env bash
# Start one execution. Usage: ./run.sh [fail]   ("fail" simulates a primary failure)
set -euo pipefail
ARN=$(aws cloudformation describe-stacks --stack-name Lab03CircuitBreaker \
  --query "Stacks[0].Outputs[?OutputKey=='StateMachineArn'].OutputValue" --output text)
FAIL=false; [ "${1:-}" = "fail" ] && FAIL=true
EXEC=$(aws stepfunctions start-execution --state-machine-arn "$ARN" \
  --input "{\"prompt\":\"Name one AWS Region.\",\"simulateFailure\":$FAIL}" --query executionArn --output text)
sleep 8
aws stepfunctions describe-execution --execution-arn "$EXEC" --query "[status,output]" --output text
