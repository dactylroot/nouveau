from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

name = 'nouveau'
version = '1.0.0'

setup(name=name
    , version=version
    , description='public domain art nouveau image data — lazy-downloading datasets of Morris, Mucha, and Driscoll'
    , long_description=long_description
    , long_description_content_type='text/markdown'
    , url='https://github.com/dactylroot/{}'.format(name)
    , download_url='https://github.com/dactylroot/{0}/archive/{1}.tar.gz'.format(name, version)
    , license='Unlicense'
    , packages=find_packages()
    , include_package_data=True
    , classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
      ]
    , keywords=['art', 'data', 'dataset', 'nouveau', 'tiffany', 'mucha', 'morris']
    , install_requires=['pandas', 'numpy', 'pillow', 'scikit-image', 'matplotlib']
    , python_requires='>=3.8'
    , zip_safe=False
     )
