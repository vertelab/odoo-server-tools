# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Let's encrypt nginx",
    "version": "14.0.1.0.0",
    "author": "Vertel AB",
    "license": "AGPL-3",
    "category": "Hidden/Dependency",
    "summary": "Create nginx configs for SSL.",
    "depends": ["letsencrypt",],
    "data": [],
    "installable": True,
    "external_dependencies": {'python3' : ['acme_tiny', 'IPy']},
}
