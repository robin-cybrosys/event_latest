from odoo import fields, models, api


class Event(models.Model):
    _inherit = "event.event"

    name_id = fields.Many2one(
        'event.latest', string='event')
    # company_id = fields.Many2one(
    #     'res.company', required=True, default=lambda self: self.env.company)

