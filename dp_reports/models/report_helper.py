from odoo import api, models


class ReportHelper(models.AbstractModel):
    _name = "report.abstract_report"

    @api.model
    def _field_set_in_lines(self, lines, field):
        fields = field.split('.')
        for line in lines:
            temp = None
            for idx, field in enumerate(fields):
                if not temp and idx == 0:
                    temp = line.__getattribute__(field)
                elif not temp and idx != 0:
                    return False
                else:
                    temp = temp.__getattribute__(field)
            if not temp:
                return False
        return True

    @api.model
    def _formatLang(self, value, currency=True):
        lang = self.partner_id.lang
        lang_objs = self.env['res.lang'].search([('code', '=', lang)])
        if not lang_objs:
            lang_objs = self.env['res.lang'].search([], limit=1)
        lang_obj = lang_objs[0]

        res = lang_obj.format('%.' + str(2) + 'f', value, grouping=True, monetary=True)
        currency_obj = self.currency_id

        if currency_obj and currency_obj.symbol and currency:
            if currency_obj.position == 'after':
                res = '%s %s' % (res, currency_obj.symbol)
            elif currency_obj and currency_obj.position == 'before':
                res = '%s %s' % (currency_obj.symbol, res)
        return res
