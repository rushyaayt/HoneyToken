#!/usr/bin/env bash
# Example: generate an ephemeral honeytoken and print it so CI can 'secret' it into the job
curl -s -X POST http://localhost:8000/generate -H "Content-Type: application/json" -d '{"type":"api_key"}'
