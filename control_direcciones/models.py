from odoo import models,fields

class Control(models.Model):    
    _name = "controles.control"

    floor = fields.Integer("Piso")
    name = fields.Char("Nombre")
    vlan = fields.Integer("Vlan")
    current_ip = fields.Char("Ip_actual")
    address = fields.Char("Direccion")
    coordination = fields.Char("Coordinacion")
    ci = fields.Char("Cedula_identidad")
    host_name = fields.Char("Host_name")
    user = fields.Char("Usuario")
    ext_phone = fields.Integer("Extencion_telefonica")
    comments = fields.Char("Observaciones")
    

    
  
    