# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sucesion(models.Model):
    _name = 'odoo_basico.sucesion'  # primero el nombre del modulo y luego el nombre de la clase
    _description = 'tipos de datos básicos'

    name = fields.Char(string="suceso", required=True, size=20)
    descripcion = fields.Text(string="A descripción")
    nivel = fields.Selection([('Alto', 'Alto'), ('Medio', 'Medio'), ('Bajo', 'Bajo')])
    data_hora = fields.Text(string="Fecha y hora")
