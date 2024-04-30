/* Meses */

/*
Crea un prograa para determinar que mes 
es segun la inicial de dicho mes introducida 
por el usuario
*/

#include <iostream>

using namespace std;

int main (){

    char mes=' ';
    cout<<"Ingresa una de estas letras en mmayuscula "<<endl;
    cout<<"E, F, M, A, J: ";    
    cin>>mes;
    switch (mes){
    case 'E':
        cout<<"El mes E es Enero"<<endl;
        break;
    case 'F':
        cout<<"El mes F es Febrero"<<endl;
        break;
    case 'M':
        cout<<"El mes M es Marzo"<<endl;
        break;
    case 'A':
        cout<<"El mes A es Abril"<<endl;
        break;
    case 'J':
        cout<<"El mes J es Junio"<<endl;
        break;
    default:
        cout<<"No ingresaste Caracter valido";
        break;
    }

    return 0;
}