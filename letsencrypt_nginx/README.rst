.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======================================================
Generate nginx config for letsencrypt.org certificates
======================================================

This module was written to add automatic nginx configuration to the letsencrypt
module. This is performed when requesting a new certificate through the 
letsencrypt cron job. Remember to set a correct *web.base.url* and
*web.base.url.freeze* before running the cron job.

Configuration
=============

Configuration files are generated in
~odoo/.local/share/Odoo/letsencrypt_nginx. You need to configure nginx
to use those files.

Your conf file should start with this::

    #odoo server
    upstream odoo {
     server 127.0.0.1:8069;
    }
    upstream longpolling {
     server 127.0.0.1:8072;
    }
    
    include /var/lib/odoo/.local/share/Odoo/letsencrypt_nginx/*.conf;
