--This is the SQL file for our queries 

create database if not exists olympics;
use olympics;

drop table if exists athlete;
drop table if exists world;

create table athlete(
    id string,
    name string,
    sex string,
    age string,
    height string,
    weight string,
    team string,
    noc string,
    games string,
    year int,
    season string,
    city string,
    sport string,
    event string,
    medal string);

create table world(
    country string,
    region string,
    population int,
    area float,
    pop_density float,
    coastline float,
    net_migration float,
    infant_mortality float,
    gdp float,
    literacy float,
    phones float,
    arable float,
    crops float,
    other float,
    climate float,
    birthrate float,
    deathrate float,
    agriculture float,
    industry float,
    service float);

