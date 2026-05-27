import requests
from PIL import Image, ImageDraw
from io import BytesIO
from pathlib import Path

def generate_feature_image(title):
    url = f"https://image.pollinations.ai/prompt/{title.replace(' ', '%20')}"
    response = requests.get(url, timeout=60)
    response.raise_for_status()

    img = Image.open(BytesIO(response.content)).convert("RGB")

    draw = ImageDraw.Draw(img)
    draw.text((30, 30), title[:60], fill=(255, 255, 255))

    output = Path("images/featured/feature.webp")
    output.parent.mkdir(parents=True, exist_ok=True)  # FIX: create folder if missing
    img.save(output, "WEBP")

    return output
