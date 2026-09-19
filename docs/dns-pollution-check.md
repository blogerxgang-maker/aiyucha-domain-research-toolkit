# DNS pollution checks

DNS pollution is a **resolution problem**, while domain blocking is a broader reachability concept. They can occur together, but they are not synonyms.

## What to compare

A useful DNS investigation compares answers from independent vantage points and resolvers. Look for:

- unexpectedly different A/AAAA answers;
- addresses that do not match the domain's known hosting/CDN pattern;
- answers that change only on particular networks;
- resolution failures while authoritative DNS remains healthy;
- IPv4/IPv6 disagreement.

One public resolver versus one local resolver is not enough to establish a network-wide conclusion. Resolver caching, CDN geo-routing, split-horizon DNS, DNSSEC, and normal load balancing can all create legitimate differences.

## Minimal local check

`examples/python/dns_lookup.py` reports what the local system resolver sees. Treat it as a baseline observation, not a China-wide verdict.

```bash
python examples/python/dns_lookup.py example.com
```

When recording a result, keep resolver/network/time metadata next to the returned IPs. Historical comparisons are far more useful when the observation context is preserved.
