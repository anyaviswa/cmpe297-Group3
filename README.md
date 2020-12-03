# cmpe297-Group3
### Term Project
#### Predicting ratings for reviews stored in NoSQL datastore

Since the dataset is huge, all the data is stored in shared google drive. Link is provided [here](https://drive.google.com/drive/folders/1uELqXJcLomwYgtXh7A0KSM0ZTaUnHCCW?usp=sharing ) <br>
<br>

#### Notebooks
1. [yelp-pipeline.ipynb](yelp-pipeline.ipynb) : Entire data pipeline implementation except dataset preparation and model building
2. [Yelp-Dataset-Preparation.py](Yelp-Dataset-Preparation.py) : A part of huge 8GB data was selected and divided uniformly into training and testing dataset to fit it in 512MB of MongoDB.
3. [yelp-lstm-model.ipynb](yelp-lstm-model.ipynb) : Training, validation and evaluation of the LSTM model.
4. [yelp-lr-rf-dt-models.ipynb](yelp-lr-rf-dt-models.ipynb) : Training, validation and evaluation of Logistic regression, Random forest, Decision trees models.
5. [yelp-svc-sgd-mlp-models.ipynb](yelp-svc-sgd-mlp-models.ipynb) : Training, validation and evaluation of Linear Support Vector Classification model , stochastic gradient descent model, Multi-layer Perceptron classifier model
