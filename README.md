# AIYucha Domain Research Toolkit

Open research notes and lightweight examples for investigating **domain risk, history, backlinks, ICP/China-market signals, DNS behavior, and valuation evidence**.

This repository is maintained by [AIYucha](https://aiyucha.com/?utm_source=github&utm_medium=organic_referral&utm_campaign=search_surface_2026q3&utm_content=d1-toolkit-readme). It is intentionally more than a link repository: the goal is to make domain due diligence reproducible, explain what each signal can and cannot prove, and keep observations separate from conclusions.

> 中文版：[README.zh-CN.md](README.zh-CN.md)

## What this repository helps with

| Research question | Start here |
| --- | --- |
| Is a domain really blocked, or is the site simply down? | [Domain blocking checks](docs/domain-block-check.md) |
| Why does a domain fail inside WeChat? | [WeChat domain blocking](docs/wechat-domain-block-check.md) |
| How is DNS pollution different from blocking? | [DNS pollution checks](docs/dns-pollution-check.md) |
| What can ICP filing history tell a buyer? | [ICP lookup](docs/icp-lookup.md) |
| Are 800k backlinks better than 10k referring domains? | [Backlink checks](docs/backlink-check.md) and [referring domains](docs/referring-domains.md) |
| What did an old domain previously host? | [Domain history](docs/domain-history.md) and [historical snapshots](docs/domain-snapshot.md) |
| How should historical links affect value? | [Backlink history](docs/backlink-history.md) and [domain valuation](docs/domain-valuation.md) |
| What does “Baidu weight” really mean? | [Baidu index notes](docs/baidu-index-check.md) |

## A useful evidence model

A domain-research result should separate three layers:

1. **Observation** — something directly measured or found, such as an HTTP status, historical snapshot year, referring-domain count, or filing record.
2. **Inference** — a reasoned interpretation, such as “the site appears inactive” or “historical use changed materially.”
3. **Decision** — what the buyer, operator, or SEO should do next.

Mixing these layers is how a simple timeout becomes “this domain is blocked,” or how a large backlink count becomes “this domain is valuable.”

## Quick local baseline

These examples are deliberately small and independent. They are useful for a first look, not as substitutes for multi-region or platform-specific evidence.

```bash
python examples/python/http_reachability.py example.com
python examples/python/dns_lookup.py example.com
```

Node.js 18+:

```bash
node examples/javascript/http-reachability.mjs example.com
```

A single machine **cannot** prove GFW blocking, DNS pollution across networks, or WeChat blocking. For those questions you need multiple independent observations or a purpose-built service.

## Repository layout

```text
docs/               Research guides and signal interpretation
examples/python/    Small zero-dependency local checks
examples/javascript/Node.js example
examples-output/    Example normalized observation
schemas/            Public research-result schema
troubleshooting/    Common interpretation mistakes
openapi/             Public API status and future OpenAPI surface
```

## Public API status

AIYucha's internal Growth API is **not** a public developer API and is intentionally not documented here. We will only publish API examples after a separate public-API audit establishes versioning, API keys, quotas, stable error codes, sanitized response schemas, and an OpenAPI contract. See [openapi/README.md](openapi/README.md).

No internal provider, worker, job, cost, credential, or diagnostic fields belong in a public client.

## Security and responsible use

The examples make ordinary DNS and HTTP requests. They do not bypass access controls, evade platform restrictions, or perform intrusive scanning. See [SECURITY.md](SECURITY.md).

## License

MIT. See [LICENSE](LICENSE).
