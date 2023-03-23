from odoo import api, fields, tools, models, _
from datetime import datetime


class RejectionReasonWizard(models.TransientModel):
    _name = 'sh.reject.reason.wizard'
    _description = "Reject reason wizard"

    name = fields.Char(string="Reason", required=True)

    def action_reject_order(self):
        
        active_obj = self.env[self.env.context.get('active_model')].browse(
            self.env.context.get('active_id'))
        active_obj.write({
            'reject_reason': self.name,
            'reject_by': active_obj.env.user,
            'rejection_date': datetime.now(),
        })

        return True