Architecture

- FastAPI service provides endpoints to generate honeytokens and receive webhook alerts.
- Tokens can be seeded into CI runs, container images, or configuration files as low-cost traps.
- When a token is used (e.g., attacker attempts to access an API), the usage triggers an alert endpoint that records context and notifies operators.

Next steps
- Add persistence (Postgres) for tokens and events
- Add signing/rotation and TTP templates per token type
- Integrate with SIEM (Splunk/Elastic/CloudWatch)
