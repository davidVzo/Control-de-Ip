from odoo import models, fields


class Area(models.Model):
    _name = "areas.control"
    address = fields.Char("Direccion")
    siglas = fields.Char("Siglas")
    vlan = fields.Integer("Vlan")
    responsible = fields.Char("Responsible")
    
