# Spam Detection API

This project implements a REST API for classifying emails as spam or not spam using NLP techniques.

## Features
- Train multiple models (Decision Tree, Logistic Regression, Random Forest, Multinomial Naive Bayes).
- Hyperparameter tuning with MLflow logging.
- REST API endpoints for model parameters, training, and prediction.
- Dockerized application with MLflow UI.

### Clone the repository:
   git clone git@github.com:Rajesh-Lohani/mlops_squad.git
   cd mlops_squad

## How to run the application using Docker image – available in docker hub :

1.	Pull the docker image using below command :

docker pull rajeshlohani/mlops_squad:latest

2.	Run the Docker Container:

docker run -p 5000:5000 -p 5001:5001 rajeshlohani/mlops_squad

3.	Applications :
Mlflow UI url : http://localhost:5001/
REST API url : http://localhost:5000/

4.	Endpoints
a.	GET /best_model_parameters: Get the best model's hyperparameters.

Sample url : http://127.0.0.1:5000/best_model_parameters

Output :

{
    "best_model_parameters": {
        "alpha": 0.1,
        "class_prior": null,
        "fit_prior": true,
        "force_alpha": "warn"
    }
}


b.	POST /train: Train the model with new data.

Sample url : http://127.0.0.1:5000/train
Input dataset :

{
  "sms": ["Free entry in 2 a wkly comp", "Hey there, how are you?", "Win a brand new car!", "Can we meet tomorrow?"],
  "label": ["spam", "ham", "spam", "ham"]
}


Output :

{
    "accuracy": 96.0,
    "message": "Model trained successfully"
}


c.	POST /predict: Predict whether a given SMS is spam or not.

Sample url : http://127.0.0.1:5000/predict

Input body : 

{
    "sms":"Hello! you won 1000"
}

Output :

{
    "prediction": "spam"
}
