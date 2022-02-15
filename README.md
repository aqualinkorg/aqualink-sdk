# aqualink-sdk
A python SDK wrapper for the Aqualink API

Initialized using [swagger-codegen](https://github.com/swagger-api/swagger-codegen).

To populate, run

```
swagger-codegen generate -i https://ocean-systems.uc.r.appspot.com/api/docs-json -l python -o ./sdk -c config.json
```

## Upload to Pypi
During the testing phase, you can upload to test.pypi easily in just a few steps.
- build the sdk: `cd sdk; python3 -m build`
- push to testpypi: `python3 -m twine upload --repository testpypi dist/* `. Use an API token and the `__token__` username.
