#include "Generate.h"







/*
 *  Returns the payload's value for the "Longitudinal Redundancy Check".
 */
int lrc(int[] payload)
{
  return payload[0] ^ payload[1] ^ payload[2];
}
