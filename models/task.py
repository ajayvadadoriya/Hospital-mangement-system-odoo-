from odoo import api, fields, models, _


class HospitalTask(models.Model):
    _inherit = 'project.project'

    project_manager = fields.Many2one('res.users', string="Project Manager")
    task_project = fields.Many2one('project.task', string="Project Task")
    location = fields.Many2one('stock.location', string="Location Desc")
    construction_type = fields.Many2one('hospital.construction', string="Construction Type")
    time_sheet = fields.One2many('account.analytic.line', 'sheet', string="Time Sheet")
    picking_count = fields.Integer(string="Picking Count", compute='compute_picking_count')

    @api.depends('picking_count')
    def compute_picking_count(self):
        for rec in self:
            picking_count = self.env['stock.picking'].search_count([('product_id', '=', rec.id)])
            rec.picking_count = picking_count

    def action_open_picking_detail(self):
        return {
            'name': 'Picking',
            'type': 'ir.actions.act_window',
            'res_model': 'stock.picking',
            'view_mode': 'tree,form',
            'domain': [('product_id', '=', self.id)],
            'target': 'current'
        }

class TimeSheet(models.Model):
    _inherit = 'account.analytic.line'

    sheet = fields.Many2one('project.project', string='Sheet')



