with Ada.Text_IO; use Ada.Text_IO;
procedure Exu03 (X : in out Integer) is

   procedure Local (Param : in out Integer) is
      Subprogram_Exception : exception;
   begin
      Param := Param * Param;
   exception
      when others =>
         raise Subprogram_Exception;
   end Local;

begin
   Noncompliant :
   begin
      Local (X);
   exception
      when others =>
         raise;
   end Noncompliant;

   Compliant :
   begin
      Local (X);
   exception
      when others =>
         raise Data_Error;
   end Compliant;

end Exu03;
