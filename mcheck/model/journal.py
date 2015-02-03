# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from datetime import datetime
import locale
import pytz
from openerp.tools.translate import _

class account_journal(osv.osv):
	_inherit = 'account.journal'
	_columns = {
		'checkmiscelaneous':fields.boolean(string="Miscellaneous Checks"),
	
	}
	_defaults = {
	'checkmiscelaneous' : False,
		} 
