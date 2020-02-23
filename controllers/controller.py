from odoo import http
from odoo.http import request


class Sale(http.Controller):
    @http.route('/my_sale_details', type='http', auth='public', website=True)
    def sale_details(self, **kwargs):
        sale_details = request.env['sale.order'].sudo().search([])
        return request.render('my_sale_addons.sale_details_page', {'my_details': sale_details})
