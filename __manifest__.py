# --------------FOR CREATE MODULS -------------
{
    'name': 'Applo Hospital Management',
    'author': 'Ajay Tech',
    'website': 'www.Hospital.com',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'depends': ['project','analytic','hr'
                ],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'security/security_access.xml',
        'reports/report.xml',
        'reports/construction_report.xml',
        'views/construction.xml',
        'views/task.xml',
        'views/project.xml',
        'views/menu.xml',



    ]

}
