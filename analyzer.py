from PIL import Image
import numpy as np
import time

def analyze_chart(image_path):
    start = time.time()
    try:
        img = Image.open(image_path).convert('L')
        img = img.resize((300, 300))
        arr = np.array(img, dtype=np.float32)
    except Exception:
        return {"signal": "ERROR", "confidence": 0, "time_ms": 0}

    top    = arr[:150, :].mean()
    bottom = arr[150:, :].mean()
    left   = arr[:, :150].mean()
    right  = arr[:, 150:].mean()

    if bottom > top and right > left:
        signal = "BUY"
        confidence = min(95, int(60 + (bottom - top) * 0.5))
    elif top > bottom and left > right:
        signal = "SELL"
        confidence = min(95, int(60 + (top - bottom) * 0.5))
    else:
        signal = "HOLD"
        confidence = 40

    elapsed_ms = (time.time() - start) * 1000
    return {"signal": signal, "confidence": confidence, "time_ms": round(elapsed_ms, 2)}
