Extended Mode
=============

Binary Representation
---------------------

+---------------------------+---------------------+---------------+
| Nibble 1                  | Nibble 2            | Nibble 3      |
+--------+--------+---------+---------+-----------+---------------+
| Toggle | Escape | Channel | Address | Mode      | Function      |
+--------+--------+----+----+---------+---+---+---+---+---+---+---+
|      0 |      0 |  C |  C |       0 | 0 | 0 | 0 | F | F | F | F |
+--------+--------+----+----+---------+---+---+---+---+---+---+---+

Field Descriptions
------------------

Nibble 3
~~~~~~~~

+----------+------+-------+-----------------------------------+
| Function | FFFF || 0000 || Brake then float output A        |
|          |      || 0001 || Increment speed on output A      |
|          |      || 0010 || Decrement speed on output A      |
|          |      || 0011 || Not used                         |
|          |      || 0100 || Toggle forward/float on output B |
|          |      || 0101 || Not used                         |
|          |      || 0110 || Toggle Address bit               |
|          |      || 0111 || Align toggle bit (get in sync)   |
|          |      || 1000 || Reserved                         |
+----------+------+-------+-----------------------------------+
