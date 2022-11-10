function Rpp12
  (Number : Positive)
   return Positive is

   A, B : Positive;

   function Non_Compliant
     (N : Positive)
      return Positive is
   begin
      if N = 1
      then
         return 1;
      else
         return N * Non_Compliant (N - 1);
      end if;
   end Non_Compliant;

   function Compliant
     (N : Positive)
      return Positive is
      Result : Positive := 1;
   begin
      for K in 2 .. N
      loop
         Result := Result * K;  -- could overflow
      end loop;
      return Result;
   end Compliant;

begin

   A := Non_Compliant (Number);
   B := Compliant (Number);
   return A + B;

end Rpp12;
