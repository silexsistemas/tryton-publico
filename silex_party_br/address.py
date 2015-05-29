# -*- coding: utf-8 -*-
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Eval

__metaclass__ = PoolMeta
__all__ = ['Address']

STATES = {
    'readonly': ~Eval('active'),
    }
DEPENDS = ['active']


class Address:
    "Address"
    __name__ = 'party.address'

    number = fields.Char(u'Número', states=STATES, depends=DEPENDS)
    complement = fields.Char(u'Complemento', states=STATES, depends=DEPENDS)
    municipio = fields.Many2One('silex_party_br.municipio', u'Município', depends=['active', 'subdivision'],
                                domain=[('subdivision', '=', Eval('subdivision'))]
                                )

    def on_change_subdivision(self):
        if self.municipio and self.municipio.subdivision != self.subdivision:
            return {'municipio': None}
        return {}