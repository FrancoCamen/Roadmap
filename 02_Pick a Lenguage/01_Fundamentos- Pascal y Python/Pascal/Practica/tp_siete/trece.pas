
Program trece;

Var texto: String;

Var longitud_texto, palaba_larga,contador_palabra: Integer;
Begin
  WriteLn('Ingrese texto finalizandolo en un punto');
  ReadLn(texto);
  i := 1;
  contador_palabra := 0;
  palabra_larga
  Repeat
    If texto[i]<>' ' Then
      Begin
        contador_palabra := contador_palabra + 1;
      End;
  Until texto[i]='.';
End.
