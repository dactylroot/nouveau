
import pandas as _pd
import os as _os
import urllib.request as _request
from skimage import io as _io
import matplotlib.pyplot as _plt
from pathlib import Path as _Path
from PIL import Image as _Image
from . import transforms

with open(_os.path.abspath(_os.path.dirname(__file__))+'/__doc__','r') as _f:
    __doc__ = _f.read()

_plt.ion()   # interactive mode


class _ArtDataset():
    _storage_csv = None
    _storage_jpg = None
    _download_base_url = None

    def __init__(self, root=_Path(__file__).parent, transform=False):
        self.storage_path = _Path(root)
        self.transform = transform
        self.index = _pd.read_csv(self.storage_path / self._storage_csv)
        self._self_validate()

    def to_torch(self):
        import torch
        from torchvision import transforms
        import numpy as _np
        ArtClass = type(self)
        while issubclass(ArtClass, torch.utils.data.Dataset):
            ArtClass = ArtClass.__bases__[1]

        class _TorchDataset(torch.utils.data.Dataset, ArtClass):

            def __init__(self, root=_Path(__file__).parent, transform=False):
                torch.utils.data.Dataset.__init__(self)
                ArtClass.__init__(self, root, transform)

            def show(self, idx):
                name = None
                if isinstance(idx, str):
                    if idx in self.index.name.values:
                        idx = self.index.index[self.index.name==idx][0]
                        idx = int(idx)
                        name = self.index.name[idx]
                        print(f"found item {idx} by name {name}")
                    else:
                        raise ValueError('item name not found')
                if isinstance(idx, int):
                    name = self.index.name[idx]
                    _plt.title(name)
                    im = transforms.ToPILImage()(self.__getitem__(idx)[0])
                    _plt.imshow(im)
                    _plt.show()
                else:
                    im = transforms.ToPILImage()(idx)
                    _plt.imshow(im)
                    _plt.show()
                return im

            def __getitem__(self, idx):
                item = self.index.iloc[idx].to_dict()
                image = _io.imread(self.storage_path / self._storage_jpg / self.index.iloc[idx].filename)
                if image.ndim == 2:
                    image = _np.stack([image] * 3, axis=-1)
                image = torch.tensor(image).permute(2, 0, 1)
                if self.transform:
                    image = self.transform(image)
                item = [image, item['name'], item['year']]
                return item

        return _TorchDataset(str(self.storage_path), self.transform)

    def __iter__(self):
        for filename in self.index['filename']:
            img = _Image.open(self.storage_path / self._storage_jpg / filename)
            img.load()
            yield img

    def __len__(self):
        return len(self.index)

    def __getitem__(self, idx):
        item = self.index.iloc[idx].to_dict()
        image = _io.imread(self.storage_path / self._storage_jpg / self.index.iloc[idx].filename)
        if self.transform:
            image = self.transform(image)
        item['image'] = image
        return item

    def toPIL(self, idx):
        if isinstance(idx, str):
            if idx in self.index.name.values:
                idx = self.index.index[self.index.name==idx][0]
                idx = int(idx)
                name = self.index.name[idx]
                print(f"found item {idx} by name {name}")
            else:
                raise ValueError('item name not found')
        if isinstance(idx, int):
            _item = self.__getitem__(idx)
            image = _item['image']
            im = _Image.fromarray(image)
        else:
            try:
                im = _Image.fromarray(idx)
                _plt.imshow(im)
                _plt.show()
            except (AttributeError, TypeError):
                im = self.to_torch().show(idx)
        return im

    def show(self, idx):
        if isinstance(idx, str):
            if idx in self.index.name.values:
                idx = self.index.index[self.index.name==idx][0]
                idx = int(idx)
                name = self.index.name[idx]
                print(f"found item {idx} by name {name}")
            else:
                raise ValueError('item name not found')
        if isinstance(idx, int):
            _item = self.__getitem__(idx)
            image = _item['image']
            name  = _item['name']
            _plt.title(name)
            im = _Image.fromarray(image)
            _plt.imshow(im)
            _plt.show()
        else:
            try:
                im = _Image.fromarray(idx)
                _plt.imshow(im)
                _plt.show()
            except (AttributeError, TypeError):
                im = self.to_torch().show(idx)
        return im

    def _self_validate(self):
        """Ensure all images in the index exist locally, downloading any that are missing."""
        allgood = True
        for filename in self.index.filename.values:
            _file = _Path(self.storage_path / self._storage_jpg / filename)
            if _file.is_file():
                continue
            allgood = False
            _os.makedirs(_file.parent, exist_ok=True)
            if self._download_base_url is None:
                raise AttributeError(
                    f"{type(self).__name__} has no _download_base_url; cannot download {filename}")
            try:
                print(f"downloading {filename}")
                url = f"{self._download_base_url}/{filename}"
                _request.urlretrieve(url, _file)
            except Exception as e:
                _file.unlink(missing_ok=True)
                print(f"couldn't load {filename}: {e}")
        if allgood:
            print(f"{len(self)} images present.")


class Morris(_ArtDataset):
    _storage_csv = 'morris.csv'
    _storage_jpg = 'morris'
    _download_base_url = 'https://huggingface.co/datasets/dactylroot/morris/resolve/main/morris'


class Mucha(_ArtDataset):
    _storage_csv = 'mucha.csv'
    _storage_jpg = 'mucha'
    _download_base_url = 'https://huggingface.co/datasets/dactylroot/mucha/resolve/main/mucha'


