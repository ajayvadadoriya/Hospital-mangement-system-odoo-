from odoo import api, fields, models,_



class HospitalImaging(models.Model):
    _name = "hospital.imaging"
    _description ="Hospital imagingtest type Detail"

    name = fields.Many2one('hospital.imagingtest',string="Name", tracking=True)
    ref = fields.Char(string="Test Request",  required=True, copy=False, readonly=True,  default=lambda self: _('New'))
    date=fields.Datetime(string="Test Date")
    rdate=fields.Datetime(string="Request date",related="name.date",readonly=True)
    test=fields.Char(string="Test",related="name.name",readonly=True)
    patient=fields.Many2one(string="patient",related="name.patient",readonly=True,)
    physician=fields.Many2one(string="Physician",related="name.physician",readonly=True)
    comment=fields.Text(string="Comments")
    state = fields.Selection([
        ('draft', "Draft"), ('confirm', "Confirm"), ('done', "Done"), ('canceled', "Canceled")], string="Status",
        default='draft', tracking=True)
    img_ids=fields.One2many('hospital.image','im_id',string="Images")
    note=fields.Text(string="Other information")





    @api.model_create_multi
    def create(self, vls_list):
        for vls in vls_list:
            vls['ref'] = self.env['ir.sequence'].next_by_code('hospital.imaging.sequence')
        return super(HospitalImaging, self).create(vls_list)





