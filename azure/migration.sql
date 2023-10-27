CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> f2ec783b77cf

INSERT INTO alembic_version (version_num) VALUES ('f2ec783b77cf');

-- Running upgrade f2ec783b77cf -> b5c9b74f8bc8

ALTER TABLE medical_records ADD COLUMN discharge_time VARCHAR(100);

UPDATE alembic_version SET version_num='b5c9b74f8bc8' WHERE alembic_version.version_num = 'f2ec783b77cf';

