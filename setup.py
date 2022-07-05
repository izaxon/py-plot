from setuptools import setup, find_packages


setup(name='xplot',
      version='0.0.5',
      description='XPlot client Python package',
      url='https://github.com/izaxon/py-plot',
      author='izaxon',
      author_email='johan@izaxon.com',
      license='MIT',
      packages=find_packages(),
      install_requires=["ipython", "pandas"],
      zip_safe=False)