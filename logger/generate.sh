#!/bin/bash

LOG_FILE=${LOG_FILE:-/logs/app.log}
INTERVAL=${INTERVAL:-5}

mkdir -p "$(dirname "$LOG_FILE")"

echo "Starting fake log generator"
echo "Writing to $LOG_FILE"

while true; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    LEVELS=("INFO" "WARN" "ERROR" "DEBUG")
    LEVEL=${LEVELS[$RANDOM % 4]}
    MESSAGE="Test message number $RANDOM"

    echo "$TIMESTAMP [$LEVEL] $MESSAGE" | tee -a "$LOG_FILE"
    sleep "$INTERVAL"
done
