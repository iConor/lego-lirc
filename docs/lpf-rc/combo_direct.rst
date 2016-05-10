Combo Direct Mode
=================

Binary Representation
---------------------

+---------------------------+---------------------+---------------+
| Nibble 1                  | Nibble 2            | Nibble 3      |
+--------+--------+---------+---------+-----------+---------------+
| Toggle | Escape | Channel | Address | Mode      | Data          |
+--------+--------+----+----+---------+---+---+---+---+---+---+---+
|      0 |      0 |  C |  C |       0 | 0 | 0 | 1 | B | B | A | A |
+--------+--------+----+----+---------+---+---+---+---+---+---+---+

Field Descriptions
------------------

+----------+----+-------+----------------------------+
| Output B | BB || 00xx || Float output B            |
|          |    || 01xx || Forward on output B       |
|          |    || 10xx || Backward on output B      |
|          |    || 11xx || Brake then float output B |
+----------+----+-------+----------------------------+
| Output A | AA || xx00 || Float output A            |
|          |    || xx01 || Forward on output A       |
|          |    || xx10 || Backward on output A      |
|          |    || xx11 || Brake then float output A |
+----------+----+-------+----------------------------+
