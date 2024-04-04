#include <bits/stdc++.h>
using namespace std;

char num_chr(int n, int k) {
	char buf[20];
	sprintf(buf, "%lld", n);
	return buf[k];
}

int main() {
	int n;
	scanf("%d", &n);
	int digit = 0, sum = 0, psum = 0, s = 9;
	while (sum < n) {
		digit++;
		psum = sum;
		sum += s * digit;
		s *= 10;
	}
	int from = 1;
	for (int i = 0; i < digit - 1; ++i) from *= 10;
	int idx = n - psum - 1;
	printf("%c", num_chr(from + (idx / digit), idx % digit));
	return 0;
}