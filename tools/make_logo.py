#!/usr/bin/env python3
"""生成 OAuth 应用图标（512×512 PNG）：橙色渐变圆角方块 + 白色云 + @Y 字样。

Cloudflare 的 public client 必须有 logo（服务端会去 URL 抓图并校验），
这里生成一张纯自制的、不含上游商标元素的图标。
"""
from PIL import Image, ImageDraw, ImageFont

S = 512
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))

# 圆角底：从 #FFA64F 到 #D9700F 的竖向渐变
grad = Image.new("RGB", (S, S))
gd = ImageDraw.Draw(grad)
for y in range(S):
    t = y / (S - 1)
    r = int(0xFF + (0xD9 - 0xFF) * t)
    g = int(0xA6 + (0x70 - 0xA6) * t)
    b = int(0x4F + (0x0F - 0x4F) * t)
    gd.line([(0, y), (S, y)], fill=(r, g, b))

mask = Image.new("L", (S, S), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, S - 1, S - 1], radius=112, fill=255)
img.paste(grad, (0, 0), mask)

d = ImageDraw.Draw(img)

# 云：三个圆 + 底部圆角横条
white = (255, 255, 255, 255)
d.ellipse([120, 250, 268, 398], fill=white)
d.ellipse([196, 196, 372, 372], fill=white)
d.ellipse([300, 258, 420, 378], fill=white)
d.rounded_rectangle([130, 316, 406, 400], radius=42, fill=white)

# 云下小字：YANJIE233
try:
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 46
    )
except OSError:
    font = ImageFont.load_default()
text = "YANJIE233"
bbox = d.textbbox((0, 0), text, font=font)
w = bbox[2] - bbox[0]
d.text(((S - w) / 2, 414), text, font=font, fill=(255, 255, 255, 235))

img.save("relay/logo.png")
print("relay/logo.png", img.size)
