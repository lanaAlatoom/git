from odoo import models, fields, api


class WorkfetchLocationfetchs(models.Model):
    _inherit = "res.partner"

    is_today = fields.Boolean(string='is today?', default=True)
    provider_latitude = fields.Float(string='latitude', digits=(16, 7))
    provider_longitude = fields.Float(string='longitude', digits=(16, 7))
    description = fields.Char(string='location Fetch')
