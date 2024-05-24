from odoo import api, fields, models, _


class CreateBedTransferWizard(models.TransientModel):
    _name = "create.bed.transfer.wizard"
    _description = "Create Bed Transfer Wizard"

    bed_from=fields.Selection([('1','1')],string="From",default='1')
    to_bed=fields.Selection([('1','1'),('2','2'),('3','3')],string="To",default='1')
    new_bad=fields.Char(string="New Bed")
    reason=fields.Char(string="Reason")
    hospital_id=fields.Many2one('patient.hospitalization',string="")
    date =fields.Datetime(string="Date", default=fields.Datetime.today())

    def action_bed_transfer(self):
        record_ids = self._context.get('active_ids')
        if record_ids:
            patient = self.env['patient.hospitalization'].browse(record_ids[0])
            if patient:
                patient.bed_ids = [(0, 0, {
                    'date': self.date,
                    'bed_from': self.bed_from,
                    'to_bed': self.to_bed,
                    'reason': self.reason
                })]