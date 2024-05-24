from odoo import api, fields, models,_



class FamilyMember(models.Model):
    _name = "family.member"
    _description = "Member Record"

    name = fields.Char(string="Display Name")
    phone = fields.Char(string="Phone")
    mail = fields.Char(string="E-mail")
    sperson = fields.Many2one('res.partner' ,string="Salesperson")
    act_ids = fields.Many2many('res.partner.category', 'hospital_patient_tag_rel', 'tag_id',
                               string="Tags")
    city = fields.Char(string="City")
    country = fields.Char(string="Country")
    member_id = fields.Many2one('hospital.family', string="Members")