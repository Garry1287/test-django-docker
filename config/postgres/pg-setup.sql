CREATE DATABASE nlmkdb;
CREATE USER nlmk WITH PASSWORD '';
ALTER ROLE nlmk SET client_encoding TO 'utf8';
ALTER ROLE nlmk SET default_transaction_isolation TO 'read committed';
ALTER ROLE nlmk SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE nlmkdb TO nlmk;
\c nlmkdb
\i /db/nlmkdb.dump
