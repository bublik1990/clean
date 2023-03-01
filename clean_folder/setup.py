from setuptools import setup, find_namespace_packages

setup(name='clean',
      version='1',
      description='Sort your folders with different types files and folders.',
      url='https://github.com/bublik1990/clean',
      author='Yuliia Bulana',
      author_email='bulanaja.julia@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:clean']}
      )