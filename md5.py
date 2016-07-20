import hashlib
mystring = raw_input('Enter Your Password: ')

hash_md5 = hashlib.md5(mystring.encode())
hash_sha1 = hashlib.sha1(mystring.encode())
hash_sha256 = hashlib.sha256(mystring.encode())
hash_sha512 = hashlib.sha512(mystring.encode())

print('MD5: ' + hash_md5.hexdigest())
print('sha1: ' + hash_sha1.hexdigest())
print('sha256: ' + hash_sha256.hexdigest())
print('sha512: ' + hash_sha512.hexdigest())

