
Program cinco;

Var num, opcion, negativos, positivos, nulos, i: Integer;

Var arr: array [1..10] Of integer;

Begin
  negativos := 0;
  nulos := 0;
  positivos := 0;
  For i := 0 To 9 Do
    Begin
      WriteLn('Ingrese un valor Entero');
      ReadLn(num);
      arr[i] := num;
    End;
  opcion := 0;
  Repeat
    If arr[i] > 0 Then
      Begin
        positivos := 1;
      End
    Else
      Begin
        If arr[i] < 0 Then
          Begin
            negativos := 1;
          End;
        If (arr[i] = 0) Then
          Begin
            nulos := 1;
          End;
      End;
    i := i -1;
  Until i < 0;
  If (negativos = 0) And (nulos = 0) Then
    Begin
      WriteLn('El vector tiene todas sus componentes positivas');
    End
  Else
    Begin
      If negativos <> 0 Then
        Begin
          WriteLn('El vector tiene componentes negativas');
        End;
      If nulos <> 0  Then
        Begin
          WriteLn('El vector tiene algun componente cero');
        End;
    End;
End.
