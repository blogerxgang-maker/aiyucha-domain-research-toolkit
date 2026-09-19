#!/usr/bin/env python3
import json, sys, time
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

def normalize(value: str) -> str:
    if '://' not in value:
        return 'https://' + value
    return value

def main() -> int:
    if len(sys.argv) != 2:
        print('usage: http_reachability.py <domain-or-url>', file=sys.stderr)
        return 2
    url = normalize(sys.argv[1].strip())
    started = time.monotonic()
    out = {'input': sys.argv[1], 'url': url}
    try:
        req = Request(url, headers={'User-Agent': 'AIYucha-Research-Example/1.0'})
        with urlopen(req, timeout=10) as r:
            out.update(status=r.status, final_url=r.geturl(), elapsed_ms=round((time.monotonic()-started)*1000), content_type=r.headers.get('content-type'))
    except HTTPError as e:
        out.update(status=e.code, final_url=e.geturl(), elapsed_ms=round((time.monotonic()-started)*1000), error='http_error')
    except URLError as e:
        out.update(elapsed_ms=round((time.monotonic()-started)*1000), error='network_error', detail=str(e.reason))
    except Exception as e:
        out.update(elapsed_ms=round((time.monotonic()-started)*1000), error=type(e).__name__, detail=str(e))
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
