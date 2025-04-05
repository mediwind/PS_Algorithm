ip = list(input().split(':'))

while len(ip) < 8:
    ip.insert(ip.index(''), '0000')
while len(ip) > 8:
    ip.remove('')

for i in range(8):
    if len(ip[i]) < 4:
        ip[i] = '0' * (4 - len(ip[i])) + ip[i]

print(*ip, sep = ':')