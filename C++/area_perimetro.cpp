/* Area y Perimetro */

/*
Crea un programa que calcule el area y el perimetro 
de un rectangulo tras ingresar la base y la altura
por el usuario 
*/

#include <iostream>
using namespace std;
int main(){

    float a,b,area,perimetro;
    cout << "Calculo del area y perimetro de un rectangulo" <<endl;
    cout << "Ingrese la base: "; cin >> a;
    cout << "Ingrese la altura: "; cin >> b;

    area = a*b;
    perimetro = 2*(a+b);
    
    cout << "El area del rectangulo es: "<< area <<endl;
    cout << "El perimetro del rectangulo es: "<< perimetro <<endl;
    return 0;
}