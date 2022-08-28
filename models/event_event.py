# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Event(models.Model):
    _inherit = 'event.event'

    university_name = fields.Char('University Name')
    university_code = fields.Char('University Code')
    university_type = fields.Char('University Type')
    event_id = fields.Many2one('event.event', string='Event Name')
    event_type = fields.Many2one(related='event_id.event_type_id',
                                 string='Event Type')
    start_date = fields.Date('Start Date', default=fields.Date.context_today)
    end_date = fields.Date('End Date')
