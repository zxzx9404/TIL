# 중첩딕셔너리 사용
air_info = {
    'A': {
        'name': 'A',
        'capital': '수도입니다.',
        'air_status': {'O2' : 3, 'CO2' : '2'}

    },
    'B': {
        'name': 'B',
        'capital': '수도가 아닙니다.',
        'air_status': {'O2' : 5, 'CO2' : '3'}
    }
}

print(f'{air_info["A"]["name"]} 도시 : 도시 이름은 {air_info["A"]["name"]}이며, {air_info["A"]["capital"]} 산소 농도는 {air_info["A"]["air_status"]["O2"]}이며, 이산화탄소 농도는 {air_info["A"]["air_status"]["CO2"]}입니다.')
print(f'{air_info["B"]["name"]} 도시 : 도시 이름은 {air_info["B"]["name"]}이며, {air_info["B"]["capital"]} 산소 농도는 {air_info["B"]["air_status"]["O2"]}이며, 이산화탄소 농도는 {air_info["B"]["air_status"]["CO2"]}입니다.')


O2_info = [air_info["A"]["air_status"]["O2"], air_info["B"]["air_status"]["O2"]]
print(O2_info)