CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> b6d0b7e17d59

INSERT INTO alembic_version (version_num) VALUES ('b6d0b7e17d59');

-- Running upgrade b6d0b7e17d59 -> 9218bace5f9c

ALTER TABLE medical_records ADD COLUMN discharge_time VARCHAR(100);

UPDATE alembic_version SET version_num='9218bace5f9c' WHERE alembic_version.version_num = 'b6d0b7e17d59';

