import flask
import joblib
import text_wrangling_util
import json

app = flask.Flask(__name__)

# Load model
try:
    model = joblib.load('movie_genre_classifier.joblib')
except FileNotFoundError:
    print("Model specification \"movie_genre_classifier.joblib\" not found.")
    print("Download the model or retrain the network using Training.ipynb notebook.")
    exit()

@app.route('/api', methods=['POST'])
def predict():
    input_data = flask.request.get_json(force=True)

    # Check and process the data
    if not input_data["title"] or not input_data["description"]:
        print("Please provide both the title and the description of the movie.")
        exit()

    if input_data["title"] == "" or input_data["description"] == "":
        print("Title and description must not be empty.")
        exit()

    input_text = text_wrangling_util.prepare_input_text(input_data["title"], input_data["description"])

    if input_text == [""]:
        print("Title and description must contain letters from the English alphabet...")
        exit()

    # Make the prediction
    Y_pred_prob = model["pipeline"].predict_proba(input_text)[0]

    # Display genres in the order of descending probabilities
    genres = [genre for (prob, genre) in sorted(zip(Y_pred_prob, model["genres"]))[::-1] if prob > model["threshold"]]

    output_dict = {"title": input_data["title"], "description": input_data["description"], "genre": ", ".join(genres)}

    return output_dict

if __name__ == "__main__":
    app.run(port=5000, debug=True)
