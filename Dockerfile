FROM postgres
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB stratusgrid
ENV POSTGRES_PORT 5032
ADD init.sql /docker-entrypoint-initdb.d/