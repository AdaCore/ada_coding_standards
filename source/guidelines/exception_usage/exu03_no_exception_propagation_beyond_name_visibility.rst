---------------------------------------------------------
No Exception Propagation Beyond Name Visibility (EXU03)
---------------------------------------------------------

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

*Remediation* :math:`\rightarrow` **Low**

*Verification Method* :math:`\rightarrow` GNATcheck rule: ``Non_Visible_Exceptions``

"""""""""""
Reference
"""""""""""

RPP05

"""""""""""""
Description
"""""""""""""

An active exception can be propagated dynamically past the point where the name of the exception is visible (the scope of the declaration). The exception can only be handled via "others" past that point. That situation prevents handling the exception specifically, and violates RPP05.

"""""""
Notes
"""""""

N/A
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   package P is
      procedure Q;
   end P;
   
   package body P is
      Error : exception;
      procedure Q is
      begin
         ...
         raise Error;   -- under some circumstance
         ...
      end Q;
   end P;
   
As a result the exception name cannot be referenced outside the body:
   
.. code:: Ada

   begin -- some code outside of P
      P.Q;
   exception
      when P.Error =>   -- illegal

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

Either make the exception name visible to clients:

.. code:: Ada
   
   package P is
      Error : exception;   -- moved from package body
      procedure Q;
   end P;
   
or ensure the exception is not propagated beyond the scope of its declaration:
   
.. code:: Ada

   package body P is
      Error : exception;
      procedure Q is
      begin
         ...
         raise Error;   -- under some circumstance
         ...
      exception
         when Error => ...
      end Q;
   end P;
