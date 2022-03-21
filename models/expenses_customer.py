# -*- coding: utf-8 -*-

from odoo import models, fields, api


 class hr.expense.sheet(models.Model):
     _inherit = "hr.expense.sheet"

      customer_name =  fields.Many2one("res.partner", "cliente")






