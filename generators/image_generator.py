import requests
from PIL import Image, ImageDraw
from io import BytesIO
from pathlib import Path

def generate_feature_image(title):
    url = f"https://image.pollinations.ai/prompt/{title}"
    response = requests.get(url, timeout=60)

    img = Image.open(BytesIO(response.content)).convert("RGB")

    draw = ImageDraw.Draw(img)
    draw.text((30, 30), title[:60], fill=(255,255,255))

    output = Path("images/featured/feature.webp")
    img.save(output, "WEBP")

    return output