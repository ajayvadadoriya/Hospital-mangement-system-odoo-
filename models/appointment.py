from odoo import api, fields, models, _


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = 'mail.thread'
    _description = "Appointment Records"
    _rec_name = 'ref'

    patient_id = fields.Many2one('hospital.patient', string="Patient Name", required=True)
    ref = fields.Char(string="Sequence Number", required=True, copy=False, readonly=True, default=lambda self: _('New'))
    age = fields.Integer(string="Age", related='patient_id.age', tracking=True)
    ref1 = fields.Char(string="Sequence Number Of Patient", related='patient_id.ref', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender",
                              related='patient_id.gender',   tracking=True)
    capitalize_name = fields.Char(string='Capitalize Name', related='patient_id.capitalize_name', tracking=True)
    product = fields.Many2one('product.template', string="Product Template")
    appointment_date = fields.Date(string="Date")
    checkup_time = fields.Datetime(string="Checkup Time")
    state = fields.Selection([
        ('draft', "Draft"), ('confirm', "Confirm"), ('done', "Done"), ('canceled', "Canceled")], string="Status",
        default='draft', tracking=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    note = fields.Text(string="Old Prescription", related='patient_id.notes')
    note1 = fields.Text(string="New Prescription")
    prescription_line_ids = fields.One2many('appointment.prescription_lines', 'appointment_id', string="PRESCRIPTION LINE")

    # --------FOR MOVING IN STATUSBAR--------------------------------
    def action_confirm(self):
        # for rec in self:
            # patients = self.env['hospital.patient'].search([])
            # print("patients", patients)

            #----singel search----
            # male_patients = self.env['hospital.patient'].search([('gender', '=', 'male')])
            # print("male patients", male_patients)


            #----search with and----
            # female_patients = self.env['hospital.patient'].search([('gender', '=', 'female'), ('age', '>=', '34')])
            # print("female patients", female_patients)
            # for rec in female_patients:
            #     print("female patients' name:", rec.name)


            #----search with or----
            # female_patients_or = self.env['hospital.patient'].search(['|', ('gender', '=', 'female'), ('age', '>=', '34')])
            # print("female patients", female_patients_or)


            #----search count----
            # total_patients_count = self.env['hospital.patient'].search_count([])
            # print("total patients", total_patients_count)

            # female_patients = self.env['hospital.patient'].search([('age', '>=', '1'), ('age', '<=', '10')])
            # print("female patients", female_patients)
            # for rec in female_patients:
            #     print("female patients' name:", rec.name)

            # female_patients = self.env['hospital.patient'].search([('tag_ids', '!=', 'res.partner.category'),
            #                                                        ('tag_ids', '!=', '')])
            # print("female patients", female_patients)
            # for rec in female_patients:
            #     print("female patients' name:", rec.name)

            #----brows method----
            # browse_result = self.env['hospital.patient'].browse(100)
            # print("browse result is:", browse_result)
            # if browse_result.exists():
            #     print("Exists")
            # else:
            #     print("Nooooooooo")


            #----orm create method----
            # vls ={
            #     'name': 'rehen'
            # }
            # self.env['hospital.patient'].create(vls)


            #----orm write method----
            # record_to_update = self.env['hospital.patient'].browse(17)
            # if record_to_update.exists():
            #     vls = {
            #         'age': '22',
            #         'gender': 'male'
            #     }
            #     record_to_update.write(vls)

            #----orm copy----
            # record_to_copy = self.env['hospital.patient'].browse(12)
            # record_to_copy.copy()

            #----orm unlink----
            # record_to_copy = self.env['hospital.patient'].browse(19)
            # record_to_copy.unlink()

            #----orm mapped----
            # partners = self.env['res.partner'].search([])
            # print("partners----", partners)
            # print("mapped partner----", partners.mapped('name'))
            # print("mapped partner----", partners.sorted(lambda o: o.create_date, reverse=True))
            # print("mapped partner----", partners.filtered(lambda o: o.user_id))
         self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'canceled'
# -------- CREATE SEQUENCE APPOINTMENT --------------------------------
    @api.model_create_multi
    def create(self, vls_list):
        for vls in vls_list:
            vls['ref'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super(HospitalAppointment, self).create(vls_list)

    @api.onchange('patient_id')
    def _onchange_state(self):
        if self.patient_id.capitalize_name:
            self.capitalize_name = self.patient_id.capitalize_name

    # @api.onchange('patient_id')
    # def _onchange_state(self):
    #     if self.patient_id.gender:
    #         self.gender = self.patient_id.gender

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, f'{rec.ref}'))
        return result

#-------ANOTHER MODEL FOR ONE2MANY FIELD------------------------------
class AppointmentPrescriptionLines(models.Model):
    _name = "appointment.prescription_lines"
    _description = "Prescription Records"

    medicine_name = fields.Char(string="Medicine Name")
    qty = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")