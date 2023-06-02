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

The configuration template(s) nginx_template.conf need to put into the data_dir
directory or a subfolder. If not using the default name or if a database need
to use a particular one, set the letsencrypt_nginx.template_conf parameter on
each effected database. The parameter is path to the file relative to data_dir.

If the template file can't be find a fallback version will be used.

Nginx configuration files are generated in
~odoo/.local/share/Odoo/letsencrypt_nginx. You need to configure nginx
to use those files.

Your conf file should start with this::

    #odoo server
    upstream odoo {
     server 127.0.0.1:8069;
    }
    upstream websocket {
     server 127.0.0.1:8072;
    }

    include /var/lib/odoo/.local/share/Odoo/letsencrypt_nginx/*.conf;
