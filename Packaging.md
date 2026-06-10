
## Releasing a new version

1. Bump `version` in `pyproject.toml`
2. Commit and push:
   ```
   git add pyproject.toml
   git commit -m "release vX.Y.Z"
   git push
   ```
3. Create a GitHub Release tagged `vX.Y.Z` — this triggers the publish workflow:
   ```
   gh release create vX.Y.Z --title "vX.Y.Z" --notes "..."
   ```

The workflow builds the wheel, attests SLSA provenance, and publishes to PyPI via OIDC Trusted Publisher (no API tokens required).

## README.md is the single source of truth

`pyproject.toml` embeds `README.md` as the PyPI long description. The package `__doc__`
is also read from it at import time via `importlib.metadata`. Do not duplicate
description content elsewhere.
