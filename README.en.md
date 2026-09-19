# AIYucha Domain Research Toolkit

Open research notes and lightweight examples for domain risk, history, backlinks, ICP/China-market signals, DNS behavior, and valuation evidence.

This repository is maintained by [AIYucha](https://aiyucha.com/?utm_source=github&utm_medium=organic_referral&utm_campaign=search_surface_2026q3&utm_content=d1-toolkit-readme-en).

Chinese version: [README.md](README.md)

## What this repository is for

The core idea is to separate:

1. **Observations** — facts directly obtained from a check;
2. **Inferences** — interpretations based on those facts;
3. **Decisions** — what a buyer, operator, SEO or developer should verify next.

A timeout is not automatically “blocked.” A large backlink count is not automatically “valuable.” An old registration date does not prove continuous website use.

## Main topics

- [Domain blocking checks](docs/domain-block-check.md)
- [WeChat domain blocking](docs/wechat-domain-block-check.md)
- [DNS pollution checks](docs/dns-pollution-check.md)
- [ICP lookup](docs/icp-lookup.md)
- [Backlink checks](docs/backlink-check.md)
- [Referring domains](docs/referring-domains.md)
- [Backlink history](docs/backlink-history.md)
- [Domain history](docs/domain-history.md)
- [Historical snapshots](docs/domain-snapshot.md)
- [Domain valuation](docs/domain-valuation.md)
- [Baidu index notes](docs/baidu-index-check.md)

## Proposed public API

A draft external API contract is available in [`openapi/openapi.yaml`](openapi/openapi.yaml), with design notes in [`docs/public-api-draft.md`](docs/public-api-draft.md) and proposed curl examples in [`examples/curl/README.md`](examples/curl/README.md).

It is explicitly **draft / not live**. The contract is being shaped first for public developer documentation and can be aligned with AIYucha's production implementation later.

It does not expose or document the internal Growth API.

## License

MIT. See [LICENSE](LICENSE).
