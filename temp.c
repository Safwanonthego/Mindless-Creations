#include <stdio.h>
#include <ctype.h>
#include <math.h>



// ------[[Declaration of the functions]]------

struct Input usrInput();
float convFormula(struct Input valus);
void results();


// ------Define the structure------

struct Input{
  float value;
  char unit1;
  char unit2;
  float conversion;
};



// ------[[Main Function]]------

int main()
{
  printf("\n\n------------------Wellcome to Temperature Conversion------------------\n\n\n");
  results();
  return 0;
};



// ------[[Definition of the functions]]------


// ------Getting input------

struct Input usrInput(){
  struct Input values;
  printf("Enter the Temperature \nExample-[<value><unit(C/K/F)>]: ");
  scanf("%f%c", &values.value, &values.unit1);
  values.unit1 = toupper(values.unit1);
  while (getchar() != '\n'); // clear the input buffer
  printf("Enter Conversion Unit: ");
  scanf("%c", &values.unit2);
  values.unit2 = toupper(values.unit2);
  return values;
};


// ------Hall of Calculations & Formula------

float convFormula(struct Input values){
  switch (values.unit1){
    case 'C':
      switch (values.unit2){
        case 'K':
          values.conversion = values.value + 273.15;
          break;
        case 'F':
          values.conversion = (values.value*(9.0/5.0))+32;
          break;
      }
      break;

    case 'K':
      switch (values.unit2){
        case 'C':
          values.conversion = values.value - 273.15;
          break;
        case 'F':
          values.conversion = ((values.value - 273.15)*(9.0/5.0))+32;
          break;
      }
      break;

    case 'F':
      switch (values.unit2){
        case 'K':
          values.conversion = ((values.value - 32)*(5.0/9.0)) + 273.15;
          break;
        case 'C':
          values.conversion = (values.value - 32)*(5.0/9.0);
          break;
      }
      break;
    default:
      printf("Invalid conversion unit");
      break;
  };
  return values.conversion;
};


//------[[Results]]------

void results(){
  struct Input values = usrInput();
  float results = convFormula(values);
  printf("\nAns is: %.2f", results);
};


