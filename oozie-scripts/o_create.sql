CREATE DATABASE IF NOT EXISTS olympic;

USE olympic;

DROP TABLE IF EXISTS athlete;
DROP TABLE IF EXISTS countries;

CREATE TABLE athlete(
    id int,
    name string,
    sex string,
    age string,
    height string,
    weight string,
    team string,
    noc string,
    games string,
    year string,
    season string,
    city string,
    sport string,
    event string,
    medal string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';

CREATE TABLE countries(
    country string,
    region string,
    population int,
    area int,
    pop_density double,
    coastline double,
    net_migration double,
    infant_mortality double,
    gdp int,
    literacy double,
    phone_1000 double ,
    arable double,
    crops double,
    other double,
    climate double,
    birthrate double,
    deathrate double,
    agriculture double,
    industry double,
    service double)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';
