FROM postgres:9.4

ADD fix-acl.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/fix-acl.sh