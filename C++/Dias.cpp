/* Dia de la semana */

/*
Crea un programa que por medio de una lista de 
numeros determinada pida uno de esos numeros
al usuario y segun el numero le diga que dia
hace referencia a ese numero 
*/

#include <iostream>

using namespace std;

int main (){

    int dia;

    cout<<"Ingresa un numero del 1 al 7: ";
    cin>>dia;
    switch (dia)
    {
    case 1:
        cout<<"El dia numero 1 es Domingo"<<endl;
        break;
    case 2:
        cout<<"El dia numero 2 es Lunes"<<endl;
        break;
    case 3:
        cout<<"El dia numero 3 es Martes"<<endl;
        break;
    case 4:
        cout<<"El dia numero 4 es Miercoles"<<endl;
        break;
    case 5:
        cout<<"El dia numero 5 es Jueves"<<endl;
        break;
    case 6:
        cout<<"El dia numero 6 es Viernes"<<endl;
        break;
    case 7:
        cout<<"El dia numero 7 es Sabado"<<endl;
        break;

    default:
        cout<<"No ingresaste un numero entre 1 y 7";
        break;
    }

    return 0;
}