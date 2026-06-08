
from ._dataset import _ArtDataset


class Morris(_ArtDataset):
    _storage_csv = 'morris.csv'
    _storage_jpg = 'morris'
    _download_base_url = 'https://huggingface.co/datasets/dactylroot/morris/resolve/main/morris'


class Mucha(_ArtDataset):
    _storage_csv = 'mucha.csv'
    _storage_jpg = 'mucha'
    _download_base_url = 'https://huggingface.co/datasets/dactylroot/mucha/resolve/main/mucha'


class Driscoll(_ArtDataset):
    _storage_csv = 'driscoll.csv'
    _storage_jpg = 'driscoll'
    _download_base_url = 'https://huggingface.co/datasets/dactylroot/driscoll/resolve/main/driscoll'
