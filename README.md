
# Art Nouveau Design Data

Public domain lazy-downloading data samples.

 - [Mucha](https://www.wikiart.org/en/alphonse-mucha/)
 - [Morris](https://www.wikiart.org/store/wm-morris-and-co.html)
 - [Driscoll](https://en.wikipedia.org/wiki/Clara_Driscoll_(glass_designer)) — Tiffany Studios lamp and glass designs (CC BY-SA 4.0)

# Example Use

    import nouveau

    # random image from all datasets
    img = next(nouveau)
    >> <PIL Image>

    # metadata for the last image returned by next()
    nouveau.details
    >> {'year': 1897, 'name': 'Zodiac', 'filename': '1897-Zodiac.jpg'}

## Indexed access — randomly assigned on first read, cached thereafter

    nouveau[0]
    >> <PIL Image>
    nouveau[0]  # same image
    >> <PIL Image>

## Sample a finite batch

    import itertools
    batch = list(itertools.islice(nouveau, 8))

## Infinite stream

    for img in nouveau:
        process(img)

## Collection Access & Sampling

    morris   = nouveau.collections.Morris()
    mucha    = nouveau.collections.Mucha()
    driscoll = nouveau.collections.Driscoll()

    # pandas index of metadata
    morris.index.head()
    >> shows pandas dataframe head with year, name, filename columns

    # random image from a specific collection
    driscoll.sample()
    >> <PIL Image>

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
license: cc-by-sa-4.0
task_categories:
- image-classification
pretty_name: Art Nouveau Design Data
size_categories:
- n<1K
tags:
- morris
- mucha
- driscoll
- tiffany
---

# Licenses

| Collection | License |
|---|---|
| Morris | [Unlicense](https://unlicense.org) |
| Mucha | [Unlicense](https://unlicense.org) |
| Driscoll | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |

The package code is [Unlicense](https://unlicense.org). Image data licenses vary by collection as noted above. The overall dataset is distributed under CC BY-SA 4.0 as the most restrictive license present.
