import sys
input = sys.stdin.readline
 
n, d = map(int, input().split())
t = list(map(int, input().split()))
 
total_song_time = sum(t)
min_required_time = total_song_time + 10 * (n - 1)
 
if min_required_time > d:
    print(-1)
else:
    jokes = (d - total_song_time) // 5
    print(jokes)