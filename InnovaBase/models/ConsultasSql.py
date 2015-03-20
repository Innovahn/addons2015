# -*- coding: utf-8 -*-

from openerp.osv import osv
#from datetime import *
#INSERT INTO account_config_settings(date_stop,period,date_start,company_id,group_multi_currency) values (now(),'month','2015-01-01',1,True)
class Currency_Historial(osv.osv):
	_name = "currency.historial"

	def init(self,cr):
		print 'antes del sql .....................................................................'
        	cr.execute(""" 
UPDATE res_currency SET active=False        WHERE (name<>'USD') and (name<>'HNL'); 
UPDATE res_currency SET position = 'before' WHERE  name ='USD'  or   name ='HNL' ;
			""")
		print 'despues del sql....................................................................'

