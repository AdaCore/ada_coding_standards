procedure Exu01 (X : in out Integer) is
   Local_Exception : exception;

   procedure Noncompliant (X : in out Integer) is
   begin
      if X < Integer'last / 2
      then
         X := X * 2;
      else
         raise Constraint_Error;
      end if;
   end Noncompliant;

   procedure Compliant (X : in out Integer) is
   begin
      if X < Integer'last / 2
      then
         X := X * 2;
      else
         raise Local_Exception;
      end if;
   end Compliant;

begin

   null;

end Exu01;
