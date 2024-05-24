from odoo import api, fields, models, _


class MedicalService(models.Model):
    _name = "medical.service"
    _rec_name="ref"


    ref = fields.Char(string="Name", tracking=True)
    description=fields.Char(string="Description")
    patient_id=fields.Many2one('hospital.patient',string="Patient")
    date_med=fields.Date(string="Date")
    service_ids=fields.One2many('medical.service.lines','medical_id',string="")



    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('medical.service.sequence')
        return super(MedicalService, self).create(vals)







class MedicalServiceLines(models.Model):
    _name = "medical.service.lines"

    invoice=fields.Boolean(string="Invoice")
    des=fields.Char(string="Description")
    product_id=fields.Many2one('product.product',string="Product")
    qty=fields.Float(string="Qty")
    from_date=fields.Date(string="From")
    to_date=fields.Date(string="To")

    medical_id=fields.Many2one('medical.service',string="")