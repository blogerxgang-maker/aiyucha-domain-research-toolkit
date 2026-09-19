# Proposed AIYucha Public API

> **Status: draft / not live.** This document describes a proposed external contract for future developer access. It does not claim that `api.aiyucha.com` or any endpoint below is currently available.

The goal is to let GitHub, GitBook, Postman and future SDKs share one stable vocabulary before the production website is technically aligned with it.

## Proposed surface

```text
GET  /v1/domains/{domain}/network
GET  /v1/domains/{domain}/icp
GET  /v1/domains/{domain}/backlinks
GET  /v1/domains/{domain}/history
POST /v1/domains/{domain}/valuation
GET  /v1/domains/{domain}/baidu
```

These six resources map to real user questions rather than internal execution paths. The public API should never expose provider names, worker/node IDs, job IDs, internal costs, cache paths, credentials or raw diagnostics.

## Authentication

The proposed public contract uses:

```http
X-API-Key: YOUR_PUBLIC_API_KEY
```

No public keys are issued by this draft. Authentication, quota tiers and billing remain implementation decisions for a later technical alignment.

## Response model

Every endpoint uses the same top-level model:

```json
{
  "request_id": "req_01HYPOTHETICAL",
  "status": "completed",
  "domain": "example.com",
  "observed_at": "2026-09-19T12:00:00Z",
  "observations": [
    {
      "kind": "referring_domains",
      "status": "observed",
      "value": 11457,
      "observed_at": "2026-09-19T12:00:00Z"
    }
  ],
  "inferences": [
    {
      "text": "The domain has a substantial historical link footprint.",
      "confidence": "high",
      "based_on": ["referring_domains"]
    }
  ],
  "next_steps": ["Review source quality and historical topic continuity."],
  "warnings": []
}
```

The separation is deliberate:

- `observations` = directly obtained facts;
- `inferences` = interpretations based on those facts;
- `next_steps` = decision-support actions;
- `warnings` = data-boundary notes, not generic disclaimers.

## Status semantics

`completed` means the requested public resource produced usable evidence. `partial` means some evidence is usable but one or more expected signals were unavailable. `unavailable` means the request completed without enough evidence to form a useful result.

A site being offline is not automatically an API failure. A missing historical snapshot is missing evidence, not proof that no site existed. A large backlink count is not itself a valuation conclusion.

## Error model

Proposed codes include:

- `invalid_domain`
- `invalid_request`
- `unauthorized`
- `quota_exceeded`
- `temporarily_unavailable`
- `unsupported_query`

Errors remain public and stable; internal exception classes must not leak into the response.

## Versioning

The contract starts at `/v1`. Backward-compatible additions may extend schemas, while breaking changes require a new major API version.

The canonical machine-readable draft is [`openapi/openapi.yaml`](../openapi/openapi.yaml).
