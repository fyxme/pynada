#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from pynada import Pynada

nada = Pynada()
print nada.get_domains() # returns a list of all available domains
