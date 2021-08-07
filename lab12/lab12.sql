.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet 
  FROM students 
  WHERE color = 'blue' and pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet,song 
  FROM students 
  WHERE color = 'blue' AND pet = 'dog';

-- The shared preferred pet of the couple
-- The shared favorite song of the couple
-- The favorite color of the first person
-- The favorite color of the second person

CREATE TABLE matchmaker AS
  SELECT s1.pet, s1.song, s1.color, s2.color
  FROM students AS s1, students AS s2
  where s1.pet = s2.pet and s1.song = s2.song and s1.time < s2.time;

-- Write a SQL query to create a table with just the column seven from students, filtering first for students who said their favorite number (column number) was 7 in the students table and who checked the box for seven (column '7') in the numbers table.

CREATE TABLE sevens AS
  select s.seven
  from students as s, numbers as n
  where s.number = 7 and n.'7'='True' and s.time = n.time;


CREATE TABLE favpets AS
  SELECT s.pet, count(s.pet)
  from students as s
  group by s.pet
  order by count(s.pet)
  desc
  limit 10;


CREATE TABLE dog AS
  SELECT s.pet, count(*) as counts
  from students as s
  where s.pet = 'dog'
  group by s.pet;


CREATE TABLE bluedog_agg AS
  SELECT song , count(*) as counts
  from bluedog_songs
  group by song
  order by counts desc;


CREATE TABLE instructor_obedience AS
  SELECT seven , instructor , COUNT(instructor)
  from students
  where seven = '7' 
  GROUP BY instructor;

-- https://github.com/sgalal/cs61a/blob/0b3e5b4d1672e682ef4b29a6e38f6505cc295607/Labs/lab13/lab13.sql#L21
CREATE TABLE smallest_int_having AS
  SELECT time,smallest as s
  from students
  group by s
  having count(s) =1;


CREATE TABLE smallest_int_count AS
  SELECT smallest , count(smallest)
  from students
  group by smallest;
