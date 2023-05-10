#define P1 A2
#define P2 A3
#define P3 A4
#define P4 A5
#define ROJO 13
#define NARANJA 12
#define AMARILLO 11
#define VERDE 10
#define A 9
#define B 8
#define C 7
#define D 6
#define E 5
#define F 4
#define G 3

void setup()
{
for(int i = 13;i > 2; i--){
  pinMode(i, OUTPUT);
}
for(int j = 19;j > 15; j--){
  pinMode(j, INPUT_PULLUP);
}
}

int estadoRojo = 0;
int estadoNaranja = 0;
int estadoAmarillo = 0;
int estadoVerde = 0;
int pulsadorUnoAnt = 1;
int pulsadorDosAnt = 1;
int pulsadorTresAnt = 1;
int pulsadorCuatroAnt = 1;

void loop()
{
	int estado = keypressed();
    switch(estado)
    {
    case 16://P1
    estadoRojo = !estadoRojo;
    break;
    case 17://P2
    estadoNaranja = !estadoNaranja;
    break;
    case 18://P3
    estadoAmarillo = !estadoAmarillo;
    break;
    case 19://P4
    estadoVerde = !estadoVerde;
    break;
    }
  prendeLed(estadoRojo,estadoNaranja,estadoAmarillo,estadoVerde);
  mostrar(hexadecimal(estadoRojo,estadoNaranja,estadoAmarillo,estadoVerde));
}

void prendeLed(int rojo,int naranja, int amarillo, int verde)
{
  digitalWrite(ROJO,rojo);
  digitalWrite(NARANJA,naranja);
  digitalWrite(AMARILLO,amarillo);
  digitalWrite(VERDE,verde);
}

int hexadecimal(int rojo,int naranja, int amarillo, int verde)
{
  return rojo*8+naranja*4+amarillo*2+verde;
}

int keypressed(void)
{ 	
  int ocho = digitalRead(P1); // devuelve 0 si presiono, 1 si no presiono
  int cuatro = digitalRead(P2);
	int dos = digitalRead(P3);
  int uno = digitalRead(P4);
  
  if (ocho== 1)     // si no presione SUBE
    pulsadorUnoAnt =1; //entonces antes tampoco estaba presionada
  if (cuatro)
    pulsadorDosAnt =1;
  if(dos)
    pulsadorTresAnt =1;
  if(uno)
    pulsadorCuatroAnt =1;
  
    
  if(ocho==0 && ocho != pulsadorUnoAnt)
    {
      pulsadorUnoAnt = 0;
    return P1;
    }
    
  if(cuatro==0 && cuatro != pulsadorDosAnt)
    {
      pulsadorDosAnt = 0;
    return P2;
    }
  
  if(dos==0 && dos != pulsadorTresAnt)
    {
      pulsadorTresAnt = 0;
    return P3;
    }
  if(uno==0 && uno != pulsadorCuatroAnt)
    {
      pulsadorCuatroAnt = 0;
    return P4;
    }
 return 0; //o no presione ninguna tecla, o presione una que estaba presionada

}

void mostrar(int digito)
{
  for(int i=3; i<10; i++){
    digitalWrite(i,LOW);
  }
  switch (digito)
  {
	case 0:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, HIGH);
      digitalWrite(F, HIGH);
    break;
    case 1:
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
    break;
    case 2:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(G, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, HIGH);
    break;
    case 3:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(G, HIGH);
    break;
    case 4:
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(G, HIGH);
      digitalWrite(F, HIGH);
    break;
    case 5:
      digitalWrite(A, HIGH);
      digitalWrite(F, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(G, HIGH);
      digitalWrite(D, HIGH);
    break;
    case 6:
      digitalWrite(A, HIGH);
      digitalWrite(F, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, HIGH);
      digitalWrite(G,HIGH);
    break;

    case 7:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
    break;
    case 8:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, HIGH);
      digitalWrite(G,HIGH);
      digitalWrite(F,HIGH);
    break;
    case 9:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(F, HIGH);
      digitalWrite(G,HIGH);
    break;
    case 10:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, HIGH);
      digitalWrite(G,HIGH);
    break;
   	case 11:
      digitalWrite(F, HIGH);
      digitalWrite(G, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, HIGH);
    break;
   	case 12:
      digitalWrite(G, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, HIGH);
    break;
   	case 13:
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, HIGH);
      digitalWrite(G, HIGH);
    break;
    case 14:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(G, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, HIGH);
      digitalWrite(F, HIGH);
    break;
    case 15:
      digitalWrite(G, HIGH);
      digitalWrite(F, HIGH);
      digitalWrite(A, HIGH);
      digitalWrite(E, HIGH);
    break;  
    
  }
}
