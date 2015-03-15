Scenarios
=========


Setup
-----

Supervisor
uWSGI
Nginx
Django app
Postgres

1. Code throwing an exception
2. Supervisor config file missing .conf
3. uWSGI config using different port to nginx
4. Password wrong for database
5. nginx server_name wrong
6. Postgres not allowing connections from app
7. uWSGI not setting env var DJANGO_CONF
8. No ALLOWED_HOSTS set
9. uWSGI pid file permissions
10. nginx listening on wrong port
11. Wrong django version installed
12. Application logs not working 'cause LOGGING isn't calling create_logging_dict
13. nginx config in sites-available, not enabled
14. uWSGI drop-after-apps + file permissions
15. DB user permissions
16. IP tables
17. Invisible unicode char