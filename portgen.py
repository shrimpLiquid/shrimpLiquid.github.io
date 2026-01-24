from flask import Flask, render_template, send_file, request
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('POTER.html')

@app.route('/process', methods=['POST'])
def process_image():
    file = request.files['image']
    img = Image.open(file.stream)
    
    # Example Pillow operation: Convert to Grayscale
    img = img.convert('L')
    
    # Save to memory buffer instead of disk
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')
