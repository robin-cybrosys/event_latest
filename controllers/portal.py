# -*- coding: utf-8 -*-
from odoo import http, SUPERUSER_ID
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal


class EventPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'event_count' in counters:
            event_count = request.env['event.event'].search_count(
                self._get_events_domain()) if request.env[
                'event.event'].check_access_rights(
                'read', raise_exception=False) else 0
            values['event_count'] = event_count
        return values

    # checking domain: user & payslips_state
    def _get_events_domain(self):
        return [
            # ('employee_id.user_id', '=', request.uid),
                ('state', 'in', ('draft', 'ongoing', 'expired'))]

    @http.route(['/my/events'], type='http', auth="user", website=True)
    def portal_my_events(self):
        user = request.env.user
        domain = self._get_events_domain()
        events = request.env['event.event'].search(domain)
        values = {
            'events': events,
            'page_name': 'event',
        }
        return request.render("website_employee_payslip.portal_my_events",
                              values)

    @http.route(['/print/report/<int:event_id>'], type='http', auth="user",
                website=True)
    def event_report(self, event_id):
        event = request.env['event.event'].search(
            [('employee_id.user_id', '=', request.env.user.id),
             ('state', 'in', ('verify', 'done')),
             ('id', '=', event_id)])
        value = {
            'event': event
        }
        pdf = request.env.ref(
            'website_employee_payslip.report_payslip').with_context(
            value)._render_qweb_pdf([event])[0]
        pdfhttpheaders = [('Content-Type', 'application/pdf'),
                          ('Content-Length', len(pdf))
                          ]
        return request.make_response(pdf, headers=pdfhttpheaders)
