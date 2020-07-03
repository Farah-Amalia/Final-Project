# Bank Marketing Prediction

This project aims to predict the success of telemarketing calls for selling bank long-term deposits. Marketing selling campaigns constitute a typical strategy to enhance business. Companies use direct marketing when targeting segments of customers by contacting them to meet a specific goal. Centralizing customer remote interactions in a contact center eases operational management of campaigns. Such centers allow communicating with customers through various channels, telephone (fixed-line or mobile) being one of the most widely used. Marketing operationalized through a contact center is called telemarketing due to the remoteness characteristic. 

## I. Data
The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.

There are 21 features in this dataset, which contains bank client data, previous campaign history, social economic attributes, and many more.

Source: UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)

## II. Pre-processing
This step involves handling outlier and transforming categorical data into numerical data using one hot encoding.

## III. Modelling
I used Logistic Regression, Decision Tree Classifier, Random Forest Classifier, Gradient Boosting Classifier, SVC, KNeighbors Classifier, MLP Classifier, and Gaussian Naive Bayes as base models. Then, I chose two models based on the highest precision score of each model to tune the hyperparameters. Below are the summary of the base model result.
| model | precision_train | recall_train | accuracy_train | precision_test | recall_test | accuracy_test |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| LogisticRegression | 0.813688 | 0.813688 | 0.797226 | 0.298805 | 0.547445 | 0.797766 |
| DecisionTreeClassifier | 0.998183 | 0.998183 | 0.996430 | 0.288642 | 0.352450 | 0.823501 |
| RandomForestClassifier | 0.996548 | 0.996548 | 0.996430 | 0.462545 | 0.405631 | 0.875941 |
| GradientBoostingClassifier | 0.890571 | 0.890571 | 0.871929 | 0.381877 | 0.492179 | 0.848143 |
| SVC | 0.717827 | 0.717827 | 0.717961 | 0.256252 | 0.694473 | 0.729789 |
| KNeighborsClassifier | 0.845459 | 0.845459 | 0.903635 | 0.236429 | 0.613139 | 0.724448 |
| MLPClassifier | 0.990074 | 0.990074 | 0.722676 | 0.647887 | 0.047967 | 0.886137 |
| GaussianNB | 0.804485 | 0.804485 | 0.803871 | 0.276170 | 0.547445 | 0.780286 |

Based on Precision Score and Accuracy Score, the top 3 models are:

1. MLP / Neural Network Classifier
2. Random Forest Classifier
3. Gradient Boosting Classifier

## IV. Hypermarameters Tuning
### 1. MLP Classifier
Below are the hyperparameters of MLPClassifier that I have tuned.
```
'hidden_layer_sizes': [(50,50,50), (50,100,50), (100,)],
'activation': ['tanh', 'relu', 'logistic'],
'solver': ['sgd', 'adam', 'lbfgs'],
'alpha': [0.05, 0.06, 0.07, 0.08, 0.09, 0.1],
'learning_rate': ['constant','adaptive']
```
From the hyperparameter tuning, below are the results of classification report.
| Model | Precision | Recall | Accuracy |
| ----- | ----- | ----- | ----- |
| MLP Classifier | 0.37 | 0.39 | 0.85 |

### 2. Random Forest Classifier
Below are the hyperparameters of MLPClassifier that I have tuned.
```
'max_depth':[10,20,30,40,50,],
'min_samples_split':[1,2,3,4,5,6,7,8,9,10,50,100,500],
'min_samples_leaf': [0.1,1,2,3,4,5,500,1000,1500,2000,2500,3000,3500,4000],
'n_estimators': [1, 100, 500, 800, 1500]
```

From the hyperparameter tuning, below are the results of classification report.
| Model | Precision | Recall | Accuracy |
| ----- | ----- | ----- | ----- |
| Random Forest Classifier | 0.46 | 0.39 | 0.88 |

## V. Deployment
The random forest classifier model that has been fitted are deployed to the dashboard to predict the success of bank marketing in the future. The dashboard is displayed below.
![Deployment](/ss.png)

## VI. Conclusion
Based on the analysis, we can conclude that random classifier is able to predict the success of bank marketing with 88% accuracy score. For further analysis, we may need to adjust the threshold or do further tuning to increase the precision and accuracy score.
