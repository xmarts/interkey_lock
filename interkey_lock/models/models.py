# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

# class interkey_lock(models.Model):
#     _name = 'interkey_lock.interkey_lock'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class LockPartner(models.Model):
    _inherit = "res.partner"

    @api.constrains('name','vat')
    def _check_constrains(self):
        if self.name:
            name_obj = self.env['res.partner'].search([('name','ilike',self.name)])
            if len(name_obj) > 1:
                raise UserError(_(
                    'Aviso !\nEl nombre de contacto ('+str(self.name)+') ya existe, no se puede repetir.'))
        if self.vat:
            vat_obj = self.env['res.partner'].search([('vat','ilike',self.vat)])
            if len(vat_obj) > 1:
                raise UserError(_(
                    'Aviso !\nEl RFC ('+str(self.vat)+') ya existe, no se puede repetir.'))


class LockSaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def action_confirm(self):
        confirm = super(LockSaleOrder, self).action_confirm()
        passed = True
        lista = []
        for x in self.order_line:
            if x.price_unit <= x.product_id.standard_price:
                passed = False
                lista +=  [x.product_id.name]
        if passed == False:
                raise UserError(_(
                    'Aviso !\nHay productos debajo del costo. (' + ", ".join(str(x) for x in lista) + ')'))
