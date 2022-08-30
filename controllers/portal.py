# -*- coding: utf-8 -*-
from odoo import http, SUPERUSER_ID, fields
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal


class EventPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'event_count' in counters:
            event_count = request.env['event.latest'].search_count(
                self._get_events_domain()) if request.env[
                'event.latest'].check_access_rights(
                'read', raise_exception=False) else 0
            values['event_count'] = event_count
        return values

    # checking domain: user & payslips_state
    def _get_events_domain(self):
        # print(fields.Date.today(),
        #       fields.Date.subtract(fields.Date.today(), months=3))
        return [
            ('start_date', '>=',
             fields.Date.subtract(fields.Date.today(), months=3)),
            ('state', 'in', ('ongoing', 'expired'))]

    @http.route(['/my/events'], type='http', auth="user", website=True)
    def portal_my_events(self):
        user = request.env.user
        domain = self._get_events_domain()
        events = request.env['event.latest'].search(domain)
        values = {
            'events': events,
            'page_name': 'event',
        }
        return request.render("event_latest.portal_my_events",
                              values)

    @http.route(['/events/view/<int:event_id>'], type='http', auth="user",
                website=True)
    def event_report(self, event_id):
        event = request.env['event.event'].search(
            # ('state', 'in', ('ongoing', 'expired')),
            [('id', '=', event_id)])
        value = {
            'events': event
        }
        return request.render('event_latest.your_template',value)
