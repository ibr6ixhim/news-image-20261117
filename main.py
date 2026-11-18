#!/usr/bin/env python3
"""
make.fun entry: Sum up 17 November 2026 world news in one image.
Writes /output/entry.png
"""
import os
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def main():
    W, H = 1200, 1600
    img = Image.new("RGB", (W, H), "#0f172a")  # dark navy
    draw = ImageDraw.Draw(img)

    # Header bar
    draw.rectangle([0, 0, W, 110], fill="#1e293b")
    title_font = get_font(42, bold=True)
    date_font = get_font(22)
    draw.text((40, 28), "THE WORLD IN ONE DAY", fill="#f8fafc", font=title_font)
    draw.text((40, 75), "Tuesday  17 November 2026  ·  Global Edition", fill="#94a3b8", font=date_font)

    # Accent line
    draw.rectangle([0, 110, W, 116], fill="#ef4444")

    y = 140
    section_font = get_font(18, bold=True)
    body_font = get_font(20)
    small_font = get_font(16)

    stories = [
        ("🔴 CONFLICT", "Ukraine strikes Kerch Bridge",
         "Ukrainian drones and missiles hit the Crimean Bridge for a second day. A section of the road span collapses into the Kerch Strait. Zelenskyy calls it an 'unprecedented operation' prepared over weeks."),
        ("🔴 MIDDLE EAST", "Iran resumes strikes on Bahrain",
         "Iran fires drones at a U.S. military radar system in Bahrain (Sheikh Isa base). Bahrain intercepts the attack. Third U.S. aircraft carrier arrives in the region amid rising tensions."),
        ("🔵 DIPLOMACY", "Trump begins Asia trip",
         "President Trump lands in the Philippines on the first leg of a three-day Asia tour. Quad leaders meet in Manila. Historic trilateral summit with Xi Jinping and Vladimir Putin planned in Shenzhen."),
        ("🔵 GEOPOLITICS", "Third U.S. carrier to Middle East",
         "A third American aircraft carrier arrives in the Middle East as pressure on Iran continues. Houthi forces claim drone attacks toward Saudi pipeline facilities."),
        ("🟡 EUROPE", "EU migrant return hub in Rwanda",
         "Germany, Austria, Denmark, Greece and the Netherlands announce a 'return hub' in Rwanda for rejected asylum seekers, planned to open in 2027. Human-rights groups condemn the plan."),
        ("🟡 TECH / INFRA", "Digital outages & AI controls",
         "Series of outages raise concern over digital infrastructure stability. U.S. tightens remote-access rules for overseas data centres using advanced AI chips. Nvidia scrutiny continues."),
        ("🟢 OTHER", "Around the world",
         "Israeli Knesset elects new speaker. Settler violence reported in West Bank. Russia–Ukraine fighting intensifies. APEC summit security tightens in Shenzhen."),
    ]

    for tag, headline, body in stories:
        # Tag
        draw.text((40, y), tag, fill="#f87171" if "🔴" in tag else ("#60a5fa" if "🔵" in tag else ("#fbbf24" if "🟡" in tag else "#4ade80")), font=section_font)
        y += 28
        # Headline
        draw.text((40, y), headline, fill="#f1f5f9", font=get_font(26, bold=True))
        y += 36
        # Body – wrap roughly
        words = body.split()
        line = ""
        for w in words:
            test = (line + " " + w).strip()
            if draw.textlength(test, font=body_font) < W - 80:
                line = test
            else:
                draw.text((40, y), line, fill="#cbd5e1", font=body_font)
                y += 28
                line = w
        if line:
            draw.text((40, y), line, fill="#cbd5e1", font=body_font)
            y += 28
        y += 22  # gap between stories

    # Footer
    draw.rectangle([0, H - 70, W, H], fill="#1e293b")
    draw.text((40, H - 48), "make.fun entry  ·  news-image-20261117  ·  AI-generated summary of open sources", fill="#64748b", font=small_font)

    os.makedirs("/output", exist_ok=True)
    out_path = "/output/entry.png"
    img.save(out_path, "PNG")
    print(f"Wrote {out_path}")

if __name__ == "__main__":
    main()
