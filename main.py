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
        lines = f.readlines()

    img = Image.open("bingo.png").copy()
    #img = Image.open(os.path.abspath(__file__).replace("main.py","bingo.png")).copy()

    draw = ImageDraw.Draw(img) 

    try:
        font = ImageFont.truetype("mononoki-Regular.ttf", 45)
        #font = ImageFont.truetype(os.path.abspath(__file__).replace("main.py","mononoki-Regular.ttf"), 45) 
    except:
        font = ImageFont.load_default()
    for XX in range(1):
        for YY in range(2):    
            for X in range(5):
                for Y in range(5):    
                    if not (X == 2 and Y == 2):
                        if lines:
                            text = choice(lines)
                            lines.remove(text)
                            newtext = text.replace(">", "\n")
                            l_count = text.count(">")
                            #=(randint(0,200), randint(0,200), randint(0,200))
                            draw.text(((409*X)+5+int(409/2)+(XX*2048), (409*Y)+5+(200-(l_count*20))+(YY*2048)), newtext,fill=((randint(0,150)), randint(0,150), randint(0,150)), font=font, align="center")
            with open("LINES.txt", encoding="utf8") as f:
                lines = f.readlines()
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    return jsonify({'image': 'data:image/png;base64,' + img_str})
