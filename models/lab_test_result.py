from odoo import api, fields, models

class LabTestResult(models.Model):
    _name = "hospital.lab.test.result"
    _rec_name="ref"

    ref = fields.Char(string="ID", tracking=True)
    test_type=fields.Many2one('draft.lab.test',string="Test Type")
    pathologist=fields.Char(string="Pathologist")
    doctor_id=fields.Many2one('hospital.doctor',string="Physician")
    pathology_group=fields.Many2one('hospital.pathology',string="Pathology Group")
    analysis_date=fields.Datetime(related="test_type.test_date",string="Date of the Analysis")
    request_date=fields.Datetime(string="Date Requested")
    patient_id=fields.Many2one('hospital.patient',string="Patient")
    cases_ids=fields.One2many('hospital.lab.test.resultlines','result_id',string="")
    result=fields.Text(string="Result")
    diagnosis_id=fields.Many2one('hospital.diseases',string="Diagnosis")

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.lab.test.result.sequence')
        return super(LabTestResult, self).create(vals)


class LabTestResultLines(models.Model):
    _name = "hospital.lab.test.resultlines"


    sequence = fields.Integer(string='Sequence', default=lambda self: self.env['ir.sequence'].next_by_code('hospital.lab.test.resultlines.sequence'))
    lines_name=fields.Char(string="Name")
    result_text=fields.Integer(string="Result Text")
    normal_range=fields.Float(string="Normal Range")
    units=fields.Many2one('uom.uom',string="Units")
    result_id=fields.Many2one('hospital.lab.test.result',string="")