from odoo import models, fields, api

class libreria_libro(models.Model):     
   _name = "libreria.libro" 
   name = fields.Char(string="Titulo", required=True)     
   precio = fields.Float(string="Precio")     
   ejemplares = fields.Integer(string="Ejemplares")     
   fecha = fields.Date(string="Fecha de compra")     
   segmano = fields.Boolean(string="Segunda mano") 
   estado = fields.Selection([('0', 'Bueno'), ('1', 'Regular'), ('2', 'Malo')], string="Estado", default="0")
   categoria = fields.Many2one("libreria.categoria", string="Categoria", required=True, ondelete="cascade")
   importeTotal=fields.Float(string="Importe Total",compute="_importetotal",store=True) 

   @api.depends('precio','ejemplares')
   def _importetotal(self): 
    for r in self: #iteramos sobre el registro que nos llega  	 	
        r.importeTotal=r.ejemplares*r.precio 
