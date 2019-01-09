import os
import csv
import sys
import shutil
from os import environ
from os.path import join
import sklearn.cross_validation 

import numpy as np
from sklearn.cross_validation import StratifiedKFold

class Bunch(dict):
    """Container object for datasets
    Dictionary-like object that exposes its keys as attributes.
    >>> b = Bunch(a=1, b=2)
    >>> b['b']
    2
    >>> b.b
    2
    >>> b.a = 3
    >>> b['a']
    3
    >>> b.c = 6
    >>> b['c']
    6
    """

    def __init__(self, **kwargs):
        dict.__init__(self, kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setstate__(self, state):
        # Bunch pickles generated with scikit-learn 0.16.* have an non
        # empty __dict__. This causes a surprising behaviour when
        # loading these pickles scikit-learn 0.17: reading bunch.key
        # uses __dict__ but assigning to bunch.key use __setattr__ and
        # only changes bunch['key']. More details can be found at:
        # https://github.com/scikit-learn/scikit-learn/issues/6196.
        # Overriding __setstate__ to be a noop has the effect of
        # ignoring the pickled __dict__
        pass

def load_iscx():
    """Load and return the ISCX dataset (classification).
    The ISCX dataset is a classic and very easy multi-class classification
    dataset.
    =================   ==============
    Classes                          2
    Samples per class               
    Samples total                  150
    Dimensionality                   9
    Features            real, positive
    =================   ==============
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:
        'data', the data to learn, 'target', the classification labels,
        'target_names', the meaning of the labels, 'feature_names', the
        meaning of the features, and 'DESCR', the
        full description of the dataset.
    """
    #These are the 4 CSV Files

    #'csvBruteForceRandom.csv', 'csvDosRandom.csv', csvDDosRandom.csv, csvInfiltrateRandom.csv

    randomcsv = '../data/csvInfiltrateTrain.csv'

    with open(randomcsv) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        n_samples = int(temp[0])
        n_features = int(temp[1]) - 2
        target_names = np.array(temp[2:])
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,), dtype=np.int)

  #      print n_samples, n_features, target_names, data, target

        for i, ir in enumerate(data_file):
            data[i] = np.asarray(ir[1:-1], dtype=np.int)
            target[i] = np.asarray(ir[-1], dtype=np.int)

   #     print data, target

    print "For " + randomcsv
        
    skf = StratifiedKFold(target, n_folds = 2)

    

    return Bunch(data=data, target=target,
                 target_names=target_names,
                 feature_names=['appName','totalDestinationPackets','totalSourcePackets','direction',
                 'sourceIP','protocolName','destinationIP','duration','target']), skf 


#    printskf.
