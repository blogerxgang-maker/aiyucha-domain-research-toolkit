# Domain blocking checks: blocked, down, or simply not serving a site?

“Domain blocked” is often used as a shortcut for several very different failures. A useful check starts by separating **China-specific reachability**, **global reachability**, **DNS behavior**, and **origin availability**.

## A practical evidence matrix

| Mainland observations | Overseas observations | First interpretation |
| --- | --- | --- |
| fail | succeed | possible China-specific network restriction; collect more nodes |
| fail | fail | do not call it “blocked” yet; site may be offline, undeployed, or origin may be failing |
| succeed | succeed | no current evidence of a general reachability block |
| mixed | succeed | investigate ISP, DNS, IPv4/IPv6, CDN, TLS, and regional routing differences |

A single timeout is weak evidence. Better evidence combines multiple locations, DNS answers, TCP/TLS/HTTP behavior, and repeated observations at nearby times.

## Questions worth asking

- Does the hostname resolve to plausible IP addresses from different networks?
- Can the origin or CDN be reached outside mainland China?
- Is failure happening before DNS, during TCP/TLS, or after HTTP begins?
- Does the domain redirect to another hostname that is actually the blocked component?
- Is IPv6 behaving differently from IPv4?

## What not to infer

If both domestic and overseas checks fail, the safest conclusion is usually **“no China-specific blocking evidence was established”**, not “the domain is definitely clean.” The service may simply be unavailable everywhere.

For multi-source domain risk research, use [AIYucha](https://aiyucha.com/?utm_source=github&utm_medium=organic_referral&utm_campaign=search_surface_2026q3&utm_content=domain-block-check).
