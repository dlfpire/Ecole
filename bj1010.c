#include <stdio.h>

int main()
{
	int N, M, T; //N : 서쪽사이트 M: 동쪽사이트 T: 테스트 개수 
	scanf("%d", &T);
	while(T--){ //테스트 개수만큼 반복 
		scanf("%d %d", &N, &M);
		printf("%.lf\n", result(M, N));
	}
	return 0;
}

double fac(int n) { 
	if(n==0) return 1;
	return n*fac(n-1); //재귀함수 
}

double result(int n, int m) { 
	return fac(n) / (fac(n-m)*fac(m));
}


