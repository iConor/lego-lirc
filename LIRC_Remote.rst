#
# contributed by
#
# brand:
# model no. of remote control:
# devices being controlled by this remote:
#

begin remote

  name  LEGO_<insert_mode>
  bits           16
  flags   SPACE_ENC
  eps            20
  aeps          105

#  toggle_bit_mask <insert_hex>

#             pulse  space
  header        158  1026
  one           158   553
  zero          158   263
  foot          158  1026

      begin codes

        <insert_codes>

      end codes

end remote
