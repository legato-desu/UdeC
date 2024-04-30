/**
Crea un programa para determinar si
una persona es mayor de edad
*/
#include <iostream>

using namespace std;

int main(){

    int edad;
    cout << "Ingrese su edad: ";
    cin >>edad;
    if (edad >= 18)
    cout << "Mayor de edad"<<endl;
    else
    cout << "Menor de edad"<<endl;
    return 0;
}

