procedure Oop04 is

   package Root is
      type Root_T is tagged null record;
      procedure Primitive_1 (X : in out Root_T) is null;
      procedure Primitive_2 (X : in out Root_T) is null;
   end Root;

   package Child is
      use Root;
      type Child_T is new Root_T with null record;
      procedure Primitive_1 (X : in out Child_T);
      procedure Primitive_2 (X : in out Child_T);
   end Child;

   package body Child is

      procedure Primitive_1 (X : in out Child_T) is
      begin
         Primitive_1 (Root_T (X)); -- constructor style is OK
         Primitive_2 (Root_T (X));
         Primitive_2 (X);
      end Primitive_1;

      procedure Primitive_2 (X : in out Child_T) is null;
   end Child;

begin

   null;

end Oop04;
