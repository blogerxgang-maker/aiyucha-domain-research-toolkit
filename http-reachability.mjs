const input = process.argv[2];
if (!input) {
  console.error('usage: node http-reachability.mjs <domain-or-url>');
  process.exit(2);
}
const url = input.includes('://') ? input : `https://${input}`;
const started = Date.now();
try {
  const response = await fetch(url, { redirect: 'follow', signal: AbortSignal.timeout(10000) });
  console.log(JSON.stringify({ input, url, status: response.status, final_url: response.url, elapsed_ms: Date.now() - started, content_type: response.headers.get('content-type') }, null, 2));
} catch (error) {
  console.log(JSON.stringify({ input, url, error: error.name, detail: error.message, elapsed_ms: Date.now() - started }, null, 2));
}
