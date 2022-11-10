pragma Profile (Jorvik);
with Ada.Real_Time; use Ada.Real_Time;
with Ada.Text_IO;   use Ada.Text_IO;
package body Con02 is

   task Task_T is
   end Task_T;

   task body Task_T is
      Period     : constant Time_Span := Milliseconds (10);
      Activation : Time               := Clock;
   begin
      loop
         delay until Activation;
         Put_Line ("Hello World");
         Activation := Activation + Period;
      end loop;
   end Task_T;

   procedure Example is
   begin
      null;
   end Example;

end Con02;
