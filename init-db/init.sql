CREATE TABLE humidity (
    id SERIAL PRIMARY KEY,
    source CHAR(100) NOT NULL,
    station_id CHAR(100) NOT NULL,
    observed_time TIMESTAMP WITH TIME ZONE,
    percent_humidity FLOAT NOT NULL
    );

CREATE TABLE temp_dry (
    id SERIAL PRIMARY KEY,
    source CHAR(100) NOT NULL,
    station_id CHAR(100) NOT NULL,
    observed_time TIMESTAMP WITH TIME ZONE,
    temperature FLOAT NOT NULL
    );

CREATE TABLE pressure (
    id SERIAL PRIMARY KEY,
    source CHAR(100) NOT NULL,
    station_id CHAR(100) NOT NULL,
    observed_time TIMESTAMP WITH TIME ZONE,
    mbar FLOAT NOT NULL
    );