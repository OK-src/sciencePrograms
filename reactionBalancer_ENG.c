#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main(){
	char stato = 'n';
	int contatore1 = 1;
	int contatore2 = 0;
	int numeroElementi = 1;
	char nomiMolecoleSinistra[30][30];
	int molecoleSinistra[30][20];
	char nomiMolecoleDestra[30][30];
	int molecoleDestra[30][20];
	char elementi[30][2];
	int numeroMolecoleSinistra;
	int numeroMolecoleDestra;
	int coefficientiSinistra[30];
	int coefficientiDestra[30];
	int massimoCoefficiente;
	int molecoleVirtualiSinistra[30][20];
	int molecoleVirtualiDestra[30][20];
	int totSinistra;
	int totDestra;
	long int tentativi = 1;
	
	while(stato != 'S'){
		printf("What element is present in this equation? ");
		scanf("%s", &elementi[numeroElementi]);
		printf("as this the last element? (Y/n) ");
		scanf("%s", &stato);
		numeroElementi++;
	}
	printf("In total, here are the elements that you selected: ");
	while(contatore1 < numeroElementi){
		printf("%s ", &elementi[contatore1]);
		contatore1++;
	}
	
	stato = 'Y';
	contatore1 = 1;
	printf("\nNow you have to insert the molecules present on the left hand side of the equals sign.\n");
	while(stato != 'n'){
		printf("What is the name of this molecule? ");
		scanf("%s", &nomiMolecoleSinistra[contatore1]);
		contatore2 = 1;
		while(contatore2 < numeroElementi){
			printf("How many atoms of %s does this molecule have? ", &elementi[contatore2]);
			scanf("%d", &molecoleSinistra[contatore1][contatore2]);
			contatore2++;
		}
		contatore1++;
		printf("Is there another molecule to consider? (Y/n) ");
		scanf("%s", &stato);
	}
	numeroMolecoleSinistra = contatore1;
	
	stato = 'Y';
	contatore1 = 1;
	printf("Now you have to insert the molecules present on the right hand side of the equals sign.\n");
	while(stato != 'n'){
		printf("What is the name of this molecule? ");
		scanf("%s", &nomiMolecoleDestra[contatore1]);
		contatore2 = 1;
		while(contatore2 < numeroElementi){
			printf("Quanti atomi di %s ha questa molecola? ", &elementi[contatore2]);
			scanf("%d", &molecoleDestra[contatore1][contatore2]);
			contatore2++;
		}
		contatore1++;
		printf("Is there another molecule to consider? (Y/n) ");
		scanf("%s", &stato);
	}
	numeroMolecoleDestra = contatore1;
	
	printf("What is the maximum coefficient? ");
	scanf("%d", &massimoCoefficiente);
	massimoCoefficiente--;
	
	stato = 'f';
	while(stato == 'f'){
		contatore1 = 1;
		while(contatore1 < numeroMolecoleSinistra){
			coefficientiSinistra[contatore1] = (rand() % massimoCoefficiente) + 1;
			contatore1++;
		}
		
		contatore1 = 1;
		while(contatore1 < numeroMolecoleDestra){
			coefficientiDestra[contatore1] = (rand() % massimoCoefficiente) + 1;
			contatore1++;
		}
		
		contatore1 = 1;
		while(contatore1 <= numeroMolecoleSinistra){
			contatore2 = 1;
			while(contatore2 < numeroElementi){
				molecoleVirtualiSinistra[contatore1][contatore2] = molecoleSinistra[contatore1][contatore2] * coefficientiSinistra[contatore1];
				contatore2++;
			}
			contatore1++;
		}
		
		contatore1 = 1;
		while(contatore1 <= numeroMolecoleDestra){
			contatore2 = 1;
			while(contatore2 < numeroElementi){
				molecoleVirtualiDestra[contatore1][contatore2] = molecoleDestra[contatore1][contatore2] * coefficientiDestra[contatore1];
				contatore2++;
			}
			contatore1++;
		}
		
		stato = 's';
		contatore1 = 1;
		while(contatore1 < numeroElementi){
			totSinistra = 0;
			contatore2 = 1;
			while(contatore2 <= numeroMolecoleDestra){
				totSinistra += molecoleVirtualiSinistra[contatore2][contatore1];
				contatore2++;
			}
			
			totDestra = 0;
			contatore2 = 1;
			while(contatore2 <= numeroMolecoleDestra){
				totDestra += molecoleVirtualiDestra[contatore2][contatore1];
				contatore2++;
			}
			
			if(totSinistra != totDestra){
				stato = 'f';
			}
			contatore1++;
		}
		
		contatore1 = 1;
		while(contatore1 < numeroMolecoleSinistra){
			printf("%d%s ", coefficientiSinistra[contatore1], &nomiMolecoleSinistra[contatore1]);
			contatore1++;
		}
		printf("= ");
		contatore1 = 1;
		while(contatore1 < numeroMolecoleDestra){
			printf("%d%s ", coefficientiDestra[contatore1], &nomiMolecoleDestra[contatore1]);
			contatore1++;
		}
		
		if(stato == 'f'){
			printf("Attempt %d failed!\n", tentativi);
		}
		tentativi++;
	}
}
