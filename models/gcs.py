from odoo import api, fields, models, _


class GCS(models.Model):
    _name = "patient.gcs"

    registration_cod = fields.Many2one('patient.apache', string="Registration Code")
    gcs_date = fields.Datetime(string="Date")
    eyes=fields.Char(string="Eyes")
    verbal=fields.Char(string="Verbal")
    motor=fields.Char(string="Motor")
    glasgow=fields.Integer(string="Glasgow")

