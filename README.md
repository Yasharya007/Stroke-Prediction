# Stroke-Prediction
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1B2ageylGg7KOqaDlx0I7oB_mwf_FWBQ-?usp=drive_link)
## Overview
- Stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths. The given dataset can be used to predict whether a patient is likely to get a stroke based on the input parameters like gender, age, bmi value, various diseases, and smoking status.
## Built using:
- [Scikit Learn: ](https://scikit-learn.org/stable/) ML Library used
- [TensorFlow Keras: ](https://www.tensorflow.org/api_docs/python/tf/keras) ML Libraries used
- [HTML: ](https://developer.mozilla.org/en-US/docs/Web/HTML) HTML documentation used
- [Javscript: ](https://developer.mozilla.org/en-US/docs/Web/JavaScript) Javscript framework used
- [Pandas: ](https://pandas.pydata.org/) Python data manipulation libraries
- [Seaborn: ](https://seaborn.pydata.org/) Data visualisation library
## Pipeline:
### 1. Stroke Final.ipynb
This is the main file with all the preprocessing, visualisations, various Machine learning and Deep Learning Models.
- Installing libraries and dependency
- Importing the dataset - [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) 
- Exploratory Data Analysis and Visualisation
- Data Preprocessing - Basic preprocessing and cleaning the dataset
- Dividing the dataset into train and test
- Applying Machine Learning models
- Following Models were Implemented:
1. Decision Tree Classifier
2. Random Forest Classifier
3. XGB Classifier
4. LGBM Classifier
5. Logistic Regression
6. SVC
7. Decision Tree Classifier(With HyperParameter Tuning)
8. Random Forest Classifier(With HyperParameter Tuning)
9. XGB Classifier(With HyperParameter Tuning)
10. LGBM Classifier(With HyperParameter Tuning)
11. Logistic Regression(With HyperParameter Tuning)
12. SVC(With HyperParameter Tuning)

- Saving the weights and .pkl file for deployment
## How to run:
- Run the cells according to above mentioned pipeline
- Model with highest accuracy (Random forest classifier) will be saved in .pkl extension.