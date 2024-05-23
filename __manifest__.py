# --------------FOR CREATE MODULS -------------
{
    'name': 'Hospital Management',
    'author': 'Ajay Tech',
    'website': 'www.Hospital.com',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'depends': ['mail', 'product', 'report_xlsx'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'wizard/create_appointment_view.xml',
        'report/patient_card.xml',
        'report/wizard_report.xml',
        'report/reports.xml',
        'views/appointment.xml',
        'views/patient.xml',
        'views/kids.xml',
        'views/doctor.xml',
        'views/menu.xml',


    ]

}
