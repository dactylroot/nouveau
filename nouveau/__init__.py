
import os as _os
import random as _random
import sys as _sys
import types as _types
from pathlib import Path as _Path
from PIL import Image as _Image
import matplotlib.pyplot as _plt

from ._dataset import _ArtDataset
from . import collections
from . import transforms

with open(_os.path.abspath(_os.path.dirname(__file__)) + '/__doc__', 'r') as _f:
    __doc__ = _f.read()

_plt.ion()


class _DetailsProxy(dict):
    def __init__(self, cache):
        self._cache = cache
        super().__init__()

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._cache[key][1]
        return super().__getitem__(key)


class _NouveauModule(_types.ModuleType):
    def __init__(self, module):
        super().__init__(module.__name__)
        self.__dict__.update(module.__dict__)
        self._pool = None
        self._cache = {}
        self.details = _DetailsProxy(self._cache)

    def _get_pool(self):
        if self._pool is None:
            entries = []
            for cls in _ArtDataset.__subclasses__():
                dataset = cls()
                for _, row in dataset.index.iterrows():
                    path = dataset.storage_path / dataset._storage_jpg / row['filename']
                    entries.append((path, row.to_dict(), dataset._ensure_downloaded))
            self._pool = entries
        return self._pool

    def __iter__(self):
        return self

    def __getitem__(self, idx):
        if idx not in self._cache:
            path, details, ensure = _random.choice(self._get_pool())
            ensure(path.name)
            img = _Image.open(path)
            img.load()
            self._cache[idx] = (img, details)
        self.details.clear()
        self.details.update(self._cache[idx][1])
        return self._cache[idx][0]

    def sample(self):
        return next(self)

    def __next__(self):
        path, details, ensure = _random.choice(self._get_pool())
        ensure(path.name)
        img = _Image.open(path)
        img.load()
        self.details.clear()
        self.details.update(details)
        return img


_sys.modules[__name__] = _NouveauModule(_sys.modules[__name__])
