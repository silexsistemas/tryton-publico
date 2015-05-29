#!/usr/bin/env python

import sys, os
DIR = os.path.abspath(os.path.normpath(os.path.join(__file__,
    '..', '..', '..', '..', '..', 'trytond')))
if os.path.isdir(DIR):
    sys.path.insert(0, os.path.dirname(DIR))

import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import POOL, DB_NAME, USER, CONTEXT, test_view,\
    test_depends
from trytond.transaction import Transaction


class PartyBrTestCase(unittest.TestCase):
    '''
    Test Party BR module.
    '''

    def setUp(self):
        trytond.tests.test_tryton.install_module('silex_party_br')
        self.party = POOL.get('party.party')

    def test0005views(self):
        '''
        Test views.
        '''
        test_view('silex_party_br')

    def test0006depends(self):
        '''
        Test depends.
        '''
        test_depends()

    def test0030party(self):
        'Create party with legal types'
        with Transaction().start(DB_NAME, USER,
                context=CONTEXT) as transaction:
            party1, = self.party.create([{
                        'name': 'Party 1',
                        'legal_type': 'fisica'
                        }])
            party2, = self.party.create([{
                        'name': 'Party 1',
                        'legal_type': 'juridica'
                        }])
            self.assertTrue(party1.id)
            self.assertEqual(party1.legal_type, 'fisica')

            self.assertTrue(party2.id)
            self.assertEqual(party2.legal_type, 'juridica')

            transaction.cursor.commit()

    def test0040party(self):
        from trytond.error import UserError
        with Transaction().start(DB_NAME, USER,
                context=CONTEXT) as transaction:
            self.assertRaises(UserError, self.party.create, [{'name': 'Party 1'}])
            transaction.cursor.commit()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PartyBrTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

