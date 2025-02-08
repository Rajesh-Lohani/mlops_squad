# MLOPS Squad

## Objective:

Students must develop a Machine Learning (ML) model for one of the following use cases:

1. Sentiment Analysis on Movie Reviews – Use NLP techniques (e.g., BERT, TF-IDF + classifiers) on the IMDB dataset.
2. Handwritten Digit Recognition – Implement an ensemble model to classify digits from the MNIST dataset.
3. Email Spam Detection – Use NLP techniques to classify emails as spam or not using the SPAM Detect dataset.
   
## Project Requirements:
1. Train an ML model using any algorithm and approach.
2. Implement hyperparameter tuning and track experiments using MLflow.
3. Develop a REST API with the following endpoints:
   - GET /best_model_parameter – Fetch best model parameters.
   - POST /prediction – Make predictions.
   - POST /training – Train the model.
4. Create a Docker container for the backend API and push it to Docker Hub.
5. Maintain an experiment artifact in a GitHub repository.
   
## Evaluation Criteria:
1. Working REST API with correct functionality.
2. Proper logging of MLflow experiments in the GitHub repository.
3. A Docker image showcasing both the MLflow UI and REST API.
   
## Guidelines:
1. All members must contribute to a single GitHub repository with valid commit history.
2. Plagiarism is strictly prohibited – Do not copy code from ChatGPT or other sources.
3. Do not push datasets to GitHub.
