from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

emoji_map = {
    "Happy": "😊",
    "Sad": "😢",
    "Angry": "😡",
    "Fear": "😨",
    "Surprise": "😲"
}

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    emoji = ""
    
    if request.method == "POST":
        text = request.form["text"]
        vec = vectorizer.transform([text])
        pred = model.predict(vec)[0]
        prediction = pred
        emoji = emoji_map.get(pred, "")
    
    return render_template("index.html", prediction=prediction, emoji=emoji)

if __name__ == "__main__":
    app.run(debug=True)