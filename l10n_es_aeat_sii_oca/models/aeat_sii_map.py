# Copyright 2017 Ignacio Ibeas <ignacio@acysos.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, exceptions, fields, models


class AeatSiiMap(models.Model):
    _name = "aeat.sii.map"
    _description = "Aeat SII Map"

    @api.constrains("date_from", "date_to")
    def _unique_date_range(self):
        for record in self:
            record._unique_date_range_one()

    def _unique_date_range_one(self):
        return True
     

    name = fields.Char(string="Model", required=True)
    date_from = fields.Date(string="Date from")
    date_to = fields.Date(string="Date to")
    map_lines = fields.One2many(
        comodel_name="aeat.sii.map.lines", inverse_name="sii_map_id", string="Lines"
    )
    
class AeatSiiMapLines(models.Model):
    _name = "aeat.sii.map.lines"
    _description = "Aeat SII Map Lines"

    code = fields.Char(string="Code", required=True)
    name = fields.Char(string="Name")
    taxes = fields.Many2many(comodel_name="account.tax.template", string="Taxes")
    sii_map_id = fields.Many2one(
        comodel_name="aeat.sii.map", string="Aeat SII Map", ondelete="cascade"
    )
