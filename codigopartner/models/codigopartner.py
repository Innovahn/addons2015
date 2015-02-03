# -*- encoding: utf-8 -*-
from openerp.osv import osv, fields

class Codigopartner(osv.Model):
    _inherit = 'res.partner'
    _columns = {
            'partnercode' : fields.integer("Partner Code",required="True"),
            }
