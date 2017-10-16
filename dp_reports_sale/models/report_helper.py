

from odoo import api, models


class SaleOrder(models.AbstractModel):
    _name = 'report.sale.report_saleorder'
    _inherit = 'report.abstract_report'
    _template = 'sale.report_saleorder'

    @api.model
    def get_report_values(self, docids, data=None):
        model = 'sale.order'
        docs = self.env[model].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': docs,
            'data': data,
            'field_set_in_lines': self._field_set_in_lines,
            'formatLang': self._formatLang,
        }
