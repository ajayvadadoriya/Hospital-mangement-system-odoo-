from odoo import api, fields, models, _

class HospitalImage(models.Model):
        _name = "hospital.image"
        _description =  'Image'

        image = fields.Image(string='Image')
        im_id = fields.Many2one('hospital.imaging',string="")