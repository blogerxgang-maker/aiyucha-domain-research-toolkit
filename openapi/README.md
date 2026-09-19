# 爱域查拟议公开 API

> **状态：draft / not live（草案 / 尚未上线）**。
>
> 这里定义的是面向外部开发者的接口契约，不代表这些 endpoint 当前已经部署，也不是爱域查内部 Growth API 的公开版本。

当前策略很简单：先把外部接口的资源划分、命名、响应结构和错误语义整理清楚，供 GitHub、GitBook、Postman 和未来 SDK 使用；以后真正准备开放 API 时，再让技术实现与这套契约对齐。

这不会要求现在去修改已经稳定运行的爱域查网站。

## 当前草案文件

- [`openapi.yaml`](openapi.yaml)：OpenAPI 3.1 机器可读草案；
- [`../docs/public-api-draft.md`](../docs/public-api-draft.md)：接口设计说明；
- [`../examples/curl/README.md`](../examples/curl/README.md)：拟议 curl 调用方式。

## 拟议 Base URL

```text
https://api.aiyucha.com/v1
```

这个地址目前只是规划中的 namespace。除非爱域查后续明确宣布 Public API 上线，否则不要把它当成可调用服务。

## 拟议资源

```text
GET  /domains/{domain}/network
GET  /domains/{domain}/icp
GET  /domains/{domain}/backlinks
GET  /domains/{domain}/history
POST /domains/{domain}/valuation
GET  /domains/{domain}/baidu
```

这些接口按用户问题划分，不按内部 provider、worker、job 或节点划分。

## 对外边界

未来无论内部最终怎么实现，公开接口都不应该暴露：

- provider 或上游名称；
- worker / node ID；
- 内部 job / task / attempt ID；
- 缓存、代理和网关路径；
- 内部成本；
- 内部异常类；
- Growth API 凭证或其他 secret。

鉴权目前暂按 `X-API-Key` 设计，但 Key 发放、额度、套餐、计费和真实限流都留到未来实现阶段确定。

只要版本仍是 `0.1.0-draft`，这套契约就可以继续调整。只有等真实服务完成技术对齐和回归测试后，才应该删除 `draft / not live` 标记。
