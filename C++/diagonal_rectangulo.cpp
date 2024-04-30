/* Diagonal de un rectangulo */

/*
Crea un programa que calcule la diagonal de un
rectangulo con la base y la altura ingresada
por el usuario
*/
#include <cmath>
#include <iostream>
using namespace std;
int main(){
    float a,b,d;
    cout << "Diagonal de un rectangulo"<< endl;
    cout << "Ingrese la base: "; cin >> a;
    cout << "Ingrese la altura: ";cin >> b;

    d = sqrt(a*a + b*b);
    cout << "La diagonal del rectangulo es: " <<d<<endl;

    return 0;
}