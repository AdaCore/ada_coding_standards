package Oop03 is

   type Shape_T is tagged private;
   procedure Set_Name
     (Shape : Shape_T;
      Name  : String);
   function Get_Name
     (Shape : Shape_T)
      return String;

   type Point_T is new Shape_T with private;
   type Square_T is new Point_T with private;
   type Cube_T is new Square_T with private;

private

   type Shape_T is tagged null record;
   type Point_T is new Shape_T with null record;
   type Square_T is new Point_T with null record;
   type Cube_T is new Square_T with null record;

   procedure Set_Name
     (Shape : Shape_T;
      Name  : String) is null;
   function Get_Name
     (Shape : Shape_T)
      return String is ("");

end Oop03;
