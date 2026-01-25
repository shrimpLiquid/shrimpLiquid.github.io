from flask import Flask, request, jsonify
from flask_cors import CORS  # You'll need: pip install flask-cors
from PIL import Image
import io
import base64

app = Flask(__name__)
CORS(app) # This allows your GitHub Page to talk to this script

@app.route('/process', methods=['POST'])
def process_image():
    # 1. Get the image from the JS request
    data = request.json['image']
    header, encoded = data.split(",", 1)
    img_data = base64.b64decode(encoded)
    
    # 2. Process with Pillow
    img = Image.open(io.BytesIO(img_data))
    img = img.convert('L') # Example: Grayscale
    
    # 3. Save back to Base64
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    result_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    return jsonify({'processed_image': 'data:image/png;base64,' + result_base64})

if __name__ == '__main__':
    app.run()
