from api import storesByAddr, storesByGeo

address = '경기도 성남시 분당구 수내동'
save_path = '../storesByAddr_output.csv'
storesByAddr(address, save_path)


lat = 37.411975
lng = 127.1465933
m = 1000
save_path = '../storesByGeo_output.csv'
storesByGeo(lat, lng, m, save_path)
