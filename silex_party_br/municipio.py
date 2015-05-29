# -*- coding: utf-8 -*-
from trytond.pool import PoolMeta
from trytond.model import ModelView, ModelSQL, fields

__metaclass__ = PoolMeta
__all__ = ['Municipio']


class Municipio(ModelSQL, ModelView):
    'Municipio'
    __name__ = 'silex_party_br.municipio'

    _rec_name = 'nome'

    nome = fields.Char(u'Nome', size=255, required=True)
    codigo_ibge = fields.Integer(u'Código do IBGE')
    codigo_siafi = fields.Integer(u'Código do SIAFI')
    subdivision = fields.Many2One('country.subdivision', u'Estado', select=True)