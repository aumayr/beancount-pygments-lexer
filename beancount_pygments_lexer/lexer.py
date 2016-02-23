# -*- coding: utf-8 -*-
"""
    pygments.lexers.beancount
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for beancount-files.

    :copyright: Copyright 2015-2016 by Dominik Aumayr (dominik@aumayr.name)
    :license: MIT
"""

import re

from pygments.lexer import RegexLexer, bygroups, default, words, include
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Literal, Whitespace

class BeancountLexer(RegexLexer):
    """
    For `Beancount <http://furius.ca/beancount/>`_ source code.

    .. versionadded:: 0.1
    """

    name = 'Beancount'
    aliases = ['beancount', 'ledger']
    filenames = ['*.beancount', '*.ledger', '*.bean']
    mimetypes = ['text/x-beancount']

    tokens = {
        'root': [
            (r'\s+', Whitespace),

            # Accounts
            (r'(?<=:)([A-Z][A-Za-z0-9\-]+)(:)?', bygroups(Punctuation, Name.Variable)),
            (r'([A-Z][A-Za-z0-9\-]+)(:)', bygroups(Name.Constant, Punctuation)),

            # Tags
            (r'(#)([A-Za-z0-9\-]+)', bygroups(Punctuation, Name.Variable)),

            # Options/Events
            (r'(option|event)(\s+)("\w*")(\s+)("[\w\s]*")', bygroups(Keyword.Reserved, Whitespace, Name.Variable, Whitespace, String)),   # Option directives

            # Directives
            (r'(\*)?(\s)*(".*")(\s)*(\|)?(\s)*(".*")', bygroups(Keyword.Reserved, Whitespace, Name.Variable, Whitespace, Keyword.Reserved, Whitespace, String)),

            # Metadata
            (r'(\w+)(:)(\s+)', bygroups(Name.Variable, Punctuation, Whitespace)),

            # Strings
            (r'(".*")', String),

            # Dates
            (r'([0-9]{4})(\-)([0-9]{2})(\-)([0-9]{2})', bygroups(Number.Integer, Punctuation, Number.Integer, Punctuation, Number.Integer)),

            # Comments
            (r";.*", Comment.Single),
            (r"#.*", Comment.Single),
            (r"\*.*", Comment.Single),

            # Numbers
            (r'(\-?)([0-9]+\.?[0-9]*(?!\.))', bygroups(Punctuation, Number.Float)),
            (r'([A-Z]+)', Name.Label),
            (r'([{}])', Punctuation),

            # Keywords
            (words((
                'open', 'close', 'pad', 'balance', 'note', 'price', 'event', 'document', 'pushtag', 'poptag'), prefix=r'\b', suffix=r'\b'),
             Keyword.Reserved),
            (words((
                'option', 'commodity'), prefix=r'\b', suffix=r'\b'),
             Keyword.Reserved)
        ]
    }

