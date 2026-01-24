import base64
import io
from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    image_data = None
    if request.method == 'POST':
        file = request.files['image']
        img = Image.open(file.stream)
        img = img.convert('L') # Example processing: Grayscale
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        base64_img = base64.b64encode(img_io.getvalue()).decode('utf-8')
        image_data = f"data:image/png;base64,{base64_img}"
    return render_template('index.html', image_data=image_data)

if __name__ == '__main__':
    app.run(debug=True)
