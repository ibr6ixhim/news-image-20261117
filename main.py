#!/usr/bin/env python3
"""make.fun entry: Sum up 17 November 2026 world news in one image. Writes /output/entry.png"""
import os
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False):
    for path in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def main():
    W, H = 1024, 1024
    img = Image.new("RGB", (W, H), "#0f172a")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 80], fill="#1e293b")
    draw.text((24, 18), "THE WORLD IN ONE DAY", fill="#f8fafc", font=get_font(28, True))
    draw.text((24, 52), "Tuesday 17 November 2026  ·  Global Edition", fill="#94a3b8", font=get_font(14))
    draw.rectangle([0, 80, W, 86], fill="#ef4444")
    y = 100
    stories = [
        ("CONFLICT", "Ukraine strikes Kerch Bridge", "Ukrainian drones/missiles hit Crimean Bridge second day. Section collapses into Kerch Strait. Zelenskyy: unprecedented multi-week op."),
        ("MIDDLE EAST", "Iran drones hit Bahrain", "Iran fires drones at US radar (Sheikh Isa base). Bahrain intercepts. 3rd US carrier arrives in region."),
        ("DIPLOMACY", "Trump starts Asia trip", "Trump lands Philippines. Quad meets Manila. Trilateral summit with Xi + Putin planned Shenzhen."),
        ("GEOPOLITICS", "Carrier pressure on Iran", "Third American carrier arrives Middle East. Houthis claim drones toward Saudi pipelines."),
        ("EUROPE", "EU return hub in Rwanda", "DE/AT/DK/GR/NL announce migrant return hub in Rwanda for 2027. Rights groups condemn."),
        ("TECH", "Outages & AI chip rules", "Digital infra outages spark concern. US tightens remote access to overseas AI data centres."),
        ("WORLD", "Also today", "Israeli Knesset new speaker. West Bank settler violence. Russia–Ukraine intensifies. APEC security."),
    ]
    colors = {"CONFLICT":"#f87171","MIDDLE EAST":"#f87171","DIPLOMACY":"#60a5fa","GEOPOLITICS":"#60a5fa","EUROPE":"#fbbf24","TECH":"#fbbf24","WORLD":"#4ade80"}
    for tag, head, body in stories:
        draw.text((24, y), tag, fill=colors[tag], font=get_font(12, True))
        y += 18
        draw.text((24, y), head, fill="#f1f5f9", font=get_font(18, True))
        y += 24
        words = body.split()
        line = ""
        for w in words:
            test = (line + " " + w).strip()
            if draw.textlength(test, font=get_font(13)) < W - 48:
                line = test
            else:
                draw.text((24, y), line, fill="#cbd5e1", font=get_font(13))
                y += 18
                line = w
        if line:
            draw.text((24, y), line, fill="#cbd5e1", font=get_font(13))
            y += 18
        y += 12
    draw.rectangle([0, H-40, W, H], fill="#1e293b")
    draw.text((24, H-28), "make.fun · news-image-20261117 · open sources", fill="#64748b", font=get_font(11))
    os.makedirs("/output", exist_ok=True)
    img.save("/output/entry.png", "PNG", optimize=True)
    print("Wrote /output/entry.png")

if __name__ == "__main__":
    main()
