# Pomelo Documentation - Context

## About Pomelo

Pomelo is a B2B fintech that provides infrastructure for issuing, processing, 
and managing credit, debit, and prepaid cards across Latin America. 
Clients include banks (BBVA, Santander, Bancolombia) and fintechs (PayJoy, Binance, Western Union).

## Solutions

### Issuer Processing
For clients with their own Visa or Mastercard license. Pomelo provides the modern 
processing engine to replace legacy processors.

### BIN Sponsorship
For clients without their own license. Pomelo provides the BIN, regulatory compliance, 
and processing under its own license. Ideal for new fintechs.

## Modules

### Authorizer
Authorizes prepaid and debit card transactions through digital accounts. 
Real-time decision making with <200ms latency requirement.

### Credit Core
Manages credit card rules: limits, interest, installments, billing cycles.

### 3D Secure (3DS)
Authentication layer for online (card-not-present) transactions. 
Reduces fraud and shifts liability from merchant to issuer.

### Dynamic CVV
A CVV that rotates over time, replacing the static CVV printed on the card. 
Adds a fraud-prevention layer for online transactions.

### Fraud Prevention
Rules engine to allow, reject, or block operations based on configurable risk policies.

### Stand-in
Failover authorization. When the client's systems don't respond in time, 
Pomelo authorizes on their behalf based on predefined rules.

### Tokenization
Integration with Apple Pay and Google Pay. Replaces the real card number (PAN) 
with a tokenized version that only works in a specific context.

### Distribution
Physical card manufacturing, embossing, and shipping logistics.

## Identity (KYC/KYB)

### KYC (Know Your Customer)
Identity verification for individuals. Required by regulation before issuing a card. 
Documents: ID front/back, selfie, proof of address.

### KYB (Know Your Business)
Identity verification for companies (corporate cards). 
Documents: incorporation papers, statute, KYC of partners.

## Integration

### Webhooks
Pomelo notifies clients of transaction events via webhooks. 
Clients must configure an HTTPS endpoint that returns 200 OK in <200ms. 
Webhooks are signed with HMAC for verification.

### REST API
All operations are available via REST API with OAuth 2.0 authentication. 
Base URL: api.pomelo.la

### Sandbox
Pomelo provides a sandbox environment with test cards and a Postman collection 
for integration testing.

## MCP Server

Pomelo exposes a Model Context Protocol (MCP) server in beta. 
It allows IDEs (Cursor, VS Code, Claude Code) to query the API documentation 
in natural language. Tools available: search_endpoints, get_endpoint, 
generate_request_example, list_endpoints_by_topic, list_topics.