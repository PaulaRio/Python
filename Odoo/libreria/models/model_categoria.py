from odoo import models, fields, api



class libreria_categoria(models.Model): 
   _name = "libreria.categoria" 
   _description = 'libreria.categoria' 
   _sql_constraints = [('name', 'unique(name)', "Ya existe una categoria con ese nombre . El nombre debe ser unico"), ] 
   name = fields.Char(string="Nombre", required=True, help="Introduce el nombre de la  categoria") 
   descripcion = fields.Text(string="Descripción")
   libros = fields.One2many("libreria.libro", "categoria", string="Libros") 