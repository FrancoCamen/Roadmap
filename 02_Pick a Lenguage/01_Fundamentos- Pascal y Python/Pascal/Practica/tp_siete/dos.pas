
Program dos;

Var cant, condi, num_ing, prod, float: Integer;

Var arr: array  Of integer;

Begin
  cant := 1;
  condi := 0;
  num_ing := 0;
  Repeat
    num_ing := 0;
    WriteLn('Ingrese el valor a ser agregado al vector de enteros');
    Read(num_ing);
    If num_ing <> 0 Then
      Begin
        SetLength(arr, cant);
        arr[cant-1] := num_ing;
        cant := cant +1;
      End
    Else
      Begin
        condi := 1;
      End;
  Until condi = 1;
  prod := 1;
  Repeat
    cant := cant-1;
    float := arr[cant-1];
    WriteLn(float);
    prod := (prod) * (float);
  Until cant = 1;
  WriteLn('El producto de los valores del vector es: ',prod);


End.
