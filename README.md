
# Art Nouveau Design Data

Public domain lazy-downloading data samples.

## Mucha

https://www.wikiart.org/en/alphonse-mucha/

## Morris

This is a collection of designs by the famous Morris company artists of the 1800s.

# Format

 - image: image in numpy array or PyTorch tensor format
 - name: a common name for the design
 - year: initial year of design

# Example Use

    import nouveau

    morris = nouveau.Morris()
    mucha  = nouveau.Mucha()

    # pandas index of metadata
    morris.index.head()
    >> shows pandas dataframe head with year, name, filename columns

    # iterate as PIL Images (aligned with index by position)
    for i, img in enumerate(morris):
        print(morris.index.iloc[i]['name'], img.size)

    # access a single item by position (returns dict with numpy image)
    morris[0]
    >> {'year': 1862,
    >>  'name': 'Fruit-Blue',
    >>  'filename': '1862-Fruit-Blue.jpg',
    >>  'image': array([[[254, 253, 249], ...

    # display by index or name
    morris.show(1)
    >> <pyplot image>

    morris.show('Fruit-Blue')
    >> <pyplot image>

    # get a PIL Image by index or name
    morris.toPIL(0)
    >> <PIL Image>

    # PyTorch dataset (returns [tensor, name, year] per item)
    tensors = morris.to_torch()
    tensors[0][0].shape
    >> torch.Size([3, 1987, 1586])


---
license: unlicense
task_categories:
- image-classification
pretty_name: Morris Co. Public Domain Art
size_categories:
- n<1K
---
