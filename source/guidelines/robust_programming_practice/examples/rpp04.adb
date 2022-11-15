procedure Rpp04
  (Register  :     Character;
   Registera : out Integer;
   Registerb : out Integer;
   Registerc : out Integer) is

   procedure Non_Compliant
     (Register  :     Character;
      Registera : out Integer;
      Registerb : out Integer;
      Registerc : out Integer) is
   begin
      if Register = 'A'
      then
         Registera := 111;
      elsif Register = 'B'
      then
         Registerb := 222;
      end if;
   end Non_Compliant;

   procedure Compliant
     (Register  :     Character;
      Registera : out Integer;
      Registerb : out Integer;
      Registerc : out Integer) is
   begin
      Registera := -1;
      Registerb := -1;
      Registerc := -1;
      if Register = 'A'
      then
         Registera := 111;
      elsif Register = 'B'
      then
         Registerb := 222;
      end if;
   end Compliant;

begin
   Non_Compliant (Register, Registera, Registerb, Registerc);
   Compliant (Register, Registera, Registerb, Registerc);

end Rpp04;
