# failgate-demo

[FailGate](#关于-failgate) 的公开演示仓库。这是一个很小的 Python 包（配置解析、URL slug、序列工具），里面**故意留了几个 bug**。这些 bug 的 issue 会由 FailGate 处理，处理过程和结果都公开在这里。

*A public demo for FailGate: a tiny Python package with deliberate bugs. Issues filed here are handled by the FailGate bot, and every step is visible in the issue and PR threads.*

## 在这里能看到什么

1. **出题**：有人报告 bug 后，FailGate 在 issue 创建时的代码上写出一个**在本仓库里会失败的 pytest 测试**。一个独立的判定器确认这个测试失败的方式和 issue 描述的一致。
2. **封存**：这个测试作为"考卷"被封存。汇总评论里附着**证据收据**：测试的 sha256、代码提交、Python 和 pytest 版本、运行命令、失败签名、每次运行的结果。任何人都可以重算哈希，核对收据有没有被改过。
3. **阅卷**（开发中）：声称修复了某个 issue 的 PR，会用封存的那份考卷来核验。核验分三层：修复前失败、修复后通过；测试没有被删改或跳过；相关的已有测试没有新的失败。
4. **考卷强度**（开发中）：用变异测试检查这份考卷够不够严，能不能区分"真修好"和"症状消失"。

## 故意留下的 bug

| 模块 | bug | 特点 |
|---|---|---|
| `failgate_demo.config` | `[section]` 之前的键会触发 `KeyError: None` | 有堆栈的崩溃 |
| `failgate_demo.text` | `slugify("Hello,  World!")` 得到 `hello---world` | 行为错误，没有堆栈（0.3.0 引入的回归） |
| `failgate_demo.seq` | `unique()` 对字符串不保持原来的顺序 | 偶发：结果随哈希种子变化 |

**请不要提交修复这些 bug 的 PR**：它们是演示素材，修复 PR 会由 FailGate 的演示流程创建。

## 本地运行

```bash
pip install -e . pytest
pytest -q
```

## 关于 FailGate

FailGate 是 bug 的验收层：修复谁都能写，考卷必须可信。它不和修复 Agent 比谁修得好，而是在修复之前先定下一份会失败、并且被封存的验收测试，再用它中立地核验任何修复，不管修复出自维护者、贡献者，还是 Claude Code、Codex、Copilot 这类 AI Agent。

本仓库的 issue 和评论由 GitHub App `failgate-dev-jian` 发出，运行在作者自己的机器上（自托管，模型用 DeepSeek）。

## License

MIT
