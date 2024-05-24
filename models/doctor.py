from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Hospital Doctors Details"
    _rec_name="name"
    name = fields.Char(compute='doctor_full_name', tracking=True)
    ref = fields.Char(string="Ref Code", tracking=True)
    first_name = fields.Char(string="First Name", tracking=True)
    middle_name = fields.Char(string="Middle Name", tracking=True)
    last_name = fields.Char(string="Last Name", tracking=True)
    date_of_birth = fields.Date(string="Birth Date", tracking=True)
    age = fields.Integer(string="Doctor Age", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    phone = fields.Char(string="Contact Number", tracking=True)
    address = fields.Char(string="Address", tracking=True)
    city = fields.Char(string="City", tracking=True)
    pin_code = fields.Char(string="Pin Code", tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
    doctor_image = fields.Image(string="Doctor Image")
    education = fields.Char(string="Education", tracking=True)
    specialization = fields.Char(string="Specialization", tracking=True)
    experience = fields.Char(string="Experience", tracking=True)
    join_date = fields.Date(string="Join Date", tracking=True)

    @api.depends('first_name', 'last_name')
    def doctor_full_name(self):
        for rec in self:
            rec.name = (rec.first_name or '') + ' ' + (rec.last_name or '')

    def name_get(self):
        return [(rec.id, "[%s] %s" % (rec.ref, rec.name)) for rec in self]

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.doctor.sequence')
        return super(HospitalDoctor, self).create(vals)

