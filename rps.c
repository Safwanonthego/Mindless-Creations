#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int score(char P);

int main(){

  char P;
  //Player inputs
  printf("Enter move(r/p/s)");
  scanf("%c", &P);
  


  int Results = score(P);
  printf("results: %d\n",Results);
  //Print the result
  if (Results == 0)
    printf("Draw!");
  else if (Results == 1)
      printf("You Win!");
  else
      printf("You Lost!");
};




int score(char P){
  
  int R;
  char C,r,s,p;
  //Cpu chooses r/p/s
  srand(time(NULL));
  R = rand() % 3;
  

  if (R == 0)
    C = 'r';
  else if (R == 1)
    C = 'p';
  else
    C = 's';

  
  //R>S....P>R....S>P
  if (P == C)
    return 0;
  else if (P == 'r' && C == 's')
    return 1;
  else if (P == 'p' && C == 'r')
    return 1;
  else if (P == 's' && C == 'p')
    return 1;
  else
    return -1;
};

