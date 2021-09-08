import os
import shutil

from odoo.exceptions import UserError
from odoo import models, fields, _

class Modules(models.Model):
    _inherit = "ir.module.module"

    def find(self, name, path):
        for root, dirs, files in os.walk(path):
            if root.split('/')[-1] == name:
                return root

    def remove_selected_module_from_server(self):
        dir_path = self.env['ir.config_parameter'].sudo().get_param('path_to_remove_module_from_server')
        if not dir_path:
            raise UserError(_(
                'Please configure path of parent directory in System Parameter with'
                ' path_to_remove_module_from_server key!'))
        module_obj = self.env['ir.module.module']
        for module in self:
            if module.state in ('uninstalled', 'uninstallable'):
                path = self.find(module.name, dir_path)
                try:
                    shutil.rmtree(path)
                    module.unlink()
                    module_obj.update_list()
                except Exception as e:
                    raise UserError("Could not Find module in server!")

