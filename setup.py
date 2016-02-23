import os
from setuptools import setup

version = __import__('beancount_pygments_lexer').__version__
author  = __import__('beancount_pygments_lexer').__author__
author_email  = __import__('beancount_pygments_lexer').__author_email__
url     = __import__('beancount_pygments_lexer').__url__
license = __import__('beancount_pygments_lexer').__license__

try:
    from pypandoc import convert
    read_md = lambda fname: convert(fname, 'rst', 'md')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda fname: open(os.path.join(os.path.dirname(__file__), fname), 'r').read()

setup(name='beancount-pygments-lexer',
      version=version,
      description=('A pygments-lexer for beancount-files.'),
      long_description=read_md('README.md'),
      url=url,
      author=author,
      author_email=author_email,
      license='MIT',
      packages=['beancount_pygments_lexer'],
      install_requires=[
            'pygments>=2.0.2',
      ],
      entry_points = {
          'pygments.lexers': ['beancount = beancount_pygments_lexer.lexer:BeancountLexer'],
      },
      zip_safe=False,
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: Office/Business :: Financial :: Accounting',
      ],
)
