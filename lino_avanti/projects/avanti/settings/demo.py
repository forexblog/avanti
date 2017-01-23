# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)
"""Defines and instantiates a demo version of a Lino Avanti Site."""

import datetime

from ..settings import *


class Site(Site):

    the_demo_date = datetime.date(2015, 5, 23)

    languages = "en de fr"

    # default_ui = 'lino_extjs6.extjs6'

SITE = Site(globals())

DEBUG = True

# the following line should not be active in a checked-in version
#~ DATABASES['default']['NAME'] = ':memory:'

