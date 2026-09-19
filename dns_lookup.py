#!/usr/bin/env python3
import json, socket, sys, time

def main() -> int:
    if len(sys.argv) != 2:
        print('usage: dns_lookup.py <domain>', file=sys.stderr)
        return 2
    domain=sys.argv[1].strip().rstrip('.')
    started=time.monotonic()
    out={'domain':domain}
    try:
        rows=socket.getaddrinfo(domain, None, proto=socket.IPPROTO_TCP)
        ips=sorted({row[4][0] for row in rows})
        out.update(addresses=ips, elapsed_ms=round((time.monotonic()-started)*1000))
    except socket.gaierror as e:
        out.update(addresses=[], elapsed_ms=round((time.monotonic()-started)*1000), error='dns_error', detail=str(e))
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
