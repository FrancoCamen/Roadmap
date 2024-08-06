
Program ejercicioDos;

Var palabra, letra_ingresada: String;

Var tam_palabra, i, j, intentos, resultado, x, u, letras: Integer;

Var arr: array Of String;

Function prueba (letra_ingresada, palabra: String): Integer;

Begin
  j := 1;
  resultado := 0;
  Repeat
    If palabra[j] = letra_ingresada Then
      Begin
        resultado := j;
        j := 100;
      End;
    j := j +1;
  Until j > Length(palabra);
  If resultado <> 0 Then
    Begin
      prueba := Trunc(resultado);
    End
  Else
    Begin
      prueba := Trunc(0);
    End;
End;

Begin
  WriteLn('Juego del ahorcado');
  WriteLn('Ingrese una palabra');
  ReadLn(palabra);
  tam_palabra := Length(palabra);
  SetLength(arr, tam_palabra-1);
  For u := 0 To tam_palabra-1 Do
    Begin
      arr[u] := ' _ ';
      Write(' _ ');
    End;
  intentos := 1;
  Repeat
    WriteLn(' ');
    WriteLn('Ingrese una Letra');
    WriteLn('Intento numero: ' , intentos);
    ReadLn(letra_ingresada);
    resultado := prueba(letra_ingresada, palabra);

    If resultado = 0 Then
      Begin
        WriteLn('No Hubo Coincidencias');
        intentos := intentos +1;
      End
    Else
      Begin
        WriteLn('La letra ingresada coincide');
        arr[resultado-1] :=  letra_ingresada;
        For u := 0 To tam_palabra Do
          Begin
            Write(arr[u]);
          End;
      End;
    x := 0;
    letras := 0;
    Repeat
      If arr[x] = palabra[x+1] Then
        Begin
          letras := letras+1;
        End;
      x := x+1;
    Until x = tam_palabra;
    If letras = tam_palabra Then
      Begin
        WriteLn(' ');
        WriteLn('Todas las letras coinciden');
        intentos := 10;
      End;
  Until intentos > 3;
End.
