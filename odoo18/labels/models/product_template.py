from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

        x_studio_print = fields.Boolean(string="Print")
