package Con03 is

   Global_Object : Integer with
     Volatile;

   function Get return Integer is (Global_Object);

end Con03;
