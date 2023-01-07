<a id="readme-top"></a>  
[![tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://github.com/barthh/from_poc_to_prod)

# Introduction

This repository is a Production-ready Machine Learning school roject

<!-- TABLE OF CONTENTS -->
<details open>
  <summary>Table of Contents</summary>
  <ul>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
        <a href="#content">Content</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
        <a href="#usage">Usage</a>
    </li>
    <li>
        <a href="#useful-commands">Useful commands</a>
    </li>
  </ul>
</details>

## About The Project

<p align="justify">
This project involves creating and deploying a machine learning model for predicting stackoverflow tags based on input text. The model has three parts: preprocessing, training, and prediction. The preprocessing part includes functions inherited from Keras, while the training and prediction involve building and using a deep learning model. A flask application has been set up to allow users to send input text via HTTP requests and then dockerized to make it portable and able to be deployed on any machine. Tools such as Flask, TensorFlow, and scikit-learn are used in this project. In order to ensure that everything is working properly, the project includes comprehensive tests.
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Content


| Folder | Description |
| ------------- | ----------- |
| [App](./app/) | The application |
| [Preprocessing](./preprocessing/) | Prepare and divide the dataset into different batches |
| [Train](./train/) | Train our deep learning model |
| [Predict](./predict/) |  Make predictions based on the previously trained model |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisites

To use this application, you will need to have [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) installed.

### Installation

To start using the application, follow these steps:

1. Clone the repository:
   ```bash
    https://github.com/barthh/from_poc_to_prod.git
    cd from_poc_to_prod
    ```

2. Create an environment:
   ```bash
    make setup
    conda activate poc_to_prod_env
    ```

3. Run tests and deploy: 
    ```bash
    make tests deploy
    ````
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

There are two ways to use the application:

### Using a browser

To use the application through a browser, open your browser and go to http://127.0.0.1:5000/

### Using a curl request

You can also send input text to the application using a curl request. For example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": ["text1", "text2"], "top_k":2}' http://localhost:5000/predict
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Useful commands

**Launch tests**
```bash
make tests
```

**Fix vscode problem**

If you have any problems about **preprocessing not found**, please do :
```bash
make vscode_pb
```

**Train model**
```python
python train/train/run.py "dataset_path" "config_path" "artefacts_path" --add_timestamp
```
Here is an example :
```python
python train/train/run.py "train/data/training-data/stackoverflow_posts.csv" "train/conf/train-conf.yml" "train/data/artefacts/"
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>
