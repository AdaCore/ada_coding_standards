----------------------
No Recursion (RPP12)
----------------------

*Level* :math:`\rightarrow` **Advisory**

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

*GNATcheck Rule* :math:`\rightarrow` Recursive_Subprograms

"""""""""""
Reference
"""""""""""

MISRA C rule 17.2 "Functions shall not call themselves, either directly or indirectly"

"""""""""""""
Description
"""""""""""""

No subprogram shall be invoked, directly or indirectly, as part of its own execution.

In addition to making static analysis more complex, recursive calls make static stack usage analysis extremely difficult, requiring manual supply of call limits (for example).

"""""""
Notes
"""""""

The compiler will detect violations with the restriction No_Recursion in place. Note this is a dynamic check. GNATcheck enforces it statically with +RRecursive_Subprograms, subject to the limitations described in http://docs.adacore.com/live/wave/asis/html/gnatcheck_rm/gnatcheck_rm/predefined_rules.html#recursive-subprograms.
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.35 "Recursion [GDL]"
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   function Factorial (N : Positive) return Positive is
   begin
      if N = 1 then
     	return 1;
      else
     	return N * Factorial (N - 1); -- could overflow
      end if;
   end Factorial;

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   function Factorial (N : Positive) return Positive is
      Result : Positive := 1;
   begin
     for K in 2 .. N loop
     	Result := Result * K;  -- could overflow
      end loop;
      return Result;
   end Factorial;
