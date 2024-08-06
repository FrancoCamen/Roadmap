
Program cinco;

Var arr: array [1..10] Of Integer;

Var i, tam, num, j,x: integer;
Begin
  randomize;
  For i := 1 To 10 Do
    Begin
      arr[i] := random(10)+1;
    End;

  WriteLn('Ingrese numero a buscar dentro del arreglo');
  ReadLn(num);

  j := 1;
  tam := Length(arr);
  Repeat
    If arr[j] = num Then
      Begin
        WriteLn('El numero se encontro en la posicion: ', j);
        x := 1;
      End;
    j := j +1;
  Until j > tam;
  If x = 0 Then
    Begin
      WriteLn('No se encontro el numero dentro del arreglo');
    End;
End.
