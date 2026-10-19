"""按 index.html 里实际用到的字符，重新生成 vendor/fonts/ 下的三个 woff2。

网页文字有改动（尤其是新加了中文字）之后运行一次：

    uv run --with fonttools --with brotli python vendor/fonts/subset.py

原始字体（约 43 MB）从 Google Fonts 官方仓库下载到 vendor/fonts/.src/，不进 git。
"""
import os
import urllib.request

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "..", "..", "index.html")
SRC = os.path.join(HERE, ".src")
BASE = "https://raw.githubusercontent.com/google/fonts/main/ofl/"

# (源文件, 输出文件, 保留的字重范围)
JOBS = [
    ("notosanssc/NotoSansSC%5Bwght%5D.ttf", "NotoSansSC.woff2", (400, 700)),
    ("notoserifsc/NotoSerifSC%5Bwght%5D.ttf", "NotoSerifSC.woff2", (700, 900)),
    ("jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf", "JetBrainsMono.woff2", (400, 700)),
]

# 页面字符之外再补上 ASCII 和常用标点，用户打开的 G-code 文件里多半只有这些
EXTRA = "".join(chr(c) for c in range(0x20, 0x7F)) + "，。、；：？！“”‘’（）《》【】—…·°×÷±≈≤≥→←↑↓✓✗▶"


def main():
    text = "".join(sorted(set(open(PAGE, encoding="utf-8").read()) | set(EXTRA)))
    os.makedirs(SRC, exist_ok=True)
    for path, out, (lo, hi) in JOBS:
        src = os.path.join(SRC, os.path.basename(path).replace("%5B", "[").replace("%5D", "]"))
        if not os.path.exists(src):
            print("下载", path)
            urllib.request.urlretrieve(BASE + path, src)
        font = TTFont(src, lazy=False)
        opts = subset.Options()
        opts.layout_features = ["*"]
        opts.name_IDs = ["*"]
        opts.notdef_outline = True
        sub = subset.Subsetter(opts)
        sub.populate(text=text)
        sub.subset(font)  # 先裁字符，再限字重；反过来 fontTools 会报 KeyError
        font = instantiateVariableFont(font, {"wght": (lo, hi)})
        font.flavor = "woff2"
        dst = os.path.join(HERE, out)
        font.save(dst)
        print(f"{out}: {os.path.getsize(dst) // 1024} KB")
    print(f"共 {len(text)} 个字符")


if __name__ == "__main__":
    main()
