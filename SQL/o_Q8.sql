--1. Does a higher GDP mean more gold medals?
USE olympic;

DROP TABLE IF EXISTS q8;

CREATE TABLE q8
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION '/user/cloudera/olympicOutput/q8'
AS
select country, service, count(medal) as gold_medals 
from countries join athlete
on (country = team and medal = "Gold" and year >= 1980) 
group by country, service;
