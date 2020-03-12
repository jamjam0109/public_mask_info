from api import storesByAddr, storesByGeo

# 주소 기반
address = '경기도 성남시 분당구 야탑동'
save_path = '../storesByAddr_output/storesByAddr_output.csv'

storesByAddr(address, save_path)


# 위도/경도 기반
lat = 37.411975
lng = 127.1465933
m = 1000
save_path = '../storesByGeo_output.csv'

storesByGeo(lat, lng, m, save_path)
