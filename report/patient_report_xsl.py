from odoo import models
class PatientCardXlsx(models.AbstractModel):
    _name = 'report.new_hospital.report_patient_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patient):
        sheet = workbook.add_worksheet('Patient Id Card')
        bold = workbook.add_format({'bold': True})
        formate = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': 'green'})
        row = 0
        col = 0
        sheet.set_column('A:B', 25)
        for obj in patient:
            row += 1
            sheet.merge_range(row, col, row, col + 1, 'Patient IdCard', formate)
            row+=1
            sheet.write(row, col, 'Name', bold)
            sheet.write(row, col+1, obj.name)
            row+=1
            sheet.write(row, col, 'Age', bold)
            sheet.write(row, col+1, obj.age)
            row += 1
            sheet.write(row, col, 'Gender', bold)
            sheet.write(row, col + 1, obj.gender)

            row+=2