# Public API status

AIYucha does not currently document its internal Growth API as a public developer API in this repository.

Before a public `/v1` surface is published, it must have:

- a separate public authentication model;
- stable versioning;
- quotas and rate limits;
- idempotency where mutations exist;
- documented error codes;
- sanitized response schemas;
- no provider/worker/job/internal-cost fields;
- no internal Growth credentials;
- OpenAPI plus curl/Python/JavaScript examples.

Until that audit is complete, examples in this repository remain standalone research utilities and documentation. This avoids creating a public contract around an internal interface.
