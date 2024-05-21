from odoo import fields,models,api,_


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.depends('name', 'default_code')
    def _compute_display_name(self):
        for template in self:
            if template.default_code:
                template.display_name = template.default_code
            else:
                template.display_name = template.name

class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.depends('name', 'default_code')
    def _compute_display_name(self):
        for template in self:
            template.display_name = template.name


