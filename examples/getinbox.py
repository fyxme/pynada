#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from pynada import Pynada

nada = Pynada()
my_email = "my_email@getnada.com"
for email in nada.inbox(my_email).get_emails():
    print email.from_name
    print email.from_email
    print email.subject
    print email.timestamp
    print email.get_contents()
