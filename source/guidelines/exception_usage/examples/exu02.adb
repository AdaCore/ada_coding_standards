procedure Exu02 (X : Integer) is
   Handled_Exception   : exception;
   Unhandled_Exception : exception;

   procedure Noncompliant (Param : Integer) is
   begin
      if Param = 1_234
      then
         raise Unhandled_Exception;
      end if;
   end Noncompliant;

   procedure Compliant (Param : Integer) is
   begin
      if Param = 1_234
      then
         raise Handled_Exception;
      end if;
   end Compliant;

begin
   Noncompliant (X);
   Compliant (X);
exception
   when Handled_Exception =>
      null;
end Exu02;
