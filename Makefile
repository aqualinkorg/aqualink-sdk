SHELL := /bin/bash

# Generate using openapi-generator
generate:
	npx openapi-generator-cli generate -i https://production-dot-ocean-systems.uc.r.appspot.com/api/docs-json -o ./sdk -c config.json -g python --skip-validate-spec
	python3 -c "$$POST_GENERATE"

build:
	cd sdk && rm -rf dist/* && python3 -m build

push_testpypi:
	cd sdk && python3 -m twine upload --repository testpypi dist/*

push_pypi:
	cd sdk && python3 -m twine upload dist/*

# Perform sdk test
test:
	python3 ./sdk/test_aqualink_sdk.py

define POST_GENERATE
from pathlib import Path

apis = Path("sdk/aqualink_sdk/apis/__init__.py")
text = apis.read_text()
line = "from aqualink_sdk.api.aggregate_api import AggregateApi\n"
marker = "# Import APIs into API package:\n"
if line not in text and marker in text:
    apis.write_text(text.replace(marker, marker + line, 1))

req = Path("sdk/requirements.txt")
rt = req.read_text()
if "pandas" not in rt:
    req.write_text("pandas == 1.4.2\n" + rt)
endef
export POST_GENERATE
