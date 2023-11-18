FROM postgres
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB formula1

# copy the sql script to create tables
COPY ./sql/create_tables.sql /docker-entrypoint-initdb.d/create_tables.sql
# copy the sql script to fill tables
COPY ./sql/fill_tables.sql /docker-entrypoint-initdb.d/fill_tables.sql

VOLUME /var/lib/postgresql/data