
import types
import unittest

import nouveau
from nouveau._dataset import _ArtDataset


class TestPublicAPI(unittest.TestCase):

    def test_details_attribute_exists(self):
        self.assertTrue(hasattr(nouveau, 'details'))

    def test_sample_callable(self):
        self.assertTrue(callable(getattr(nouveau, 'sample', None)))

    def test_transforms_is_module(self):
        self.assertIsInstance(nouveau.transforms, types.ModuleType)

    def test_collections_is_module(self):
        self.assertIsInstance(nouveau.collections, types.ModuleType)

    def test_morris_in_collections(self):
        self.assertTrue(hasattr(nouveau.collections, 'Morris'))
        self.assertTrue(issubclass(nouveau.collections.Morris, _ArtDataset))

    def test_mucha_in_collections(self):
        self.assertTrue(hasattr(nouveau.collections, 'Mucha'))
        self.assertTrue(issubclass(nouveau.collections.Mucha, _ArtDataset))

    def test_driscoll_in_collections(self):
        self.assertTrue(hasattr(nouveau.collections, 'Driscoll'))
        self.assertTrue(issubclass(nouveau.collections.Driscoll, _ArtDataset))

    def test_collections_are_direct_subclasses(self):
        for cls in (nouveau.collections.Morris, nouveau.collections.Mucha, nouveau.collections.Driscoll):
            with self.subTest(cls=cls.__name__):
                self.assertEqual(cls.__bases__, (_ArtDataset,))

    def test_nouveau_is_iterator(self):
        self.assertIs(iter(nouveau), nouveau)
        self.assertTrue(callable(getattr(nouveau, '__next__', None)))

    def test_nouveau_supports_index_access(self):
        self.assertTrue(callable(getattr(nouveau, '__getitem__', None)))

    def test_no_public_dataset_classes_on_root(self):
        public = {k for k in vars(nouveau) if not k.startswith('_')}
        self.assertEqual(public & {'Morris', 'Mucha', 'Driscoll'}, set(),
                         "dataset classes should live under nouveau.collections, not the root module")


if __name__ == '__main__':
    unittest.main()
