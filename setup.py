from setuptools import setup

setup(name='beancount-pygments-lexer',
      version='0.1.0a1',
      description='A lexer for pygments for beancount-files',
      url='http://github.com/aumayr/beancount-pygments-lexer',
      author='Dominik Aumayr',
      author_email='dominik@aumayr.name',
      license='MIT',
      packages=['beancount_pygments_lexer'],
      install_requires=['pygments'],
      entry_points = {
          'pygments.lexers': ['beancount = beancount_pygments_lexer.lexer:BeancountLexer'],
      },
      zip_safe=False)
