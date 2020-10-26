import numpy as np
from scipy.stats import entropy
from math import log, e
import pandas as pd

import timeit


import math
from collections import Counter

def entropy(labels):
    """ Computes entropy of 0-1 vector. """
    n_labels = len(labels)

    if n_labels <= 1:
        return 0

    counts = np.bincount(labels)
    probs = counts[np.nonzero(counts)] / n_labels
    n_classes = len(probs)

    if n_classes <= 1:
        return 0
    return - np.sum(probs * np.log(probs)) / np.log(n_classes)


def entropy2(labels, base=None):
  """ Computes entropy of label distribution. """

  n_labels = len(labels)

  if n_labels <= 1:
    return 0

  value, counts = np.unique(labels, return_counts=True)
  probs = counts / n_labels
  n_classes = np.count_nonzero(probs)

  if n_classes <= 1:
    return 0

  ent = 0.

  # Compute entropy
  base = e if base is None else base
  for i in probs:
    ent -= i * log(i, base)

  return ent


def eta(data, unit='natural'):
       base = {
           'shannon': 2.,
           'natural': math.exp(1),
           'hartley': 10.
       }

       if len(data) <= 1:
           return 0

       counts = Counter()

       for d in data:
           counts[d] += 1

       probs = [float(c) / len(data) for c in counts.values()]
       probs = [p for p in probs if p > 0.]

       ent = 0

       for p in probs:
           if p > 0.:
               ent -= p * math.log(p, base[unit])

       return ent
