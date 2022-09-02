#include <stdio.h>

int main(){
	int i, j, k, N, M;
	scanf("%d %d", &N, &M);
	int a[N], sum[N];
	for(k=1; k<N+1; k++){
		scanf("%d", &a[k]);
		sum[k] = sum[k-1] + a[k];
	}
	
	while(M--){
		scanf("%d %d", &i, &j);
		printf("%d\n", sum[j]-sum[i-1]);
	}
	return 0;
}
