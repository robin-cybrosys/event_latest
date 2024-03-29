# -*- coding: utf-8 -*-
{
    'name': "Upcoming Events",
    'application': "True",
    'author': "R",
    'website': "http://www.cybrosys.com",
    'sequence': "-1",
    'licence': "LGPL-3",
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'depends': [
        'base','web', 'website', 'base_setup',
        'event', 'website_event', 'portal', 'utm'],
    'data': [
        'views/event_event.xml',
        'data/sequence_data.xml',
        'security/ir.model.access.csv',
        'views/event_portal_template.xml',
        'views/event_latest.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            # 'event_latest/static/src/js/*',
            'event_latest/static/src/js/event_details.js',
        ],

        # 'web.assets_qweb': [
        #     'event_latest/static/src/xml/event_details.xml'
        # ],
    },
}
