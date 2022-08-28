# -*- coding: utf-8 -*-
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
        'base', 'website', 'base_setup',
        'event', 'website_event', 'portal', 'utm'],
    'data': [
        'views/event_event.xml',
        # 'views/event_latest.xml'
    ],
}
