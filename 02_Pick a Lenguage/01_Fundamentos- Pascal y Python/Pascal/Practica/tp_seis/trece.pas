
Program trece;

Var i, Resultado: integer;

Var car: Integer;


Function prueba (car: Integer): Integer;
Begin
  prueba := 0;
  For i := 0 To 9 Do
    Begin
      If car = i Then
        Begin
          prueba := 1;
        End
    End;
End;
Begin
  WriteLn('Ingrese un caracter');
  ReadLn(car);
  Resultado := prueba(car);
  If Resultado = 1 Then
    Begin
      WriteLn('El caracter se encuentra entre 0 y 9');
    End
  Else
    Begin
      WriteLn('El caracter no se encuentra entre 0 y 9');
    End;
End.
