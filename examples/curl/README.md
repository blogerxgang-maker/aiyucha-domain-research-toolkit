# 爱域查拟议公开 API：curl 示例

> **草案 / 尚未上线。** 下面命令只是展示未来公开 API 的使用方式，在爱域查正式宣布 Public API 上线之前，不应期待这些请求可以成功调用。

先假设未来已经拿到公开 API Key：

```bash
export AIYUCHA_API_KEY="YOUR_PUBLIC_API_KEY"
```

## 域名被墙 / 网络与 DNS 相关研究

```bash
curl -sS \
  -H "X-API-Key: $AIYUCHA_API_KEY" \
  "https://api.aiyucha.com/v1/domains/example.com/network"
```

适合承载：大陆访问、海外访问、DNS 异常、区域性可达性等外部结果。

## ICP 备案研究

```bash
curl -sS \
  -H "X-API-Key: $AIYUCHA_API_KEY" \
  "https://api.aiyucha.com/v1/domains/example.com/icp"
```

适合返回当前或历史备案相关证据，但不会把“没有当前备案”解释成“历史从未备案”。

## 外链 / 反链 / 引用域

```bash
curl -sS \
  -H "X-API-Key: $AIYUCHA_API_KEY" \
  "https://api.aiyucha.com/v1/domains/example.com/backlinks"
```

重点应放在引用域、来源结构、历史变化和质量，而不只是总外链数量。

## 域名建站历史 / 历史快照

```bash
curl -sS \
  -H "X-API-Key: $AIYUCHA_API_KEY" \
  "https://api.aiyucha.com/v1/domains/example.com/history"
```

## 域名估价

```bash
curl -sS -X POST \
  -H "X-API-Key: $AIYUCHA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"currency":"CNY","purpose":"purchase"}' \
  "https://api.aiyucha.com/v1/domains/example.com/valuation"
```

估价接口未来也应该返回“依据”，而不是只给一个数字。

## 百度收录 / SEO 可见性

```bash
curl -sS \
  -H "X-API-Key: $AIYUCHA_API_KEY" \
  "https://api.aiyucha.com/v1/domains/example.com/baidu"
```

这里会把“百度收录”和第三方所谓“百度权重”分开表达；后者不是百度官方指标。

等 Public API 真正实现后，应先用真实服务回归这些示例，再删除本页的 `draft / not live` 提示。
