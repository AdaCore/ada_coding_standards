---------------------------------------
Functions Only Have Mode "in" (RPP07)
---------------------------------------

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

*GNATcheck Rule* :math:`\rightarrow` function_out_parameters

"""""""""""
Reference
"""""""""""

RP07

"""""""""""""
Description
"""""""""""""

Functions must have only mode "in".

As of Ada 2012, functions are allowed to have the same modes as procedures. However, this can lead to side effects and aliasing.

This rule disallows all modes except mode "in" for functions.

"""""""
Notes
"""""""

Violations are detected by SPARK. 
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.24 "Side-effects and order of evaluation [SAM]".
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   function Square (Input : in out Integer) return Integer is
      Result : Integer;
   begin
      Result := Input * Input;
      Input := Input + 1;
      return Result;
   end Square;

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   function Square (Input : in Integer) return Integer is
      Result : Integer;
   begin
      Result := Input * Input;
      return Result;
   end Square;
   
or
   
.. code:: Ada

   function Square (Input : in Integer) return Integer is
      (Input * Input);
