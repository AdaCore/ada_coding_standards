package Swe04 is

   package Noncompliant is
      type Array_T is array (0 .. 31) of Boolean;
      type Record_T is record
         Field1 : Array_T;
         Field2 : Array_T;
      end record;
   end Noncompliant;

   package Compliant is
      type Array_T is array (0 .. 31) of Boolean;
      type Record_T is private;
   private
      type Record_T is record
         Field1 : Array_T;
         Field2 : Array_T;
      end record;
   end Compliant;

end Swe04;
