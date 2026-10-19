# G-code 实验室 · GcodeLAB

读懂切片软件写给 3D 打印机（FDM / FFF）的每一行 G-code。

一个单文件网页，直接用浏览器打开 `index.html` 即可使用，无需安装或构建。

## 内容

- **课程**：22 节课，分为基础、挤出、温度、读懂切片文件、多材料、进阶六个部分，每节配图示、常见错误和小测
- **模拟器**：逐行执行 G-code，俯视图与 3D 视图查看路径，支持打开 `.gcode` / `.gcode.3mf`，自动检查常见问题
- **耗材**：20 种常见耗材的打印温度、干燥和性能对比，附多材料结合表
- **多材料**：逐行拆解一次换料，讲解冲刷、渗料、待机温度和喷头偏移
- **切片软件**：PrusaSlicer、OrcaSlicer / Bambu Studio、Cura 与 Klipper 宏写法对照
- **练习**：编写代码自动判分，另有选择题
- **速查表**：常用指令的作用、示例和固件支持情况

支持中文 / English 切换，以及浅色 / 深色模式。

## 使用

```bash
open index.html
```

或部署到任意静态托管（如 GitHub Pages）。

## 依赖

所有文件都随站点一起发布，不请求任何外部服务器（不用 Google Fonts，也不用 CDN），国内外访问一致。

- `vendor/fonts/`：Noto Serif SC、Noto Sans SC、JetBrains Mono，按页面用字裁剪过。改了网页文字后需要重新生成，方法见 [vendor/fonts/README.md](vendor/fonts/README.md)
- `vendor/three/`：[three.js](https://threejs.org/) r128 及 OrbitControls、Line2 系列，只在打开 3D 视图时加载

学习进度和主题、语言选择只保存在浏览器本地（localStorage）。
