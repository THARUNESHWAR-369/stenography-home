import os
from flask import Flask, render_template
# from modes.Image.image import image
# # from modes.Audio.audio import audio
# # from modes.Text.text import text
# from modes.Video.video import video


# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# app = Flask(__name__)
# app.secret_key = "<Your Key>"

# app.register_blueprint(image, url_prefix="/image")
# # app.register_blueprint(audio, url_prefix="/audio")
# # app.register_blueprint(text, url_prefix="/text")
# app.register_blueprint(video, url_prefix="/video")

@app.route("/")
def home():
    # return render_template("home.html")
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True)