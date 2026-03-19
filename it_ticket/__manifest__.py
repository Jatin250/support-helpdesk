{
    "name": "Support HelpDesk",
    "version": "1.0",
    "summary": "Track and manage internal support tickets with Kanban & Chatter",
    "description": """
        This module provides a complete IT Helpdesk / Support Ticket system.
        Features include:
        - Auto-sequence ticket generation (TKT-XXXX)
        - Kanban view with drag-and-drop lock
        - Chatter for communication and attachments
        - Role-based access control (User vs Manager)
    """,
    "category": "Operations/Helpdesk",
    "author": "Digimonk Technologies",
    "website": "https://digimonk.in/",
    "license": "LGPL-3",
    "depends": ["base", "mail"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/ticket_sequence.xml",
        "views/ticket_views.xml",
    ],
    "images": ["static/description/icon.png"],
    "installable": True,
    "application": True,
}
