package Oop05 is

   type Root_T is tagged null record;
   procedure Primitive (X : in out Root_T) is null;

   package Non_Compliant is
      type Child_T is new Root_T with null record;
      procedure Primitive (X : in out Child_T) is null;
   end Non_Compliant;

   package Compliant is
      type Child_T is new Root_T with null record;
      overriding procedure Primitive (X : in out Child_T) is null;
   end Compliant;

end Oop05;
