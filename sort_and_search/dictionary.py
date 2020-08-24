# @Author YoungMinKim
# Data structure
# Python dictionary를 통한 구현
d={} 
d['data'] = '자료'
d['structure'] = '구조'
d['sequential search'] = '선형 탐색'
d['binary search'] = '이진 탐색'
d['game'] = '게임'

print('나의 단어장: ')
print(d)

if d.get('game'): print('탐색: game --> ',d['game'])
if d.get('over'): print('탐색: over --> ',d['over'])
if d.get('data'): print('탐색: data --> ',d['data'])

d.pop('game')
print('나의 단어장: ')
print(d)