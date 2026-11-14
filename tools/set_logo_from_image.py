#!/usr/bin/env python3
"""把用户给的图（灯泡 + 打响指）做成 512×512 的 OAuth 应用图标。

原图是手绘线稿、四周留白不均（下方尤其空），直接缩放会显得偏右下。
做法：先按非白像素求真实包围盒裁掉多余白边，再等比缩到画布的 76% 几何居中，
保证圆形/圆角裁切时左上放射线与右侧折线都不会被切掉。
"""
import sys
from PIL import Image

SRC = sys.argv[1]
OUT = "relay/logo.png"
S = 512
FILL = 0.72  # 内容最大边占画布比例：内切圆半径 256，72% 时四角仍在圆内（留出裁切安全区）
WHITE_CUT = 242  # 高于此亮度视为背景

im = Image.open(SRC).convert("L")
# 非白像素的包围盒
mask = im.point(lambda v: 0 if v >= WHITE_CUT else 255)
bbox = mask.getbbox()
print("content bbox:", bbox, "of", im.size)

art = Image.open(SRC).convert("RGB").crop(bbox)
w, h = art.size
scale = (S * FILL) / max(w, h)
art = art.resize((max(1, round(w * scale)), max(1, round(h * scale))), Image.LANCZOS)

canvas = Image.new("RGB", (S, S), (255, 255, 255))
DX = 6  # 左侧放射线多、视觉重心偏左，整体右移几像素平衡
canvas.paste(art, ((S - art.width) // 2 + DX, (S - art.height) // 2))
canvas.save(OUT)
print("written", OUT, canvas.size, "art", art.size)
