# -*- coding: utf-8 -*-

from odoo import models, fields, api


class informacion(models.Model):
    _name = 'odoo_basico.informacion' # primero el nombre del modulo y luego el nombre de la clase
    _description = 'tipos de datos básicos'

    name = fields.Char(string="Titulo",required= True,size=20)
    descripcion = fields.Text(string="A descripción")
    autorizado = fields.Boolean(string="¿Estas autorizado?",default=True)
    sexo_traducido = fields.Selection([('Hombre','Home'),('Mujer','Muller'),('Otro','Outro')],string="sexo")
    alto_centimetros = fields.Integer(string='Alto en cm')
    longo_centimetros = fields.Integer(string='Longo en cm')
    ancho_centimetros = fields.Integer(string='Ancho en cm')
    volume = fields.Float(compute='_volume',store=True)
    peso = fields.Float(string='Peso',default=2.7,digits=(6,2))
    densidade =fields.Float(compute='_densidade',store=True)


    @api.depends('alto_centimetros','longo_centimetros','ancho_centimetros')
    def _volume(self):
        for rexistro in self:
            rexistro.volume = float(rexistro.ancho_centimetros)* float(rexistro.longo_centimetros)*float(rexistro.alto_centimetros)

    @api.depends('volume','peso')
    def _densidade(self):
        for rexistro in self:
            if rexistro.volume != 0:
                rexistro.densidade = (float(rexistro.peso) / float(rexistro.volume))*100
            else:
                rexistro.densidade = 0

