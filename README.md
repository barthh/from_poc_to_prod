# From POC to Production

## Introduction

This repository contains the work I did to build and deploy a machine learning model for predicting stackoverflow tags based on input text. The model has three parts: preprocessing, training, and prediction. 

The preprocessing portion includes functions inherited from Keras, and the training and prediction sections involve building and utilizing a deep learning model. After building the model, a flask application has been implemented to allow users to send input text via HTTP requests and then dockerized the application to make it portable and able to be deployed on any machine.

## Getting started

Clone the repo:
```bash
https://github.com/barthh/from_poc_to_prod.git
cd from_poc_to_prod
```

Create the environment
```bash
make setup
conda activate poc_to_prod_env
```

Make tests and deploy the app
```bash
make tests deploy
```

## How to use the app
**Using a browser**

Open your browser and go to http://127.0.0.1:5000/


## Useful command

**Launch test**
```bash
make tests
```

**Fix vscode problem**

If you have any problems about **preprocessing not found**, please do :
```bash
make vscode_pb
```

**Train model**
```
python train/train/run.py "train/data/training-data/stackoverflow_posts.csv" train/conf/train-conf.yml "train/data/artefacts/"
```
