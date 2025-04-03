from PIL import Image
import io

def convert_to_png(image_bytes, mode='RGBA'):
    
    if mode not in ['RGBA', 'LA', 'L']:
        raise ValueError("Mode must be one of 'RGBA', 'LA', or 'L'")
    
    # Open and convert the image from bytes
    img = Image.open(io.BytesIO(image_bytes))
    img_converted = img.convert(mode)
    
    # Save to bytes buffer
    buffer = io.BytesIO()
    img_converted.save(buffer, format='PNG')
    
    # Get the bytes
    img_bytes = buffer.getvalue()
    
    return img_bytes