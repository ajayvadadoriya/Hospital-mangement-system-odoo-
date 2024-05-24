from odoo import api, fields, models, _


class CreateBloodTakeWizard(models.TransientModel):
    _name = "create.blood.take.wizard"
    _description = "Create Blood Take Wizard"

    donors_id=fields.Many2one('res.partner',string="Donors")
    blood_group=fields.Char(string="Blood Group")
    blood_type=fields.Selection([('in','In'),('out','Out')],string="Type",default="out")
    transfer_date=fields.Datetime(string="Date")
    quantity=fields.Float(string="Quantity")



    def action_create_blood_take(self):
        for rec in self:
            rec.env['blood.buy'].create({
                # 'partner_id': self.donors_id.donor_id.id,
                'patient_id': self.donors_id.id,
                'blood_group': self.blood_group,
                'buy_date': self.transfer_date,
                'qty': self.quantity
            })