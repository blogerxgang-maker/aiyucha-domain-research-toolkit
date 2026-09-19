# Proposed curl examples

> Draft only. These commands illustrate the planned public contract and are **not expected to work until AIYucha announces a live public API**.

```bash
export AIYUCHA_API_KEY="YOUR_PUBLIC_API_KEY"
```

Network and blocking research:

```bash
curl -sS \
  -H "X-API-Key: $AIYUCHA_API_KEY" \
  "https://api.aiyucha.com/v1/domains/example.com/network"
```

ICP research:

```bash
curl -sS \
  -H "X-API-Key: $AIYUCHA_API_KEY" \
  "https://api.aiyucha.com/v1/domains/example.com/icp"
```

Backlink research:

```bash
curl -sS \
  -H "X-API-Key: $AIYUCHA_API_KEY" \
  "https://api.aiyucha.com/v1/domains/example.com/backlinks"
```

Domain history:

```bash
curl -sS \
  -H "X-API-Key: $AIYUCHA_API_KEY" \
  "https://api.aiyucha.com/v1/domains/example.com/history"
```

Valuation draft:

```bash
curl -sS -X POST \
  -H "X-API-Key: $AIYUCHA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"currency":"CNY","purpose":"purchase"}' \
  "https://api.aiyucha.com/v1/domains/example.com/valuation"
```

Baidu SEO research:

```bash
curl -sS \
  -H "X-API-Key: $AIYUCHA_API_KEY" \
  "https://api.aiyucha.com/v1/domains/example.com/baidu"
```

When the public API is implemented, these examples should be tested against the actual service before the `draft` notice is removed.

