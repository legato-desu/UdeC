/*
Crea un programa que dado los siguientes datos 
de entrada: saldo anterior, tipo de movimiento R (retiro) 
o D (deposito) y monto de transaccion, obtener como dato 
la salida el saldo actual
*/

#include <iostream>

using namespace std;

int main(){
    float santerior,monto_transaccion,sactual;
    char tipo_movimiento;
    cout << "ingrese el saldo anterior: ";
    cin >> santerior;
    cout << " ingrese el tipo de movimiento (D) o (R): ";
    cin >> tipo_movimiento;
    cout << " ingrese el monto de transaccion: ";
    cin >> monto_transaccion;
    if (tipo_movimiento== 'D' || tipo_movimiento == 'd')
    sactual = santerior + monto_transaccion;
    else
    sactual = santerior - monto_transaccion;

    cout << "saldo actual: "<<sactual<<endl;
    return 0;
}