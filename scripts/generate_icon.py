from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


ASSET_DIR = Path("assets")
ICON_PATH = ASSET_DIR / "AvtoVinchickTG.ico"
PNG_PATH = ASSET_DIR / "AvtoVinchickTG.png"


def make_icon(size: int = 1024) -> Image.Image:
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    shadow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    pad = int(size * 0.09)
    shadow_draw.rounded_rectangle(
        (pad, pad, size - pad, size - pad),
        radius=int(size * 0.23),
        fill=(0, 0, 0, 95),
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(int(size * 0.025)))
    image.alpha_composite(shadow, (0, int(size * 0.025)))

    draw.rounded_rectangle(
        (pad, pad, size - pad, size - pad),
        radius=int(size * 0.23),
        fill=(35, 161, 226, 255),
    )
    draw.rounded_rectangle(
        (pad, pad, size - pad, size - pad),
        radius=int(size * 0.23),
        outline=(20, 109, 181, 255),
        width=int(size * 0.025),
    )

    # Telegram paper-plane mark.
    plane = [
        (int(size * 0.18), int(size * 0.48)),
        (int(size * 0.80), int(size * 0.23)),
        (int(size * 0.68), int(size * 0.78)),
        (int(size * 0.50), int(size * 0.60)),
        (int(size * 0.40), int(size * 0.72)),
        (int(size * 0.36), int(size * 0.55)),
    ]
    draw.polygon(plane, fill=(255, 255, 255, 255))
    draw.line(
        [
            (int(size * 0.36), int(size * 0.55)),
            (int(size * 0.80), int(size * 0.23)),
            (int(size * 0.50), int(size * 0.60)),
        ],
        fill=(190, 235, 255, 255),
        width=int(size * 0.018),
        joint="curve",
    )

    # Filter/check badge.
    badge_box = (
        int(size * 0.55),
        int(size * 0.55),
        int(size * 0.87),
        int(size * 0.87),
    )
    draw.ellipse(badge_box, fill=(24, 201, 137, 255), outline=(255, 255, 255, 255), width=int(size * 0.025))
    funnel = [
        (int(size * 0.62), int(size * 0.64)),
        (int(size * 0.81), int(size * 0.64)),
        (int(size * 0.74), int(size * 0.72)),
        (int(size * 0.74), int(size * 0.80)),
        (int(size * 0.69), int(size * 0.80)),
        (int(size * 0.69), int(size * 0.72)),
    ]
    draw.polygon(funnel, fill=(255, 255, 255, 255))
    return image


def main() -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    icon = make_icon()
    icon.save(PNG_PATH)
    icon.save(
        ICON_PATH,
        sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
    )
    print(ICON_PATH)


if __name__ == "__main__":
    main()
