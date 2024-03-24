from typing import Any

from helper_functions import HelperFunctions

set_order_data = [
    { # required fields only
        'user_details_form_data': {
            'name': 'Иван',
            'surname': 'Иванов',
            'address': '',
            'station': 'Лубянка',
            'phone': '+79001231234'
        },
        'order_details_form_data': {
            'date': HelperFunctions.get_tomorrow_date(),
            'duration': 'сутки',
            'color_black': False,
            'color_gray': False,
            'comment': '',
        }
    },
        { # all fields
        'user_details_form_data': {
            'name': 'Иван',
            'surname': 'Иванов',
            'address': 'Тверская улица, дом 13',
            'station': 'Лубянка',
            'phone': '+79001231234'
        },
        'order_details_form_data': {
            'date': HelperFunctions.get_tomorrow_date(),
            'duration': 'сутки',
            'color_black': True,
            'color_gray': True,
            'comment': 'comment comment comment 123 !!',
        }
    }
]
