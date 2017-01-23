# -*- coding: UTF-8 -*-
# generated by lino.sphinxcontrib.help_text_builder
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
help_texts = {
    'lino_avanti.lib.avanti.Plugin' : _("""See lino.core.plugin.Plugin."""),
    'lino_avanti.lib.avanti.choicelists.Translators' : _("""Types of registries for the Belgian residence."""),
    'lino_avanti.lib.avanti.choicelists.ClientEvents' : _("""A choicelist of observable client events."""),
    'lino_avanti.lib.avanti.choicelists.ClientCreated' : _("""The choice for ClientEvents which
selects clients whose record has been created during the observed
period."""),
    'lino_avanti.lib.avanti.choicelists.ClientModified' : _("""The choice for ClientEvents which selects clients whose
main record has been modified during the observed period."""),
    'lino_avanti.lib.avanti.migrate.Migrator' : _("""The standard migrator for Lino Avanti."""),
    'lino_avanti.lib.avanti.models.Client' : _("""A client is a person using our services."""),
    'lino_avanti.lib.avanti.models.Client.overview' : _("""A panel with general information about this client."""),
    'lino_avanti.lib.avanti.models.Client.client_state' : _("""Pointer to ClientStates."""),
    'lino_avanti.lib.avanti.models.Client.unemployed_since' : _("""The date when this client got unemployed and stopped to have a
regular work."""),
    'lino_avanti.lib.avanti.models.Client.seeking_since' : _("""The date when this client registered as unemployed and started
to look for a new job."""),
    'lino_avanti.lib.avanti.models.Clients' : _("""Base class for most lists of clients."""),
    'lino_avanti.lib.avanti.models.Clients.client_state' : _("""If not empty, show only Clients whose client_state equals
the specified value."""),
    'lino_avanti.lib.avanti.models.Clients.model' : _("""alias of Client"""),
}
