

from odoo import api, models


class StockPicking(models.AbstractModel):
    _name = 'report.stock.report_deliveryslip'
    _inherit = 'report.abstract_report'
    _template = 'stock.report_deliveryslip'

    @api.model
    def get_report_values(self, docids, data=None):
        model = 'stock.picking'
        docs = self.env[model].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': docs,
            'data': data,
            'field_set_in_lines': self._field_set_in_lines,
            'formatLang': self._formatLang,
        }
