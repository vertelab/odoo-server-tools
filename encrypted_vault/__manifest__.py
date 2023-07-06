# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2022- Vertel AB (<https://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Server Tools: Encrypted Vault',
    'version': '14.0.1.0.0',
    # Version ledger: 14.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary': ' This module uses encrypted fields to store sensitive credentials, and related information',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical',
    'description': """
     This module uses encrypted fields to store sensitive credentials, and related information
    """,
    #'sequence': '1',
    'author': 'Modoolar',
    'website': 'https://modoolar.com',
    'images': ['static/description/banner.png'], # 560x280 px.
    'license': 'LGPL-3',
    'contributor': '',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-server-tools',
    # Any module necessary for this one to work correctly
    'depends': ['base_encrypted_field','web_clipboard',],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/encrypted_vault_data.xml',
        'views/encrypted_vault_history_view.xml',
        'views/encrypted_vault_view.xml',
        'views/encrypted_vault_custom_field_view.xml',
        "views/res_config_settings_view.xml",
        'views/actions.xml',
        'views/menu.xml',
    ],
    'external_dependencies': {
        'python': [
            'cryptography'
        ]
    },
    "application": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
