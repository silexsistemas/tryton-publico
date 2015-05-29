# -*- coding: utf-8 -*-
from trytond.pool import Pool
from .party import *
from .municipio import *
from .address import *

def register():
    Pool.register(
        Party,
        Municipio,
        Address,
        module='silex_party_br', type_='model'
    )
