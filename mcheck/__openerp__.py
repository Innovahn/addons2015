# -*- coding: utf-8 -*-
{	
	'name' : 'miscellaneous checks',
	'author': 'Grupo Innova',
	'category': 'Generic Modules/Accounting',
	'summary': 'This module allows you to record miscellaneous payments checks',
	'description': """miscellaneous checks""",

	'data':[	
		'views/journal_view.xml',
		'views/mcheck_view.xml',	
		'views/reporte1.xml' ,
			'views/layouts.xml' ,
			'views/mcheck_reports.xml'
	],
	'update_xml' : [
			'security/groups.xml',
			'security/ir.model.access.csv',
	],
	'depends': ['base','sale','account_voucher'],
    	'installable': True,
}
