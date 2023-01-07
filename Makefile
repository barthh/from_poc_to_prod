setup:
	conda env create -f environment.yml

tests:
	python -m unittest preprocessing.tests.test_utils
	python -m unittest train.tests.test_model_train
	python -m unittest predict.tests.test_predict

deploy:
	python app.py

vscode_fix:
	python3 setup.py install clean
