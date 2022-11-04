-------------------------------------------------
Don't Raise Language-Defined Exceptions (EXU01)
-------------------------------------------------

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

*GNATcheck Rule* :math:`\rightarrow` Raising_Predefined_Exceptions

"""""""""""
Reference
"""""""""""

[SEI-Java]_ ERR07-J

"""""""""""""
Description
"""""""""""""

In no case should the application explicitly raise a language-defined exception. 

The Ada language-defined exceptions are raised implicitly in specific circumstances defined by the language standard. Explicitly raising these exceptions would be confusing to application developers. The potential for confusion increases as the exception is propagated up the dynamic call chain, away from the point of the raise statement, because this increases the number of paths and thus corresponding language-defined checks that could have been the cause.

"""""""
Notes
"""""""
   
This restriction is detected by GNATcheck with the Raising_Predefined_Exceptions rule applied.
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   if Fuel_Exhaused (This) then
      raise Constraint_Error;
   end if;

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   Fuel_Limits : exception;
   ...
   if Fuel_Exhaused (This) then
      raise Fuel_Limits;
   end if;
