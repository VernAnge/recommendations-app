# Product Recommendation App

## Description

This project involves creating a product recommendation app using Python and Dash. The application can be applied to any large set of data and it provides personalised recommendations.

## Data Cleaning

The data cleaning process involves:

1. Reading the data from the CSV file.
2. Handling missing values by filling or dropping them.
3. Standardizing text formats to ensure consistency.
4. Removing duplicate records.

## Data Filtering

The data is filtered based on customer segmentation, interaction type, and activity status to provide relevant recommendations.

## Bootstrap Method

Bootstrap sampling is a resampling technique used to create multiple samples from a single dataset. It is particularly useful in scenarios where the dataset size is small or when you want to estimate the sampling distribution of a statistic. By generating multiple bootstrap samples, we can increase the dataset size and perform more robust analysis and modeling. In this project, we used bootstrap sampling to create a larger dataset for our recommendation system.

## Recommendation System

The recommendation system implemented in this project uses user-user cosine similarity to generate personalized product recommendations. The steps involved are as follows:

1. **Data Loading** : Load the cleaned interaction data and create interaction matrices for training and testing.
2. **Cosine Similarity Calculation** : Compute the cosine similarity between users based on their interaction patterns.
3. **Recommendation Generation** : For a given user, identify the most similar users and recommend products that these users have interacted with.

The recommendation system ensures that the recommendations are personalized and relevant based on the user's past interactions and the interactions of similar users.

## Running the App

In the terminal:

* navigate to the directory where your project is located.
* Create a virtual environment by typing: *$ python -m venv venv*
* Activate the virtual environment by typing: *$ source venv/bin/activate*  # On Windows use `venv\Scripts\activate`
* Then install all of the requirements: *$ pip install -r requirements.txt*
* Then run the application by entering the command in the following order:
  * *$ python3 clean.py*
  * *$ python3 filter.py*
  * *$ python3 bootstrap.py*
  * *$ python3 rec_model.py*
  * *$ python3 app.py*
  * *$ python3 bi_dash.py*
* When you are done, close the virtual environment by typing: *$ deactivate*

NOTE:

1. Ensure all required packages are installed.
2. Place your `data.csv` file in the same directory as the scripts.
3. Run `python app.py` to start the client Dash app and `bi_dash.py` to run the management analytical Dash app.

## Files

- `clean.py`: Script for cleaning the data.
- `filter.py`: Script for filtering the data.
- `bootstrap.py: `Script for generating additional data from the original dataset.
- `rec_model.py:` Script making the recommendation by training a model on the dataset.
- `app.py`: Main script for running the client Dash app.
- `bi_dash.py`: Main script for running the business Dash app.
- `products.txt`: List of FNB products.
- `users.txt`: List of user_id's used to test `rec_model.py`
- `assets/style.css: `Contains the style guidelines for the Dash apps.

## Conclusion

This repository provides a comprehensive solution for data cleaning, filtering, bootstrap sampling, and creating a BI Dashboard and recommendation system. The methods implemented ensure robust data analysis and personalized recommendations, making it a valuable tool for business intelligence and customer insights.
