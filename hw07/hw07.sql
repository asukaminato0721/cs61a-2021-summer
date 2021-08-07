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
  SELECT name , size
  from dogs, sizes
  where sizes.min < dogs.height and dogs.height <= sizes.max;

-- name, parent's height
CREATE TABLE child_parent_height AS
  select a.name, b.height
  from dogs as a, dogs as b, parents
  where parents.child = a.name and parents.parent = b.name;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT dogs.name
  from dogs,child_parent_height
  where child_parent_height.name = dogs.name
  order by  child_parent_height.height desc;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child as ac, b.child as bc
  from parents as a, parents as b
  where a.parent = b.parent and a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT 'The two siblings, '|| ac ||' plus '|| bc||' have the same size:'
  from siblings
  where ;


-- Ways to stack 4 dogs to a height of at least 175, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height, n);

-- Add your INSERT INTOs here


CREATE TABLE stacks AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


-- Total size for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


-- Heights and names of dogs that are above average in height among
-- dogs whose height has the same first digit.
CREATE TABLE above_average AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
CREATE TABLE non_parents as
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

