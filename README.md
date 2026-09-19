# 爱域查域名研究工具箱

这是爱域查（AIYucha）的公开域名研究工具箱，主要面向站长、域名投资者、SEO 从业者和开发者，整理一套更容易复核的域名尽调方法。

重点覆盖：**域名被墙检测、微信域名拦截检测、DNS 污染查询、ICP备案查询、外链/反链、引用域、域名历史、历史快照、百度收录和域名估价**。

爱域查入口：[aiyucha.com](https://aiyucha.com/?utm_source=github&utm_medium=organic_referral&utm_campaign=search_surface_2026q3&utm_content=d1-toolkit-readme)

English version: [README.en.md](README.en.md)

## 这个仓库解决什么问题

很多域名查询工具给出一个数字或一个“好/坏”结论，但真正做域名购买、建站或 SEO 判断时，更重要的是分清三层：

1. **事实**：到底查到了什么；
2. **推断**：这些事实可能意味着什么；
3. **决策**：接下来该继续核验什么、是否值得买、是否适合建站。

例如：

- “国内打不开”不等于“域名被墙”；
- “微信打不开”不一定是网络层被墙；
- “几十万外链”不等于 SEO 资产很强；
- “域名很老”不等于历史一直在正常建站；
- “百度权重”也不是百度官方发布的指标。

这个仓库的目标，就是把这些容易混淆的地方拆开。

## 主题入口

| 你想查什么 | 从这里开始 |
| --- | --- |
| 域名到底是被墙，还是网站本身挂了？ | [域名被墙怎么判断](docs/domain-block-check.md) |
| 微信里打不开，怎么区分微信拦截和普通故障？ | [微信域名拦截检测](docs/wechat-domain-block-check.md) |
| DNS 污染和“被墙”有什么区别？ | [域名 DNS 污染查询](docs/dns-pollution-check.md) |
| 备案历史对买老域名有什么意义？ | [域名备案 / ICP 查询](docs/icp-lookup.md) |
| 外链多是不是一定值钱？ | [外链查询与反链查询](docs/backlink-check.md) |
| 引用域应该怎么看？ | [引用域分析](docs/referring-domains.md) |
| 老域名过去做过什么网站？ | [域名建站历史](docs/domain-history.md) |
| 历史页面和快照怎么看？ | [域名历史快照](docs/domain-snapshot.md) |
| 历史外链还有没有价值？ | [域名外链历史](docs/backlink-history.md) |
| 域名怎么估价才不只看一个分数？ | [域名估价](docs/domain-valuation.md) |
| 百度收录和“百度权重”怎么区分？ | [百度收录与百度权重](docs/baidu-index-check.md) |

## 本地先做一个最小基线

仓库里有几个很小的本地示例，可以先回答“当前这台机器看到了什么”。

```bash
python examples/python/http_reachability.py example.com
python examples/python/dns_lookup.py example.com
```

Node.js 18+：

```bash
node examples/javascript/http-reachability.mjs example.com
```

这些脚本只能作为**单点基线**，不能单独证明 GFW、跨运营商 DNS 污染或微信拦截。区域性问题需要多节点、不同网络或平台上下文共同判断。

## 仓库结构

```text
docs/                域名研究方法和指标解释
examples/python/     Python 本地检查示例
examples/javascript/ Node.js 本地检查示例
examples/curl/       拟议公开 API 的 curl 示例
examples-output/     规范化结果示例
schemas/             公开研究结果 schema
troubleshooting/     常见误判与排查说明
openapi/             拟议公开 API 与 OpenAPI 草案
```

## 拟议公开 API

仓库已经放入一份**外部 API 契约草案**：

- [`openapi/openapi.yaml`](openapi/openapi.yaml)：OpenAPI 3.1 草案；
- [`docs/public-api-draft.md`](docs/public-api-draft.md)：接口设计和结果语义；
- [`examples/curl/README.md`](examples/curl/README.md)：curl 示例。

这套接口目前明确是 **draft / not live（草案 / 尚未上线）**。

策略是先把外部接口的命名、资源划分、返回结构和错误语义整理清楚，用于 GitHub、GitBook、Postman 等公开资料；以后真正开放 API 时，再让技术实现与这套外部契约对齐。

它**不是**爱域查内部 Growth API 的公开文档，也不会暴露 provider、worker、job、node、内部成本、缓存路径、凭证或内部诊断信息。

## 一个更稳的结果模型

公开结果建议统一拆成：

```text
observations  →  直接查到的事实
inferences    →  基于事实形成的推断
next_steps    →  下一步建议核验什么
warnings      →  数据边界或证据不足说明
```

这样可以避免把“查不到”“超时”“无快照”直接写成负面结论。

## 安全与边界

仓库中的本地示例只做普通 DNS 和 HTTP 请求，不绕过访问控制、不规避平台限制，也不做侵入式扫描。

更多说明见 [SECURITY.md](SECURITY.md)。

## License

MIT，见 [LICENSE](LICENSE)。
