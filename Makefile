pipinit:
	pip install -r requirements.txt


condainit:
	conda install --yes --file requirements.txt

	
freeze:
	conda list -e > conda-requirements.txt
	pip freeze > requirements.txt

	
test:
	python -m pytest test/


.PHONY: test 
