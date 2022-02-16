SHELL := /bin/bash
# Perform sdk test
build:	
	cd sdk && rm -rf dist/* && python3 -m build

push_testpypi:
	cd sdk && python3 -m twine upload --repository testpypi dist/*

test:
	python3 ./sdk/test_aqualink_sdk.py
