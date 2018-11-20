#!/usr/bin/env python
"""
lexer_test.py: Tests for lexer.py
"""

import unittest

from core.meta import syntax_asdl, Id
from frontend.lex import LEXER_DEF


class TokenTest(unittest.TestCase):

  def testToken(self):
    t = syntax_asdl.token(Id.Lit_Chars, 'abc')
    print(t)

    # This redundancy is OK I guess.
    t = syntax_asdl.token(Id.Lit_LBrace, '{')
    print(t)

    t = syntax_asdl.token(Id.Op_Semi, ';')
    print(t)

  def testPrintStats(self):
    states = sorted(
        LEXER_DEF.items(), key=lambda pair: len(pair[1]), reverse=True)
    total = 0
    for state, re_list in states:
      n = len(re_list)
      print(n, state)
      total += n

    print("Number of lex states: %d" % len(LEXER_DEF))
    print("Number of token dispatches: %d" % total)

  def testLineId(self):
    # TODO: Test that the lexer gives line_ids when passed an arena.
    # This might be more relevant if we start deallocating memroy.
    pass


if __name__ == '__main__':
  unittest.main()