# -*- coding: utf-8 -*-
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Eval

from enumeradores import *

__metaclass__ = PoolMeta
__all__ = ['Party']


class Party():
    __name__ = 'party.party'

    legal_type = fields.Selection(LEGAL_TYPE, 'Tipo', required=True)
    cpf = fields.Char(u'CPF',
                      states={'invisible': Eval('legal_type', 'fisica') != 'fisica'})
    rg = fields.Char(u'RG',
                     states={'invisible': Eval('legal_type', 'fisica') != 'fisica'},
                     help=u'Carteira de Identidade')
    emissor = fields.Char(u'Emissor',
                     states={'invisible': Eval('legal_type', 'fisica') != 'fisica'},
                     help=u'Órgão Emissor')
    data_emissao = fields.Date(u'Data de Emissão',
                               states={'invisible': Eval('legal_type', 'fisica') != 'fisica'},
                                help=u'Data de Emissão')
    cnpj = fields.Char(u'CNPJ',
                       states={'invisible': Eval('legal_type', 'juridica') != 'juridica'},
                       help=u'CNPJ')
    ie = fields.Char(u'IE',
                     states={'invisible': Eval('legal_type', 'juridica') != 'juridica'},
                     help=u'Inscrição Estadual')
    im = fields.Char(u'IM',
                     states={'invisible': Eval('legal_type', 'juridica') != 'juridica'},
                     help=u'Inscrição Municipal')