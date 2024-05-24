from odoo import api, fields, models, _


class CreateImagingRequestWizard(models.TransientModel):
    _name = "create.imaging.request.wizard"
    _description = "Create Imaging Request"

    date = fields.Datetime(string="Test Date")
    patient = fields.Many2one('hospital.patient', string="Patient")
    physician = fields.Many2one('hospital.doctor', string="Physician")
    urgent = fields.Boolean(string="Urgent")
    test_name = fields.Char(string="Name")
    test_code = fields.Integer(string="Code")
    service = fields.Selection([('x-ray', 'X-Ray'), ('mri', 'MRI'), ('ct', 'CT')], string="Service")
    test_type = fields.Selection([('x-ray', 'X-Ray'), ('mri', 'MRI'), ('ct scan', 'CT Scan')], string="Type")

    def action_create_request(self):
        for rec in self:
            rec.env['hospital.imagingtest'].create({
                'name': self.test_name,
                'date': self.date,
                'patient': self.patient.id,
                'physician': self.physician.id
            })
