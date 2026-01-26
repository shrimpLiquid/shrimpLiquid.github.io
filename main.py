from flask import Flask, jsonify
from flask_cors import CORS
from random import choice, randint
from PIL import Image, ImageFont, ImageDraw
import io
import base64

app = Flask(__name__)
CORS(app)

@app.route('/get-processed-image')
def get_image():
    with open("LINES.txt", encoding="utf8") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

    img = Image.open("bingo.png").copy() 
    draw = ImageDraw.Draw(img) 

    try:
        font = ImageFont.truetype("mononoki-Regular.ttf", 45) 
    except:
        font = ImageFont.load_default()

    for X in range(5):
        for Y in range(5):    
            if not (X == 2 and Y == 2):
                if lines:
                    text = choice(lines)
                    lines.remove(text)
                    newtext = text.replace(">", "\n")
                    l_count = text.count(">")
                    draw.text(((409*X)+5, (409*Y)+5+(200-(l_count*20))), newtext,fill=(randint(0,200), randint(0,200), randint(0,200)), font=font, align="left")
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    return jsonify({'image': 'data:image/png;base64,' + img_str})
