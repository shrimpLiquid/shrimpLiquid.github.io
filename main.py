from flask import Flask, render_template_string
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # 1. Open and process the image with Pillow
    img = Image.open('lockin.png') # Ensure this file exists!
    img = img.convert('L')  # Convert to grayscale
    
    # 2. Save the processed image to a byte buffer
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    byte_im = buf.getvalue()

    # 3. Encode the bytes to a Base64 string
    img_base64 = base64.b64encode(byte_im).decode('utf-8')

    # 4. Pass the string to a simple HTML template
    return render_template('porter.html', img_str=img_base64)

if __name__ == '__main__':
    app.run(debug=True)
