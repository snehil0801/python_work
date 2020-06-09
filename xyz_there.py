def xyz_there(str):
    return str.count('.xyz') != str.count('xyz')
print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))