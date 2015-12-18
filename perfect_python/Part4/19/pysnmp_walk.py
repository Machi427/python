import pprint
from pysnmp.entity.rfc3413.oneliner import cmdgen


# コマンド生成器を作る
cmd_generator = cmdgen.CommandGenerator()

# 接続情報を設定する
community_data = cmdgen.CommunityData('agent', 'public', 0)

# 接続先
target = cmdgen.UdpTransportTarget(('localhost', 161))

# 取得する OID (Object ID)
oid = (1,3,6,1,2,1,1)

# SNMPNEXT でデータを取得する
result = cmd_generator.nextCmd(community_data, target, oid)
error_indication, error_status, error_index, var_binds = result

# OID で指定した情報が取得できる
pprint.pprint(var_binds)

