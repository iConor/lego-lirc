Single Output Mode
==================

Binary Representation
---------------------

+---------------------------+---------------------+---------------+
| Nibble 1                  | Nibble 2            | Nibble 3      |
+--------+--------+---------+---------+-----------+---------------+
| Toggle | Escape | Channel | Address | Mode      | Data          |
+--------+--------+----+----+---------+---+---+---+---+---+---+---+
|      0 |      0 |  C |  C |       0 | 1 | M | O | D | D | D | D |
+--------+--------+----+----+---------+---+---+---+---+---+---+---+

Field Descriptions
------------------

Nibble 2
~~~~~~~~

+--------+---+----+--------------------------------+
| Mode   | M || 0 || PWM                           |
|        |   || 1 || Clear/Set/Toggle/Inc/Dec      |
+--------+---+----+--------------------------------+
| Output | O || 0 || Output A                      |
|        |   || 1 || Output B                      |
+--------+---+----+--------------------------------+

Nibble 3
~~~~~~~~

+------+------+-------+----------------------------+
| Mode = PWM                                       |
+------+------+-------+----------------------------+
| Data | DDDD || 0000 || Float                     |
|      |      || 0001 || PWM forward, step 1       |
|      |      || 0010 || PWM forward, step 2       |
|      |      || 0011 || PWM forward, step 3       |
|      |      || 0100 || PWM forward, step 4       |
|      |      || 0101 || PWM forward, step 5       |
|      |      || 0110 || PWM forward, step 6       |
|      |      || 0111 || PWM forward, step 7       |
|      |      || 1000 || Brake then float          |
|      |      || 1001 || PWM backward, step 7      |
|      |      || 1010 || PWM backward, step 6      |
|      |      || 1011 || PWM backward, step 5      |
|      |      || 1100 || PWM backward, step 4      |
|      |      || 1101 || PWM backward, step 3      |
|      |      || 1110 || PWM backward, step 2      |
|      |      || 1111 || PWM backward, step 1      |
+------+------+-------+----------------------------+
| Mode = Clear/Set/Toggle/Inc/Dec                  |
+------+------+-------+----------------------------+
| Data | DDDD || 0000 || Toggle Full Forward [#]_  |
|      |      || 0001 || Toggle Direction          |
|      |      || 0010 || Increment Numerical PWM   |
|      |      || 0011 || Decrement Numerical PWM   |
|      |      || 0100 || Increment PWM             |
|      |      || 0101 || Decrement PWM             |
|      |      || 0110 || Full Forward Timeout [t]_ |
|      |      || 0111 || Full Backward Timeout [t]_|
|      |      || 1000 || Toggle Forward/Backward   |
|      |      || 1001 || Clear C1 (High)           |
|      |      || 1010 || Set C1 (Low)              |
|      |      || 1011 || Toggle C1                 |
|      |      || 1100 || Clear C2 (High)           |
|      |      || 1101 || Set C2 (Low)              |
|      |      || 1110 || Toggle C2                 |
|      |      || 1111 || Toggle Full Backward [#]_ |
+------+------+-------+----------------------------+

.. [#] Stop --> Forward, Forward --> Stop, Backward --> Forward
.. [#] Stop --> Backward, Backward --> Stop, Forward --> Backward
.. [t] All other commands have no timeout on lost IR.
