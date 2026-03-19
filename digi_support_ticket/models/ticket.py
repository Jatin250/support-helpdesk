from odoo import models, fields, api


class ItTicket(models.Model):
    _name = "it.ticket"
    _description = "IT Support Ticket"

    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Ticket Reference",
        required=True,
        copy=False,
        readonly=True,
        default="New",
    )

    issue_title = fields.Char(string="Issue Title", required=True, tracking=True)
    description = fields.Text(string="Issue Description", required=True)

    reported_by_id = fields.Many2one(
        "res.users",
        string="Reported By",
        default=lambda self: self.env.user,
        readonly=True,
    )

    priority = fields.Selection(
        [("0", "Low"), ("1", "Medium"), ("2", "High"), ("3", "Urgent")],
        string="Priority",
        required=True,
        default="1",
        tracking=True,
    )

    state = fields.Selection(
        [
            ("new", "New"),
            ("in_progress", "In Progress"),
            ("resolved", "Resolved"),
            ("closed", "Closed"),
        ],
        string="Status",
        default="new",
        group_expand="_expand_states",
        tracking=True,
    )

    assigned_to_id = fields.Many2one("res.users", string="Assigned To", tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = (
                    self.env["ir.sequence"].next_by_code("it.ticket") or "New"
                )
        return super().create(vals_list)

    # ==========================================
    # KANBAN COLUMN LOCK
    # ==========================================
    @api.model
    def _expand_states(self, states, domain, order=None):
        return ["new", "in_progress", "resolved", "closed"]

    # ==========================================
    # ACTION BUTTONS (WORKFLOW)
    # ==========================================
    def action_in_progress(self):
        for rec in self:
            rec.state = "in_progress"
            if not rec.assigned_to_id:
                rec.assigned_to_id = self.env.user.id

    def action_resolved(self):
        for rec in self:
            rec.state = "resolved"

    def action_closed(self):
        for rec in self:
            rec.state = "closed"
