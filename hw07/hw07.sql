CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
-- Create a size_of_dogs table with two columns, one for each dog's name and another for its size.
CREATE TABLE size_of_dogs AS
SELECT  name
       ,size
FROM dogs, sizes
WHERE sizes.min < dogs.height
AND dogs.height <= sizes.max;
-- name, parent's height
CREATE TABLE child_parent_height AS
SELECT  a.name
       ,b.height
FROM dogs AS a, dogs AS b, parents
WHERE parents.child = a.name
AND parents.parent = b.name;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
SELECT  dogs.name
FROM dogs, child_parent_height
WHERE child_parent_height.name = dogs.name
ORDER BY child_parent_height.height desc;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
SELECT  a.child AS ac
       ,b.child AS bc
FROM parents AS a, parents AS b
WHERE a.parent = b.parent
AND a.child < b.child;
-- Sentences about siblings that are the same size
-- https://github.com/yngz/cs61a/blob/master/homework/hw11/hw11.sql
CREATE TABLE sentences AS
  SELECT 'The two siblings, ' || p1.child || ' plus '|| p2.child ||' have the same size: '|| s1.size
  FROM parents AS p1, parents AS p2, size_of_dogs AS s1, size_of_dogs AS s2
  WHERE p1.parent = p2.parent
    AND p1.child = s1.name 
    AND p2.child = s2.name
    AND p1.child < p2.child
    AND s1.size = s2.size;



-- Ways to stack 4 dogs to a height of at least 175, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height, n);

-- Add your INSERT INTOs here

-- https://github.com/yngz/cs61a/blob/master/homework/hw11/hw11.sql
CREATE TABLE stacks AS
  SELECT a.name || ", " || b.name || ", " || c.name || ", " || d.name,
  a.height + b.height + c.height + d.height AS total_height
  FROM dogs AS a, dogs AS b, dogs AS c, dogs AS d
  WHERE a.height + b.height + c.height + d.height > 175
    AND a.height < b.height
    AND b.height < c.height
    AND c.height < d.height
  ORDER BY total_height;


-- Total size for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
SELECT  fur
       ,SUM(height)
FROM dogs
GROUP BY  fur
HAVING MIN(height) > 0.7 * AVG(height) AND MAX(height) < 1.3 * AVG(height);
-- Heights and names of dogs that are above average in height among
-- dogs whose height has the same first digit.

CREATE TABLE tallest AS WITH avgHeight AS
(
	SELECT  height / 10 AS ten
	       ,AVG(height) AS a
	FROM dogs
	GROUP BY  height / 10
)
SELECT  height
       ,name
FROM dogs, avgHeight
WHERE avgHeight.ten = height / 10
AND height > avgHeight.a
GROUP BY  height / 10
HAVING COUNT(height) >= 1;

-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
CREATE TABLE non_parents AS
SELECT  "REPLACE THIS LINE WITH YOUR SOLUTION";