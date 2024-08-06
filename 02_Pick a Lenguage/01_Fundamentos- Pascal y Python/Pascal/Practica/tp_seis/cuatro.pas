
Program cuatro;

Var i,x: integer;

Var arr: array [] Of integer;

Var maximo: Integer;


Begin
  randomize;
  WriteLn('Ingrese la dimension del arreglo que quiere crear');
  ReadLn(maximo);
  SetLength(arr, maximo);
  For i := 1 To maximo Do
    Begin
      arr[i] := random(50)+1;
      WriteLn('Posicion del arreglo: ', i  );
      WriteLn('Valor del arreglo en esta posicion: ' , arr[i]);
    End;
End.
