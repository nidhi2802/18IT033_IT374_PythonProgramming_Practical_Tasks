import sys
import qrcode

id = sys.argv[1]

qrcode_id = qrcode.make(id)

qrcode_id.save('18IT033.png')
