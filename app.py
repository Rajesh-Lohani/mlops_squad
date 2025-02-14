from flask import Flask, request, jsonify
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

app = Flask(__name__)

with open("model/spam_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


# Endpoint to get the best model parameters
@app.route("/best_model_parameters", methods=["GET"])
def best_model_parameters():
    return jsonify({"best_model_parameters": model.get_params()})

# Endpoint to make predictions
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data["sms"]
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)
    return jsonify({"prediction": "spam" if prediction[0] == 1 else "not spam"})

# Endpoint to trigger model training
@app.route("/train", methods=["POST"])
def train():
    # Get data from request : We can send single sms aur multiple sms for training
    data = request.json
    # Create a DataFrame from the input data
    df = pd.DataFrame({"text": data["sms"], "label": data["label"]})

    # Preprocess data
    df["label"] = df["label"].map({"ham": 0, "spam": 1})
    X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

    # Vectorize text
    vectorizer = TfidfVectorizer(stop_words="english")
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Train the model
    model = MultinomialNB()
    model.fit(X_train_vec, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)

    # Log experiment with MLflow
    mlflow.set_experiment("Spam Detection")
    with mlflow.start_run():
        mlflow.log_param("model_type", "MultinomialNB")
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(model, "model")

    # Save the model and vectorizer using Pickle
    with open("model/spam_model.pkl", "wb") as f:
        pickle.dump(model, f)
    with open("model/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    return jsonify({"message": "Model trained successfully", "accuracy": accuracy})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)