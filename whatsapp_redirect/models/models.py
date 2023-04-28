from odoo import models, fields, api, _


class ClothRequestDetails(models.Model):
    _inherit = 'cloth.request.details'

    is_start = fields.Boolean(
        compute='_compute_is_start'
    )
    @api.depends('stage_id')
    def _compute_is_start(self):
        start_stage = self.env.ref('cloth_tailor_management_odoo.start_stage_id').id
        for rec in self:
            if start_stage == rec.stage_id.id:
                rec.is_start = True
            else:
                rec.is_start = False

    def send_msg(self):
        return {'type': 'ir.actions.act_window',
                'name': _('Whatsapp Message'),
                'res_model': 'whatsapp.message.wizard',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_user_id': self.partner_id.id,
                            'default_message': 'عملينا العزبز يرجي العلم بانه تم البدأ في تنفيذ الثوب الخاص بك وسيتم ارسال رسالة اخري عند الانتهاء'},
                }


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def send_msg(self):
        return {'type': 'ir.actions.act_window',
                'name': _('Whatsapp Message'),
                'res_model': 'whatsapp.message.wizard',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_user_id': self.partner_id.id,
                            'default_message': 'عملينا العزبز يرجي العلم بانه تم الانتهاء من تنفيز الثزب الخاص بك والرجاء التوجه للاستلام'},
                }
