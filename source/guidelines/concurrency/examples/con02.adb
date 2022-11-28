pragma Profile (Jorvik);
with Ada.Real_Time; use Ada.Real_Time;
with Ada.Text_IO;   use Ada.Text_IO;
package body Con02 is

   package Noncompliant is
      task Task_T is
         entry Entry_Point;
      end Task_T;
   end Noncompliant;

   package body Noncompliant is
      task body Task_T is
      begin
         accept Entry_Point do
            Put_Line ("Hello World");
         end Entry_Point;
         loop
            delay 1.0;
            Put_Line ("Ping");
         end loop;
      end Task_T;
   end Noncompliant;

   package Compliant is
      task Task_T is
      end Task_T;
   end Compliant;

   package body Compliant is
      task body Task_T is
      begin
         delay 1.0;
         loop
            delay 1.0;
            Put_Line ("Ping");
         end loop;
      end Task_T;
   end Compliant;

   procedure Example is
   begin
      null;
   end Example;

end Con02;
