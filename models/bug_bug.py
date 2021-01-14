from odoo import models, fields, api


class Bug(models.Model):
    _name = 'bug.bug'
    _description = 'Bug'
    name = fields.Char('Bug简述', required=True)
    detail = fields.Text('详情')
    is_closed = fields.Boolean('是否关闭')
    close_reason = fields.Selection([('changed', '已修改'),
                                     ('cannot', '无法修改'),
                                     ('delay', '推迟')],
                                    string='关闭原因')
    user_id = fields.Many2one('res.users', string='负责人', default=lambda self: self.env.user)
    follower_id = fields.Many2many('res.partner', string='关注者')

    def do_close(self):
        for bug in self:
            bug.is_closed = not bug.is_closed
            bug.close_reason = ""
        return True
