from odoo import api, fields, models, _


class CreateBloodTransferWizard(models.TransientModel):
    _name = "create.blood.transfer.wizard"
    _description = "Create Blood Transfer Wizard"

    donors_id=fields.Many2one('blood.donors',string="Donors")
    blood_group=fields.Char(related='donors_id.blood_group',string="Blood Group")
    blood_type=fields.Selection([('in','In'),('out','Out')],string="Type",default="in")
    transfer_date=fields.Datetime(string="Date")
    quantity=fields.Float(string="Quantity")

    def action_blood_transfer(self):
        for rec in self:
            rec.env['blood.transaction'].create({
                # 'partner_id': self.donors_id.donor_id.id,
                'donors_id': self.donors_id.id,
                'blood_group': self.blood_group,
                'blood_type': self.blood_type,
                'transfer_date': self.transfer_date,
                'quantity': self.quantity
            })