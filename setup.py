from setuptools import setup, find_packages

setup(
      name='rtfd-clitest',
      version='0.1',
      description='CLI to download docs from ReadTheDocs.org',
      author='HVN',
      author_email='hvn@familug.org',
      packages=find_packages(),
      entry_points={
            'console_scripts': [
                  'rtfd-cli = rtfd.rtfd:command_line',
            ]
      },
      url='https://github.com/MUSoC/rtfd-cli',
      keywords=['readthedocs', 'terminal', 'command-line', 'rtfd', 'python'],
      license='MIT',
      classifiers=[],
      install_requires=[
            'requests',
            'BeautifulSoup4',
            'tqdm',
            'colorama'
      ]
)
