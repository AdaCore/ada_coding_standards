-----------------------------------------------------
No Unassigned Mode-Out Procedure Parameters (RPP04)
-----------------------------------------------------

*Level* :math:`\rightarrow` **Required**

*Category*
   :Safety: :math:`\checkmark`
   :Cyber: :math:`\checkmark`

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: :math:`\checkmark`
   :Performance: 
   :Security: 

*Remediation* :math:`\rightarrow` **High**

*Verification Method* :math:`\rightarrow` GNATcheck rule: ``Unassigned_OUT_Parameters``

"""""""""""
Reference
"""""""""""

MISRA C rule 9.1 "The value of an object with automatic storage duration shall not be read before it has been set"

"""""""""""""
Description
"""""""""""""

For any procedure, all formal parameters of mode "out" must be assigned a value if the procedure exits normally. This rule ensures that, upon a normal return, the corresponding actual parameter has a defined value. Ensuring a defined value is especially important for scalar parameters because they are passed by value, such that some value is copied out to the actual. These undefined values can be especially difficult to locate because evaluation of the actual parameter's value might not occur immediately after the call returns.

"""""""
Notes
"""""""

GNATcheck can detect violations via the Unassigned_OUT_Parameters rule. 
   
Warning: This rule only detects a trivial case of an unassigned variable and doesn't provide a guarantee that there is no uninitialized access. It is not a replacement for a rigorous check for uninitialized access provided by advanced static analysis tools such as SPARK and CodePeer. Note that the GNATcheck rule does not check function parameters (as of Ada 2012 functions can have out parameters). As a result, the better choice is either SPARK or CodePeer.
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.32 "Passing parameters and return values [CSJ]".
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   type Agency is (ESA, NASA, RFSA, JAXA, CNSA);
   --  there are dozens...
   for Agency use 
      (ESA => 1, NASA => 3, RFSA => 5, JAXA => 7, CNSA => 9);
   Bureau : Agency := RFSA;
   
   procedure Update (Input   : in Boolean; 
                     Partner : out Agency) 
   is
   begin
      if Input then
         Partner := ...
      end if;
   end Update;
   
In the above, some value is copied back for the second formal parameter Partner, but the value is only defined if the first parameter is True. That value copied to the actual parameter may not be a valid representation for a value of the type. (We give the enumeration values a non-standard representation for the sake of illustration, i.e., to make it more likely that the undefined value is not valid.)

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   type Agency is (ESA, NASA, RFSA, JAXA, CNSA);
   --  there are dozens...
   for Agency use 
      (ESA => 1, NASA => 3, RFSA => 5, JAXA => 7, CNSA => 9);
   
   Bureau : Agency := RFSA;
   
   procedure Update (Input   : in Boolean; 
                     Partner : out Agency) 
   is
   begin
      if Input then
         Partner := ...
      else
         Partner := ...
      end if;
   end Update;
