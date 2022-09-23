from odoo import models, fields


class Users(models.Model):
    _name = "users.control"
    
    name = fields.Char("Nombre")
    ci = fields.Char("Cedula")
    host_name = fields.Char("Host name")
    user = fields.Char("Usuario")
    ext_phone = fields.Char("Extencion telefonica")
    
