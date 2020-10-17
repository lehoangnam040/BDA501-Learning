records = LOAD './input.txt' USING PigStorage(',') AS (matrix:chararray, row:int, col:int, val:float);
X = FILTER records BY matrix == 'X';
Y = FILTER records BY matrix == 'Y';
Z = FOREACH (JOIN X BY col, Y BY row) GENERATE X::row, Y::col, (X::val * Y::val) AS mul;
RES = FOREACH(GROUP Z BY (X::row, Y::col)) GENERATE group, SUM(Z.mul);

DUMP X;
DUMP Y;
DUMP RES;
