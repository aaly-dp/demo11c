

from odoo import api, models


class PurchaseQuotation(models.AbstractModel):
    _name = 'report.purchase.report_purchasequotation'
    _inherit = 'report.abstract_report'
    _template = 'purchase.report_purchasequotation'

    @api.model
    def get_report_values(self, docids, data=None):
        model = 'purchase.order'
        docs = self.env[model].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': docs,
            'data': data,
            'field_set_in_lines': self._field_set_in_lines,
            'formatLang': self._formatLang,
        }


class PurchaseOrder(models.AbstractModel):
    _name = 'report.purchase.report_purchaseorder'
    _inherit = 'report.abstract_report'
    _template = 'purchase.report_purchaseorder'

    @api.model
    def get_report_values(self, docids, data=None):
        model = 'purchase.order'
        docs = self.env[model].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': docs,
            'data': data,
            'field_set_in_lines': self._field_set_in_lines,
            'formatLang': self._formatLang,
        }


