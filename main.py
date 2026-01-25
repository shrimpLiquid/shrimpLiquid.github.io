from flask import Flask, jsonify
from flask_cors import CORS
from PIL import Image
import io
import base64

app = Flask(__name__)
CORS(app)

@app.route('/get-processed-image')
def get_image():
    # 1. Open the local image file on the server
    img = Image.open('lockin.png') 
    
    # 2. Process it
    img = img.convert('L') # Grayscale filter
    
    # 3. Encode to Base64
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    return jsonify({'image': 'data:image/png;base64,' + img_str})
