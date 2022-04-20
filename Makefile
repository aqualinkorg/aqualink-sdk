SHELL := /bin/bash

# Generate using openapi-generator
generate:
	openapi-generator-cli generate -i https://ocean-systems.uc.r.appspot.com/api/docs-json -o ./sdk -c config.json -g python --skip-validate-spec

build:	
	cd sdk && rm -rf dist/* && python3 -m build

push_testpypi:
	cd sdk && python3 -m twine upload --repository testpypi dist/*

push_pypi:
	cd sdk && python3 -m twine upload dist/*

# Perform sdk test
test:
	python3 ./sdk/test_aqualink_sdk.py
