CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> e96a902d2da5

ALTER TABLE patients DROP COLUMN is_alive;

INSERT INTO alembic_version (version_num) VALUES ('e96a902d2da5');

-- Running upgrade e96a902d2da5 -> 2dbdcdc8f6c3

ALTER TABLE patients ADD COLUMN is_alive VARCHAR(50) NOT NULL;

UPDATE alembic_version SET version_num='2dbdcdc8f6c3' WHERE alembic_version.version_num = 'e96a902d2da5';

