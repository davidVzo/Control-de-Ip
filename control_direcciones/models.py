from odoo import models,fields

class Control(models.Model):
    _name = "controles.control"
    name = fields.Char("Nombre")
    status = fields.Selection(selection=[("borrador","Borrador"),("hecho","Hecho")])
    ip = fields.Char("Ip")
    area = fields.Char("Area")
    