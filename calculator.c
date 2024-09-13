#include <stdio.h>
#include<math.h>

//------{{Function-Declare}}------

struct Input input();
float basicCalc(struct Input values);
void results();

//----structureDefine
struct Input{
  float Inp1;
  char Oprt;
  float Inp2;
  float Ans;
};

//----{{MainFunction}}---
int main(){
  printf("\n\n\n------------------------------------------------------Simple Calculator (Version:Alpha)--------------------------------------------------\n\n\n");

//--Call_resultFunction{MainFunction}
  results();
};

//______{{Function-Definition}}______


//----userInputFunction
struct Input input(){
  struct Input values;
  printf("Enter test Num-1: ");
  scanf("%f", &values.Inp1);
  printf("Enter Operator(+,-,x,/): ");
  scanf(" %c", &values.Oprt);
  printf("Enter Num-2: ");
  scanf("%f", &values.Inp2);
  return values;
};

//----calculationFunction
float basicCalc(struct Input values){
  switch (values.Oprt){
    case '+':
      values.Ans = values.Inp1 + values.Inp2;
      break;
    case '-':
      values.Ans = values.Inp1 - values.Inp2;
      break;
    case 'x':
      values.Ans = values.Inp1 * values.Inp2;
      break;
    case '/':
      values.Ans = values.Inp1 / values.Inp2;
      break;
    default:
      printf("Invalid Operator!!\n");
      break;
  };
return values.Ans;
};


//----rersultFunction
void results(){  
  struct Input values = input();
  float results = basicCalc(values);
  printf("Ans: %.3f %c %.3f = %.3f \n",values.Inp1, values.Oprt, values.Inp2, results);
};
//loopFunction



