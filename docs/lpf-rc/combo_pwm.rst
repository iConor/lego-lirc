Combo PWM Mode
==============

Binary Representation
---------------------

+----------------------------+---------------+---------------+
| Nibble 1                   | Nibble 2      | Nibble 3      |
+---------+--------+---------+---------------+---------------+
| Address | Escape | Channel | Output B      | Output A      |
+---------+--------+-----+---+---+---+---+---+---+---+---+---+
|       0 |      1 |   C | C | B | B | B | B | A | A | A | A |
+---------+--------+-----+---+---+---+---+---+---+---+---+---+

Field Descriptions
------------------

Nibble 2
~~~~~~~~

+----------+------+-------+-----------------------+
| Output B | BBBB || 0000 || Float                |
|          |      || 0001 || PWM forward, step 1  |
|          |      || 0010 || PWM forward, step 2  |
|          |      || 0011 || PWM forward, step 3  |
|          |      || 0100 || PWM forward, step 4  |
|          |      || 0101 || PWM forward, step 5  |
|          |      || 0110 || PWM forward, step 6  |
|          |      || 0111 || PWM forward, step 7  |
|          |      || 1000 || Brake then float     |
|          |      || 1001 || PWM backward, step 7 |
|          |      || 1010 || PWM backward, step 6 |
|          |      || 1011 || PWM backward, step 5 |
|          |      || 1100 || PWM backward, step 4 |
|          |      || 1101 || PWM backward, step 3 |
|          |      || 1110 || PWM backward, step 2 |
|          |      || 1111 || PWM backward, step 1 |
+----------+------+-------+-----------------------+

Nibble 3
~~~~~~~~

+----------+------+-------+-----------------------+
| Output A | AAAA || 0000 || Float                |
|          |      || 0001 || PWM forward, step 1  |
|          |      || 0010 || PWM forward, step 2  |
|          |      || 0011 || PWM forward, step 3  |
|          |      || 0100 || PWM forward, step 4  |
|          |      || 0101 || PWM forward, step 5  |
|          |      || 0110 || PWM forward, step 6  |
|          |      || 0111 || PWM forward, step 7  |
|          |      || 1000 || Brake then float     |
|          |      || 1001 || PWM backward, step 7 |
|          |      || 1010 || PWM backward, step 6 |
|          |      || 1011 || PWM backward, step 5 |
|          |      || 1100 || PWM backward, step 4 |
|          |      || 1101 || PWM backward, step 3 |
|          |      || 1110 || PWM backward, step 2 |
|          |      || 1111 || PWM backward, step 1 |
+----------+------+-------+-----------------------+
