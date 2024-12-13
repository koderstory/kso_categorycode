from odoo import models, fields

class CustomCategory(models.Model):
    _inherit = 'product.category'

    code = fields.Char("Category Code", help="Code for category")