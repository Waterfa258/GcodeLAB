# 字体

| 文件 | 来源 | 字重 |
|---|---|---|
| `NotoSansSC.woff2` | [Noto Sans SC](https://fonts.google.com/noto/specimen/Noto+Sans+SC) | 400–700 |
| `NotoSerifSC.woff2` | [Noto Serif SC](https://fonts.google.com/noto/specimen/Noto+Serif+SC) | 700–900 |
| `JetBrainsMono.woff2` | [JetBrains Mono](https://www.jetbrains.com/lp/mono/) | 400–700 |

都是可变字体，只保留了 `index.html` 里实际出现的字符（外加 ASCII 和常用标点），所以三个文件加起来不到 1 MB。
页面里没有的字，比如用户打开的 G-code 文件注释里的生僻字，会自动退回系统字体显示。

**改了网页文字之后**（尤其是加了新的中文字），重新生成一次：

```bash
uv run --with fonttools --with brotli python vendor/fonts/subset.py
```

许可：均为 SIL Open Font License 1.1，见 `OFL-Noto.txt`（Noto Sans SC 与 Noto Serif SC 同一份）和 `OFL-JetBrainsMono.txt`。
