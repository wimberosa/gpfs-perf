#!/usr/bin/python
import sys
import os

import mmtune_toc as toc

def addArguments(parser):
  """Routine any global command line arguments that are
     applicable to all modules.  The toc module itself
     generally only provides global variables and not
     actual implementations of anything
  """
  parser.add_argument('--dummy', dest='dummy',
                      action='store_const', const=True,
                      help='dummy command')


def main(args):
  if args.dummy is not None:
    print("we got dummy")

  return toc.MOD_OK
