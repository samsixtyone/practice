

import os
import sys
import re
import math


def fab(n):
  if n == 0 or n == 1:
    return 1
  return fab(n-1) + fab(n-2)


if "__name__ == main":
  print (fab(21))

