# 爱域查公开 API 契约草案

> **状态：draft / not live（草案 / 尚未上线）**。
>
> 本文档定义的是未来可能开放给开发者的外部接口形态，不代表 `api.aiyucha.com` 或下面的路径现在已经可调用。

这套 API 先解决一个问题：让 GitHub、GitBook、Postman、未来 SDK 使用统一的接口语言。等以后真正开放 API，再让技术实现与这套契约对齐。

它和爱域查当前稳定运行的网站、内部 Growth API 是两回事。

## 拟议接口

```text
GET  /v1/domains/{domain}/network
GET  /v1/domains/{domain}/icp
GET  /v1/domains/{domain}/backlinks
GET  /v1/domains/{domain}/history
POST /v1/domains/{domain}/valuation
GET  /v1/domains/{domain}/baidu
```

资源按用户真正关心的问题划分，而不是照搬内部任务、provider 或节点结构。

## 拟议鉴权方式

```http
X-API-Key: YOUR_PUBLIC_API_KEY
```

目前不会发放真实 Key。API Key、套餐、额度、计费和限流规则都留到真正上线时决定。

## 为什么不按内部接口直接公开

公开 API 应该稳定、容易理解，而且不能把内部工程细节暴露出去。

未来公开返回中不应该出现：

- 上游 provider 名称；
- worker / node 标识；
- 内部 job / task / attempt ID；
- 缓存、代理、网关路径；
- 内部成本；
- 内部凭证；
- 原始异常栈和诊断信息。

## 统一响应模型

建议所有查询类接口都保持相同顶层结构：

```json
{
  "request_id": "req_01HYPOTHETICAL",
  "status": "completed",
  "domain": "example.com",
  "observed_at": "2026-09-19T12:00:00Z",
  "observations": [
    {
      "kind": "referring_domains",
      "status": "observed",
      "value": 11457,
      "observed_at": "2026-09-19T12:00:00Z"
    }
  ],
  "inferences": [
    {
      "text": "该域名存在较明显的历史外链资产。",
      "confidence": "high",
      "based_on": ["referring_domains"]
    }
  ],
  "next_steps": ["继续检查来源质量、主题相关性和历史变化。"],
  "warnings": []
}
```

这里刻意把几层拆开：

- `observations`：直接取得的事实；
- `inferences`：基于事实做出的判断；
- `next_steps`：下一步该查什么；
- `warnings`：数据边界或证据不足。

这样可以避免把“没查到”直接解释成“没有”，也避免把一次超时直接解释成“被墙”。

## status 语义

建议只保留三个主状态：

- `completed`：已经取得足够的可用结果；
- `partial`：有可用结果，但部分预期信号没取得；
- `unavailable`：这次没有拿到足以形成有效结果的证据。

“网站打不开”本身不是 API 错误；“历史快照缺失”也不等于历史上从未建站。

## 错误码草案

```text
invalid_domain
invalid_request
unauthorized
quota_exceeded
temporarily_unavailable
unsupported_query
```

对外错误码应该稳定，内部异常类型不直接暴露。

## 版本策略

首版从 `/v1` 开始。

兼容性新增可以继续放在 `v1`；如果未来出现明显破坏兼容性的字段或语义变化，再进入新的 major version。

机器可读版本见 [`openapi/openapi.yaml`](../openapi/openapi.yaml)。
