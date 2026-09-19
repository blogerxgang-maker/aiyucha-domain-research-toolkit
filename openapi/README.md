# Proposed AIYucha Public API

> **Status: draft / not live.** This directory defines a proposed external developer contract. It does not claim that the endpoints are currently deployed, and it does not mirror AIYucha's internal Growth API.

The strategy is deliberately decoupled from the production website: first make the external vocabulary, endpoint shape and response model coherent for GitHub, GitBook, Postman and future SDKs; later, when appropriate, align the implementation behind that contract without forcing changes to the currently stable website.

## Draft assets

- [`openapi.yaml`](openapi.yaml) — machine-readable OpenAPI 3.1 draft.
- [`../docs/public-api-draft.md`](../docs/public-api-draft.md) — design notes and response semantics.
- [`../examples/curl/README.md`](../examples/curl/README.md) — proposed curl usage examples.

## Proposed base URL

```text
https://api.aiyucha.com/v1
```

This is a **planned namespace only** until AIYucha separately announces a live public API.

## Proposed resources

```text
GET  /domains/{domain}/network
GET  /domains/{domain}/icp
GET  /domains/{domain}/backlinks
GET  /domains/{domain}/history
POST /domains/{domain}/valuation
GET  /domains/{domain}/baidu
```

The public surface is intentionally organized around user questions instead of internal execution details.

## Public-contract boundary

A future implementation may use any internal architecture, but the external contract should not expose:

- provider or upstream names;
- worker/node identifiers;
- job/task/attempt identifiers;
- cache/proxy/gateway paths;
- internal cost information;
- internal exception classes or diagnostics;
- Growth credentials or other secrets.

Authentication is currently modeled as `X-API-Key`, but key issuance, quotas, billing and actual rate limits remain future implementation decisions.

The draft can evolve freely while it is marked `0.1.0-draft`. The `draft / not live` notice should only be removed after the public API has been technically aligned and tested against a real service.
