BEGIN;

SET client_encoding = 'LATIN1';

CREATE TABLE car (
    car_id SERIAL PRIMARY KEY,
    make text NOT NULL,
    model text NOT NULL
);

INSERT INTO car (make, model)
VALUES 
    ('Ford','Escort'),
    ('Dodge','Ram'),
    ('Chrysler','Impala'),
    ('Honda','Accord'),
    ('Hyundai','Elantra'),
    ('Datsun','310GX'),
    ('Nissan','Xterra'),
    ('Pontiac','Thunderbird'),
    ('Toyota','Tercel'),
    ('Oldsmobile','Cutlass Supreme'),
    ('Jeep','Cherokee');

END;