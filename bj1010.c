#include <stdio.h>

int main()
{
	int N, M, T; //N : ���ʻ���Ʈ M: ���ʻ���Ʈ T: �׽�Ʈ ���� 
	scanf("%d", &T);
	while(T--){ //�׽�Ʈ ������ŭ �ݺ� 
		scanf("%d %d", &N, &M);
		printf("%.lf\n", result(M, N));
	}
	return 0;
}

double fac(int n) { 
	if(n==0) return 1;
	return n*fac(n-1); //����Լ� 
}

double result(int n, int m) { 
	return fac(n) / (fac(n-m)*fac(m));
}


