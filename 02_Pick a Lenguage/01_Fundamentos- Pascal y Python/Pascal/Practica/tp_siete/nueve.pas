
Program nueve;

Var arr: array Of Integer;

Var suma_par, suma_impar, media_par, media_impar,cont_par, cont_impar: Integer;

Var tam, i: Integer;
Begin
  randomize;
  tam := random(30)+1;
  SetLength(arr, tam);
  For i := 0 To tam Do
    Begin
      arr[i] := random(10)+1;
    End;
  suma_par := 0;
  suma_impar := 0;
  cont_par := 0;
  cont_impar := 0;
  For i := 0 To tam Do
    Begin
      If (i Mod 2 = 0) Then
        Begin
          suma_par := suma_par + arr[i];
          cont_par := cont_par +1;
        End
      Else
        Begin
          suma_impar := suma_impar + arr[i];
          cont_impar := cont_impar +1;

        End;
    End;
  WriteLn('Suma en la posicion par: ', suma_par);
  WriteLn('Suma en la posicion impar: ',suma_impar);
  WriteLn('Posiciones pares: ',cont_par);
  WriteLn('Posiciones impares: ',cont_impar);

  media_par := Trunc(suma_par / cont_par);
  media_impar := Trunc(suma_impar / cont_impar);
  WriteLn('La media de los valores en posiciones pares es: ', media_par);
  WriteLn('La media de los valores en posiciones impares es: ', media_impar);


End.
