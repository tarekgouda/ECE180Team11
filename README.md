# ECE 180 Team 11

## Get (git) the repository
`git clone https://github.com/tarekgouda/ECE180Team11`

## Introduction
As part of our team project for ECE 180: Python for Data Analysis, we are investigating the data provided by the [Yelp Open Dataset](https://www.yelp.com/dataset). Yelp is a website and mobile app that helps users find local businesses and services based on crowd-sourced reviews. Many people look to Yelp for ideas on what to eat, drink, and do. We are particularly interested in this dataset because of its many rich features for exploring data analysis.

## Dataset
Contained in the dataset folder are **6 JSON** files:
- review.json
- business.json
- photos.json
- user.json
- tip.json
- checkin.json

## Research Questions and Purpose:
After exploring the datasets, we ultimately chose the **business.josn** file to focus our analysis on. This file contains business data including location data, attributes, and categories. We chose this because many different features pertaining to each business could be useful. For instance, attributes such as location, wheelchair accessbility, happy hours, and parking could be useful in predicting businesses' **ratings (1-5 stars)**. Some questions we have considered are:
- Do the number or type of service offered by businesses affect rating?
- Can we predict the ratings of businesses from different attributes?
- What attributes contribute the most to rating?

The **purpose** of the project is to allow businesses to increase their ratings by focusing/improving on the attributes most correlated with rating. We do this by creating visualizations that would help us understand the data on a broader scale and implement models for predicting business rating based on specific features.

## Dependencies
The following libraries/modules are used for pre-processing, plotting, and prediction:
- [Plotly](https://plot.ly/python)
- [Matplotlib](https://matplotlib.org)
- [NumPy](http://www.numpy.org/)
- [*pandas*](https://pandas.pydata.org/)
- [scikit-learn](http://scikit-learn.org/)
- [JSON](https://docs.python.org/2/library/json.html)

## Models
1. Global Average
2. Linear Regression
3. Decision Tree Regression

## Author
- Binh Nguyen
