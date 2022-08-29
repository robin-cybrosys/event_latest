from odoo import fields, models, api


class Event(models.Model):
    _inherit = "event.event"

    name_id = fields.Many2one(
        'event.latest', string='event')
