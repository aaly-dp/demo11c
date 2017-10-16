

from odoo import api, models


class AccountInvoice(models.AbstractModel):
    _name = 'report.account.report_invoice'
    _inherit = 'report.abstract_report'
    _template = 'account.report_invoice'

    @api.model
    def get_report_values(self, docids, data=None):
        model = 'account.invoice'
        docs = self.env[model].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': docs,
            'data': data,
            'field_set_in_lines': self._field_set_in_lines,
            'formatLang': self._formatLang,
        }

