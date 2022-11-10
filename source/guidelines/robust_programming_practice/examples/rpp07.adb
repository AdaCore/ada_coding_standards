procedure Rpp07 (X : in out Integer) is
   A, B : Integer;

   function Non_Compliant
     (Value : in out Integer)
      return Integer is
   begin
      if Value < Integer'last
      then
         Value := Value + 1;
      end if;
      return Value;
   end Non_Compliant;

   function Compliant
     (Value : Integer)
      return Integer is
   begin
      return Value + 1;
   end Compliant;

begin
   A := X;
   B := Non_Compliant (A);
   X := Compliant (B);
end Rpp07;
