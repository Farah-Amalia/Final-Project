# Bank Marketing Prediction

This project aims to predict the success of telemarketing calls for selling bank long-term deposits. Marketing selling campaigns constitute a typical strategy to enhance business. Companies use direct marketing when targeting segments of customers by contacting them to meet a specific goal. Centralizing customer remote interactions in a contact center eases operational management of campaigns. Such centers allow communicating with customers through various channels, telephone (fixed-line or mobile) being one of the most widely used. Marketing operationalized through a contact center is called telemarketing due to the remoteness characteristic. 

## I. Data
The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.

There are 21 features in this dataset, which contains bank client data, previous campaign history, social economic attributes, and many more.

Source: UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)

## II. Pre-processing
This step involves handling outlier and transforming categorical data into numerical data using one hot encoding.

## III. Modelling
I used Logistic Regression, Decision Tree Classifier, Random Forest Classifier, Gradient Boosting Classifier, SVC, KNeighbors Classifier, MLP Classifier, and Gaussian Naive Bayes as base models. Then, I chose two models based on the highest recall score of each model to tune the hyperparameters.

## IV. Hypermarameters Tuning
