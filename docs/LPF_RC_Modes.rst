Mode-Specific Bit Fields & Flags
================================

Extended Mode
-------------

**Relevant Bit Fields:**

+---------------------+---------------+
| Nibble 2            | Nibble 3      |
+---------+-----------+---------------+
| Address | Mode      | Data          |
+---------+---+---+---+---+---+---+---+
|       a | 0 | 0 | 0 | F | F | F | F |
+---------+---+---+---+---+---+---+---+

**Relevant Flags:**

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

Combo Direct Mode
-----------------

**Relevant Bit Fields:**

+---------------------+---------------+
| Nibble 2            | Nibble 3      |
+---------+-----------+---------------+
| Address | Mode      | Data          |
+---------+---+---+---+---+---+---+---+
|       a | 0 | 0 | 1 | B | B | A | A |
+---------+---+---+---+---+---+---+---+

**Relevant Flags:**

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

Single Output Mode
------------------

**Relevant Bit Fields:**

+---------------------+---------------+
| Nibble 2            | Nibble 3      |
+---------+-----------+---------------+
| Address | Mode      | Data          |
+---------+---+---+---+---+---+---+---+
|       a | 1 | M | O | D | D | D | D |
+---------+---+---+---+---+---+---+---+

**Relevant Flags:**

+--------+---+----+--------------------------------+
| Mode   | M || 0 || PWM                           |
|        |   || 1 || Clear/Set/Toggle/Inc/Dec      |
+--------+---+----+--------------------------------+
| Output | O || 0 || Output A                      |
|        |   || 1 || Output B                      |
+--------+---+----+--------------------------------+
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

Combo PWM Mode
--------------

**Relevant Bit Fields:**

+----------------------------+---------------+---------------+
| Nibble 1                   | Nibble 2      | Nibble 3      |
+---------+--------+---------+---------------+---------------+
| Address | Escape | Channel | Output B      | Output A      |
+---------+--------+-----+---+---+---+---+---+---+---+---+---+
|       a |      1 |   C | C | B | B | B | B | A | A | A | A |
+---------+--------+-----+---+---+---+---+---+---+---+---+---+

**Relevant Flags:**

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
