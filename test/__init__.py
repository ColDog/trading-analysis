import importlib
from os import listdir
from os.path import isfile, join
import os
import traceback
import re


def run():
    dr = os.path.dirname(os.path.abspath(__file__))
    files = [f for f in listdir(dr) if isfile(join(dr, f))]

    passed = 0
    failed = []

    for fil in files:
        if not re.match('_', fil):
            try:
                mod = fil.replace('.py', '')
                importlib.import_module('test.' + mod)
                passed += 1
            except Exception as e:
                failed.append({'msg': e, 'bkt': traceback.format_exc()})

    print('Tests failed:', len(failed))
    print(' ')

    for test in failed:
        print('Failure', test['msg'])
        print(test['bkt'])