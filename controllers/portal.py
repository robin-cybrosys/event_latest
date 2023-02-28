# -*- coding: utf-8 -*-

from odoo import fields, http
from odoo.addons.portal.controllers import portal
from odoo.http import request


class EventPortal(portal.CustomerPortal):

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

    # def _prepare_event_portal_rendering_values(
    #         self, page=1, date_begin=None, date_end=None, sortby=None,
    #         event_page=False, **kwargs
    # ):
    #     SaleOrder = request.env['sale.order']
    #
    #     # if not sortby:
    #     #     sortby = 'date'
    #
    #     partner = request.env.user.partner_id
    #     values = self._prepare_portal_layout_values()
    #
    #     if event_page:
    #         url = "/my/quotes"
    #         domain = self._prepare_quotations_domain(partner)
    #     else:
    #         url = "/my/orders"
    #         domain = self._prepare_orders_domain(partner)
    #
    #     # searchbar_sortings = self._get_sale_searchbar_sortings()
    #     #
    #     # sort_order = searchbar_sortings[sortby]['order']
    #     #
    #     # if date_begin and date_end:
    #     #     domain += [('create_date', '>', date_begin),
    #     #                ('create_date', '<=', date_end)]
    #
    #     # pager_values = portal_pager(
    #     #     url=url,
    #     #     total=SaleOrder.search_count(domain),
    #     #     page=page,
    #     #     step=self._items_per_page,
    #     #     url_args={'date_begin': date_begin, 'date_end': date_end,
    #     #               'sortby': sortby},
    #     # )
    #     # orders = SaleOrder.search(domain, order=sort_order,
    #     #                           limit=self._items_per_page,
    #     #                           offset=pager_values['offset'])
    #
    #     values.update({
    #         # 'date': date_begin,
    #         # 'quotations': orders.sudo() if event_page else SaleOrder,
    #         # 'orders': orders.sudo() if not event_page else SaleOrder,
    #         'page_name': 'quote' if event_page else 'order',
    #         # 'pager': pager_values,
    #         'default_url': url,
    #         # 'searchbar_sortings': searchbar_sortings,
    #         # 'sortby': sortby,
    #     })
    #
    #     return values

    @http.route(['/my/events'], type='http', auth="user", website=True)
    def portal_my_events(self):
        # values = self._prepare_event_portal_rendering_values(
        #     event_page=True, **kwargs)
        user = request.env.user
        domain = self._get_events_domain()
        events = request.env['event.latest'].search(domain)
        values = {
            'default_url' : "/my/events",
            'events': events,
            'page_name': 'event',
        }
        return request.render("event_latest.portal_my_events",
                              values)

    # @http.route(['/events/view/<int:event_id>'], type='http', auth="user",
    #             website=True)
    # def event_report(self, event_id):
    #     event = request.env['event.event'].search(
    #         # ('state', 'in', ('ongoing', 'expired')),
    #         [('id', '=', event_id)])
    #     value = {
    #         'events': event
    #     }
    #     return request.render('event_latest.your_template',value)
