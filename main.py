from flask import Flask, jsonify
from flask_cors import CORS
from PIL import Image, ImageFont, ImageDraw
import io
import base64

app = Flask(__name__)
CORS(app)
file = open("LINES.txt",encoding="utf8")
lines = file.readlines()  
image = Image.open("bingo.png") 
@app.route('/get-processed-image')
def get_image():
    # 1. Open the local image file on the server
    draw = ImageDraw.Draw(image) 

    font = ImageFont.truetype("mononoki-Regular.ttf", 45) 
    
    for X in range(5):
        for Y in range(5):    
            if not X == Y == 2:
                text = choice(lines)
                lines.remove(text)
                newtext=text.replace(">","\n")
                l = text.count(">")
                draw.text(((409*X)+5, (409*Y)+5+(200-(l*20))), newtext,fill=(randint(0,200),randint(0,200),randint(0,200)), font = font, align ="left") 

    buf = io.BytesIO()
    img.save(buf, format='PNG')
    img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    return jsonify({'image': 'data:image/png;base64,' + img_str})
