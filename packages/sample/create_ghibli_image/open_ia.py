import os
import base64

# openai imports
from openai import OpenAI

# image convert
from image_convert import convert_to_png

# Use environment variable instead of hardcoded API key
api_key = os.environ.get('OPEN_IA_API_KEY')

def get_vision_response(client: OpenAI, base64_image: str):
    vision_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe photo in detail for converting to Studio Ghibli"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=300
    )
    return vision_response.choices[0].message.content


def dall_e_generating(client: OpenAI, image_description: str) -> str:
    prompt = f"""Convierte esta imagen:{image_description} 
                en una ilustración con un estilo inspirado en la animación japonesa tradicional. 
                Utiliza una paleta de colores suaves y cálidos, con tonos vibrantes pero equilibrados con delicadeza. 
                El fondo debe estar compuesto por elementos pintados a mano con 
                gran detalle: árboles, casas, montañas suaves o cualquier paisaje natural que aporte profundidad.
                Aplica una iluminación difusa, dorada y tenue que transmita calma, nostalgia y un toque de magia serena.
                El personaje debe mantener los rasgos principales de la fotografía original, 
                pero reinterpretados con líneas suaves, ojos expresivos y un aire soñador, 
                como si perteneciera a un mundo lleno de emoción contenida. Añade pequeños 
                detalles del día a día que refuercen la sensación de fantasía encantadora en medio de lo cotidiano, 
                construyendo así una atmósfera envolvente y poética.
    """

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response.data[0].url
 
def generate_image(image: bytes) -> str:
    client = OpenAI(
        api_key=api_key
    )
    # Get the correct image format to DALL-E API
    converted_image_bytes = convert_to_png(image, mode='RGBA')
    base64_image = base64.b64encode(converted_image_bytes).decode('utf-8')
    print("Getting image description...")
    image_description = get_vision_response(client, base64_image)
    print(f"getting image...")
    image_url = dall_e_generating(client, image_description)

    # free memory
    del client

    return image_url
