from odoo import api, fields, models, _


class BloodDonors(models.Model):
    _name = "blood.donors"
    _rec_name = "donor_id"

    donor_name = fields.Many2one(related="donor_id", string="")
    donor_id = fields.Many2one('res.partner', string="Donor")
    blood_group = fields.Char(string="Blood Group")
    phone = fields.Char(string="Mobile No.")
    e_mail = fields.Char(string="E-mail")
    balance = fields.Float(string="Balance", compute='_compute_total_balance')
    consent = fields.Boolean(string="Consent")
    donate_count = fields.Integer(string="Donate Count", compute='compute_donate_count')
    buy_count = fields.Integer(string="Take", compute='compute_take_count')

    def _compute_total_balance(self):
        for lead in self:
            all_donors = self.env['blood.transaction'].search(
                [('donors_id', '=', lead.id), ('blood_group', '=', lead.blood_group)])
            all_buyer = self.env['blood.buy'].search(
                [('blood_type','=','out'),('blood_group', '=', lead.blood_group)])
            if all_donors:
                for rec in all_donors:
                    lead.balance = lead.balance + rec.quantity

            elif all_buyer:
                for i in all_buyer:
                    lead.balance = lead.balance - i.qty

            else:
                lead.balance = 0

    @api.depends('buy_count')
    def compute_take_count(self):
        for rec in self:
            buy_count = self.env['blood.buy'].search_count([('patient_id', '=', rec.id)])
            rec.buy_count = buy_count

    @api.depends('donate_count')
    def compute_donate_count(self):
        for rec in self:
            donate_count = self.env['blood.transaction'].search_count([('donors_id', '=', rec.id)])
            rec.donate_count = donate_count


    def action_open_transaction(self):
        return {
            'name': 'Donate Transaction',
            'type': 'ir.actions.act_window',
            'res_model': 'blood.transaction',
            'view_mode': 'tree,form',
            'domain': [('donors_id', '=', self.id)],
            'target': 'current',
        }

    def action_open_take(self):
        return {
            'name': 'Buy Transaction',
            'type': 'ir.actions.act_window',
            'res_model': 'blood.buy',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.id)],
            'target': 'current',
        }
