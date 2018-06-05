
from setuptools import setup

def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
                return readme_file.read()

setup(name='trimet_freq_vs_ridership',
      version='0.1',
      description='ETL & Longitudinal MultiLevel Regression Analysis between Trimet Ridership & Service Frequency',
      long_description=readme(),
      classifiers=[
          'Programming Language :: Pythong :: 3'
      ],
      url='https://github.com/hackoregon/transportation-systems-data-science',
      author='Lee Coates',
      author_email='lee@hackoregon.com',
      license='MIT',
      packages=['trimet_freq_vs_ridership'],
      install_requires=[
          'pypandoc>=1.4'
      ],
      zip_safe=False
)
