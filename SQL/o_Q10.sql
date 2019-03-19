--1. Does a higher GDP mean more gold medals?
USE olympic;

DROP TABLE IF EXISTS q10;

CREATE TABLE q10
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION '/user/cloudera/olympicOutput/q10'
AS
select country, industry, count(medal) as gold_medals 
from countries join athlete 
on (country = team and medal = "Gold" and year >= 1980) 
group by country, industry;
