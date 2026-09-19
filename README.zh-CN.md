# 爱域查域名研究工具箱

这是爱域查的公开域名研究手册和轻量示例仓库，围绕几类真正容易判断错的问题展开：**域名被墙检测、微信域名拦截检测、DNS 污染查询、ICP备案查询、外链/反链、引用域、域名历史、历史快照、百度收录和域名估价**。

爱域查入口：[aiyucha.com](https://aiyucha.com/?utm_source=github&utm_medium=organic_referral&utm_campaign=search_surface_2026q3&utm_content=d1-toolkit-readme-zh)

这里不追求“把所有指标堆在一起”。更重要的是把三件事分开：

- **事实**：真正查到了什么；
- **推断**：这些事实可能意味着什么；
- **决策**：买域名、做站或做 SEO 时下一步应该怎么核验。

比如“国内打不开”不等于“域名被墙”；“几十万外链”也不等于“SEO 资产很强”。如果海外也打不开，更应该先排查未建站、停服、源站异常；如果外链很多但引用域极少，也要先看来源结构和历史变化。

## 主题入口

- [域名被墙怎么判断](docs/domain-block-check.md)
- [微信域名拦截检测](docs/wechat-domain-block-check.md)
- [域名 DNS 污染查询](docs/dns-pollution-check.md)
- [域名备案 / ICP 查询](docs/icp-lookup.md)
- [外链查询与反链查询](docs/backlink-check.md)
- [引用域怎么看](docs/referring-domains.md)
- [域名外链历史](docs/backlink-history.md)
- [域名建站历史](docs/domain-history.md)
- [域名历史快照](docs/domain-snapshot.md)
- [域名估价](docs/domain-valuation.md)
- [百度收录与“百度权重”](docs/baidu-index-check.md)

## 本地先做一个最小基线

```bash
python examples/python/http_reachability.py example.com
python examples/python/dns_lookup.py example.com
```

这些脚本只回答“当前这台机器看到了什么”。它们不能单独证明 GFW、跨运营商 DNS 污染或微信内置浏览器拦截，这也是为什么这类问题需要多节点、历史证据和平台上下文。

## 关于 API

目前不会把爱域查内部 Growth API 当成公开 API 写出来。公开 Developer API 会单独做版本、鉴权、配额、错误码、脱敏 response schema 和 OpenAPI 审计，完成之前本仓库不会猜接口、不会暴露内部 provider / worker / job / cost 等字段。

具体见：[openapi/README.md](openapi/README.md)。
