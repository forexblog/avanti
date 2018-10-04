# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)
"""Demo data for Lino Avanti.

"""


from django.conf import settings
from lino.api import rt
from lino.utils import Cycler

def objects():
    
    UserTypes = rt.models.users.UserTypes
    Client = rt.models.avanti.Client
    COACHES = Cycler(rt.models.users.User.objects.filter(
        user_type__in=[UserTypes.user, UserTypes.admin]))

    for client in Client.objects.all():
        client.user = COACHES.pop()
        yield client
    
    obj = rt.models.courses.Enrolment.objects.get(pk=2)
    yield rt.models.courses.Reminder(
        enrolment=obj, user=obj.pupil.user,
        date_issued=settings.SITE.demo_date(-10))

    rt.models.courses.update_missing_rates()
