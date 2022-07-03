# Copyright 2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2018 Rafis Bikbov <https://it-projects.info/team/bikbov>
# Copyright 2021 Denis Mudarisov <https://github.com/trojikman>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
import json
import logging

import werkzeug

from odoo import http
from odoo.tools import date_utils

from odoo.addons.web.controllers.main import ensure_db

_logger = logging.getLogger(__name__)


class OAS(http.Controller):
    @http.route(
        "/api/v1/<namespace_name>/swagger.json",
        type="http",
        auth="none",
        csrf=False,
    )
    def OAS_json_spec_download(self, namespace_name, **kwargs):
        ensure_db()
        namespace = (
            http.request.env["openapi.namespace"]
            .sudo()
            .search([("name", "=", namespace_name)])
        )
        if not namespace:
            raise werkzeug.exceptions.NotFound()
        if namespace.token != kwargs.get("token"):
            raise werkzeug.exceptions.Forbidden()

        response_params = {"headers": [("Content-Type", "application/json")]}
        if "download" in kwargs:
            response_params = {
                "headers": [
                    ("Content-Type", "application/octet-stream; charset=binary"),
                    ("Content-Disposition", http.content_disposition("swagger.json")),
                ],
                "direct_passthrough": True,
            }

        return werkzeug.wrappers.Response(
            json.dumps(namespace.get_OAS(), default=date_utils.json_default),
            status=200,
            **response_params
        )

    @http.route(
        "/api/v2/contacts",
        type="http",
        auth="none",
        csrf=False,
    )
    def get_contacts(self, **kwargs):
        res_partner_ids = http.request.env["res.partner"].sudo().search([])
        res = []
        for res_partner in res_partner_ids:
            res.append({'id': res_partner.id, 'name': res_partner.name, 'email': res_partner.email})
        response = json.dumps(res)
        return response

    @http.route(
        "/api/v2/contact/<contact_id>",
        type="http",
        auth="none",
        csrf=False,
    )
    def get_contact_byid(self, contact_id, **kwargs):
        res_partner_id = http.request.env["res.partner"].sudo().browse(int(contact_id))
        res = []
        if res_partner_id:
            res.append({'id': res_partner_id.id, 'name': res_partner_id.name, 'email': res_partner_id.email})
            response = json.dumps(res)
        else:
            response = json.dumps({'result': 'contact not found!'})
        return response