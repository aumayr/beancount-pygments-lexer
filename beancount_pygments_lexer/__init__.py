# -*- coding: utf-8 -*-
"""
    Pygments Beancount Lexer – A Beancount lexer for Pygments to
    highlight Beancount code snippets.
    Copyright ©  2015-2016 Dominik Aumayr <dominik@aumayr.name>
    Licensed under the MIT License.
    You may not use this file except in compliance with the License.

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
from __future__ import absolute_import, unicode_literals, print_function

from .lexer import BeancountLexer
from .util.version import get_version

VERSION = (0, 1, 1, '', 0)

__url__             = "http://github.com/aumayr/beancount-pygments-lexer"
__version__         = get_version(VERSION)
__license__         = "MIT"
__author__          = "Dominik Aumayr"
__author_email__    = "dominik@aumayr.name"

__all__ = ['BeancountLexer']
