substr = ["ch", "he", "ef"]
ans = 0
for _ in range(int(input())) :
	s = input().strip()
	ans += int(any([x in s for x in substr]))
print(ans)