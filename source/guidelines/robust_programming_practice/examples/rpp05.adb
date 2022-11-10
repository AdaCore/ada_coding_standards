procedure Rpp05 (Value : in out Integer) is

   procedure Non_Compliant (X : in out Integer) is
   begin
      X := X * X;
   exception
      when others =>
         X := -1;
   end Non_Compliant;

   procedure Compliant (X : in out Integer) is
   begin
      X := X * X;
   exception
      when Constraint_Error =>
         X := -1;
   end Compliant;

begin
   Non_Compliant (Value);
   Compliant (Value);
end Rpp05;
