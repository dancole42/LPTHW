from nose.tools import *
from ex48 import lexicon, parser

test_sentence = "this is a bear princess test of stop 123."

def test_peek():
  assert_equal(parser.peek(lexicon.scan(test_sentence)), ('error'))

def test_match():
  assert_equal(parser.match(lexicon.scan(test_sentence), 'error'), (('error', 'this')))

def test_skip():
  assert_equal(skip(lexicon.scan(test_sentence)), '')
  

"""
def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess')])
"""