# -*- coding: utf-8 -*-
from odoo import api, fields, models


class LatestEvent(models.Model):
    _name = 'event.latest'

    university_name = fields.Char('University Name',required=True)
    university_code = fields.Char('University Code')
    university_type = fields.Char('University Type')
    event_id = fields.Many2one('event.event', string='Event Name')
    event_type = fields.Many2one(related='event_id.event_type_id',
                                 string='Event Type')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'Ongoing'),
        ('expired', 'Expired')
    ], string='Status', readonly=True, copy=False, index=True, tracking=True,
        default='draft')
    start_date = fields.Datetime(
        'Start Date', default=fields.Date.today)
    end_date = fields.Datetime(
        'End Date', default=fields.Date.add(fields.Date.today(), days=3))
    event_ids = fields.One2many(
        'event.event', 'name_id', string="Event", store=True)

