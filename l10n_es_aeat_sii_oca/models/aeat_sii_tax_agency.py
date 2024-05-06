# Copyright 2018 Javi Melendez <javimelex@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AeatSiiTaxAgency(models.Model):
    _name = "aeat.sii.tax.agency"
    _description = "Aeat SII Tax Agency"

    name = fields.Char(string="Tax Agency", required=True)
    wsdl_out = fields.Char(string="SuministroFactEmitidas WSDL", required=True)
    wsdl_out_test_address = fields.Char(string="SuministroFactEmitidas Test Address")
    wsdl_in = fields.Char(string="SuministroFactRecibidas WSDL", required=True)
    wsdl_in_test_address = fields.Char(string="SuministroFactRecibidas Test Address")
    wsdl_pi = fields.Char(string="SuministroBienesInversion WSDL", required=True)
    wsdl_pi_test_address = fields.Char(string="SuministroBienesInversion Test Address")
    wsdl_ic = fields.Char(string="SuministroOpIntracomunitarias WSDL", required=True)
    wsdl_ic_test_address = fields.Char(
        string="SuministroOpIntracomunitarias Test Address"
    )
    wsdl_pr = fields.Char(string="SuministroCobrosEmitidas WSDL", required=True)
    wsdl_pr_test_address = fields.Char(string="SuministroCobrosEmitidas Test Address")
    wsdl_ott = fields.Char(string="SuministroOpTrascendTribu WSDL", required=True)
    wsdl_ott_test_address = fields.Char(string="SuministroOpTrascendTribu Test Address")
    wsdl_ps = fields.Char(string="SuministroPagosRecibidas WSDL", required=True)
    wsdl_ps_test_address = fields.Char(string="SuministroPagosRecibidas Test Address")

    agency_aeat_sii_map = fields.Many2one(comodel_name="aeat.sii.map", string="Tax agency", required=True)    
    active = fields.Boolean(string="Activo")
    agency_sii_version = fields.Char(string="Version SII", required=True)

    def _connect_params_sii(self, mapping_key, company):
        self.ensure_one()
        
        if mapping_key == "out_invoice" or mapping_key == "out_refund":
            wsdl_key = self.wsdl_out
            wsdl_test = self.wsdl_out_test_address
        
        elif mapping_key == "in_invoice" or mapping_key == "in_refund":
            wsdl_key = self.wsdl_in
            wsdl_test = self.wsdl_in_test_address
            
        else:
            raise exceptions.UserError("El tipo de factura " + mapping_key + " no puede ser enviado al SII.")

        return {
            "wsdl": wsdl_key,
            "address": wsdl_test if company.sii_test else False,
        
        }
