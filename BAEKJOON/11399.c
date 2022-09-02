#include <stdio.h>
#include <stdlib.h>

int main() {
	int num, i, j, temp, time=0;
	scanf("%d", &num);
	int p[num];
	for(i=0; i<num; i++){
		scanf("%d", &p[i]);
	}
	for(i=0; i<num; i++){
		for(j=i+1; j<num; j++){
			if(p[i]>p[j]) {
				temp = p[i];
				p[i] = p[j];
				p[j] = temp;
			}
		}
	}
	for(i=0; i<num; i++) {
		for(j=0; j<i+1; j++) {
			time+=p[j];
		}
	}
	printf("%d", time);
	return 0;
}
