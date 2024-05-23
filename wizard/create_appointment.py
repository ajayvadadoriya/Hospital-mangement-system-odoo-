from odoo import api, fields, models, _


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard("


    patient_id = fields.Many2one('hospital.patient', string="Patient Name", required=True)
    date = fields.Date(string="Date")


    # def action_create_appointment(self):
    #     vals = {
    #         'patient_id': self.patient_id.id,
    #         'appointment_date': self.date
    #     }
    #     self.env['hospital.appointment'].create(vals)
    def action_create_appointment(self):
        for rec in self:
            rec.env['hospital.appointment'].create({
                'patient_id': self.patient_id.id,
                'appointment_date': self.date
            })

    # def print_report(self):
    #     data = {
    #         'model':'create.appointment.wizard',
    #         'form': self.read()[0]
    #     }
    #     if data['form']['patient_id']:
    #         select_patient =data['form']['patient_id'][0]
    #         appointment=self.env['hospital.appointment'].search([('patient_id', '=', select_patient)])
    #     else:
    #         appointment = self.env['hospital.appointment'].search([])
    #     appointment_list=[]
    #     for i in appointment:
    #         vals = {
    #             'name':i.patient_id,
    #             # 'age':i.age,
    #             # 'appointment_date':i.date
    #         }
    #         appointment_list.append(vals)
    #     data['appointment'] =appointment_list
    #     return self.env.ref('new_hospital.report_appointment').report_action(self,data=data)

    def action_view_appointment(self):
        action = self.env.ref('new_hospital.action_hospital_appointment').read()[0]
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return action
