# -*- coding: utf-8 -*-
"""
    pygments.lexers.beancount
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for beancount-files.

    :copyright: Copyright 2015 by Dominik Aumayr (dominik@aumayr.name)
    :license: MIT
"""

import re

from pygments.lexer import RegexLexer, bygroups, default, words, include
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Literal

class BeancountLexer(RegexLexer):
    """
    For `Beancount <http://furius.ca/beancount/>`_ source code.

    .. versionadded:: 0.1
    """

    name = 'Beancount'
    aliases = ['beancount', 'ledger']
    filenames = ['*.beancount', '*.ledger']
    mimetypes = ['text/x-beancount']

    tokens = {
        'root': [
            # Text
            # (r'[ \t]+', Text),
            # (r'\.\.\n', Text),  # Line continuation
            # Comments
            (r";.*", Comment.Single),
            (r"\*.*", Comment.Single),
            (r"#!.*", Comment.Hashbang),
            (r'([A-Z][A-Za-z0-9\-]+)(:)', bygroups(Name.Constant, Punctuation)),   # Root Accounts
            (r'([:]?)([A-Z][A-Za-z0-9\-]+)', bygroups(Name.Namesepace, Punctuation)),   # Accounts
            (r'([a-z][A-Za-z0-9\-\_]+)(:)', bygroups(Name.Variable.Class, Name.Variable)),   # Metadata
            (r"\".*\"", String),
            # (r'^(option)\s*(\".*\")\s*(\".*\")\s*', bygroups(Keyword.Reserved, Name.Variable, String)),   # Option directives
            (r"\s([A-Z][A-Z0-9\'\.\_\-]{0,10}[A-Z0-9])[\,?|\s]", Literal),    # Currencies
            (r'([0-9]{4})(\-)([0-9]{2})(\-)([0-9]{2})', bygroups(Number.Integer, Punctuation, Number.Integer, Punctuation, Number.Integer)),   # Dates
            (r'([\-|\+]?)([\d]+[\.]?[\d]*)', bygroups(Number, Name.Other)),   # Numbers

            # Numbers
            # (r'[0-9]+\.[0-9]*(?!\.)', Number.Float),
            # # Other
            # (r'[(),.:\[\]]', Punctuation),
            # (r'(?:#[\w \t]*)', Name.Label),
            # (r'(?:\?[\w \t]*)', Comment.Preproc),
            # Identifiers
            # (r'(option)\s*(\".*\")\s*(\".*\")\s*', Keyword.Reserved),
            # Keywords
            (words((
                'open', 'close', 'pad', 'balance', 'note', 'price', 'event', 'document'), prefix=r'\b', suffix=r'\b'),
             Keyword.Type),
            (words((
                'option', 'commodity'), prefix=r'\b', suffix=r'\b'),
             Keyword.Reserved)
        ]
    }

