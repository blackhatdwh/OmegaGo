#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 weihao <blackhatdwh@gmail.com>
#
# Distributed under terms of the MIT license.

import os
import subprocess

models_list_file = open('../saved_models/checkpoint')
models_list_file.readline()
models = []
while True:
    line = models_list_file.readline()
    if not line:
        break
    models.append(line.split('"')[1])

newest_model = sorted(models, key=lambda x: int(x.split('-')[1]))[-1]

pwd = os.getcwd()
parent = os.path.dirname(pwd)

param1 = 'python3 %s/main.py gtp policy --read-file=%s/saved_models/' % (parent, parent) + models[0]
param2 = 'python3 %s/main.py gtp policy --read-file=%s/saved_models/' % (parent, parent) + models[1]
os.system('./bin/gogui-twogtp -black "%s" -white "%s" -size 9 -komi 7.5 -verbose -auto -sgffile log' % (param1, param2))

subprocess.getoutput('ls kifu')
