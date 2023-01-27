import hashlib

def Hashing(in_str, in_size=64, return_type='digest'): # 해쉬값을 구하는 함수
    assert 1 <= in_size and in_size <= 64 # 해당 조건이 참인 경우에만 실행
    blake  = hashlib.blake2b(in_str.encode('utf-8'), digest_size=in_size) # 해쉬값 변환
    if return_type == 'number': return int(blake.hexdigest(), base=16)
    return blake.digest()

message = 'mew'
print(Hashing(in_str=message, in_size=64, return_type='number')) #blake2는 64bit에 최적화되어있으므로, in_size에 64사용