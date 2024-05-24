from odoo import api, fields, models,_


class HospitalFamily(models.Model):
    _name = "hospital.family"
    _description ="Family Details"


    f_id=fields.Many2one('hospital.patient',string="Patient")
    fname = fields.Char(related="f_id.family",string="Family")
    operational = fields.Char(string="Operational Sector")
    member_ids = fields.One2many('family.member', 'member_id', string="Members")
    hff = fields.Selection([('verymuch', 'Very much'),('little', 'Little')], string="Help from family")
    pd = fields.Selection([('moderately', 'Moderately'),('notmoderately', 'Not Moderately')], string="Problems Discussion")
    dm = fields.Selection([('moderately', 'Moderately'),('notmoderately','Not Moderately')], string="Decision making")
    ts = fields.Selection([('verymuch', 'Very much'),('little', 'Little')], string="Time Sharing")
    fa = fields.Selection([('moderately', 'Moderately'),('notmoderately','Not Moderately')], string="Family affection")

