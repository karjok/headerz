import setuptools
with open('README.md','r') as description:
	long_description = description.read()

setuptools.setup(
  name = 'headerz',
  packages = ['headerz'],
  version = '0.5',
  license='MIT',
  description = 'A simple package for parsing a header string from sniffer app on android or PC',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Karjok Pangesty',
  author_email = 'karjok.pangesty@gmail.com',
  url = 'https://github.com/karjok/headerz',
  download_url = 'https://github.com/karjok/headerz/archive/v_05.tar.gz',
  keywords = ['header parser', 'header string', 'parsing header string'],
 
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3'
  ],
)
