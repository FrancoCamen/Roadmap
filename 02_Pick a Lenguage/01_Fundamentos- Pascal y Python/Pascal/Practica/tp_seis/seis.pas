
Program seis;

Const 
  maximo = 50;

Type 
  vector = array [1..maximo] Of integer;

Var 
  opcion: String;
  salida: boolean;
  vec: Vector;

Procedure carga(Var vec:vector);

Var i: Integer;
Begin
  randomize;
  writeln('Vector sin ordenar');
  For i :=1 To maximo Do
    Begin
      vec[i] := random(9)+1;
      write(vec[i],' ');
    End;
  ReadLn;
End;

Procedure insercion;

Var i,j,aux: Integer;

Var vec: vector;
Begin
  carga(vec);
  For i:= 2 To maximo Do
    Begin
      j := i-1;
      aux := vec[i];
      While (j>0) And (vec[j]> aux) Do
        Begin
          vec[j+1] := vec[j];
          j := j-1;
        End;
      vec[j +1] := aux;
    End;
  WriteLn;
  WriteLn('El vector ordenado es');
  For j := 1 To maximo Do
    write(vec[j], ' ');
  readln;
End;
Begin
  carga(vec);
  insercion();
End.
