
## Preparation

    python3 -m pip install --user --upgrade build twine

## Distribution

  1. Build: `python3 -m build`
  2. Distribute: 
    * `twine upload --repository-url https://upload.pypi.org/legacy/ dist/*`
      * [Preview](https://pypi.org/project/nouveau/)
    * `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
      * [Preview](https://test.pypi.org/project/nouveau/)
  3. Distribute github backup:
    1. `git tag <version> -m "tag for PyPI"`
    2. `git push --tags remotename branchname`
