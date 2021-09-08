# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Servertools Module Remover",
    "version": "12.0.0.1.0",
    "summary": " This module adds a Server Action to remove modules that are not used from the server. "
               "It is done to reduce the risk of having vulnerabilities entered to the system without notice.",
    "author": "Vertel AB",
    "license": "AGPL-3",
    "website": "https://vertel.se/",
    "category": "Tools",
    "depends": [],
    "external_dependencies": [],
    "data": [
        'data/server_actions.xml',
        'data/data.xml'
    ],
    "application": True,
    "installable": True,
}
