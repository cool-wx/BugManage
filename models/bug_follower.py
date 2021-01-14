from odoo import models, fields, api


class Follower(models.Model):
    _inherit = 'res.partner'
    bug_ids = fields.Many2many('bug.bug', string='Bug')