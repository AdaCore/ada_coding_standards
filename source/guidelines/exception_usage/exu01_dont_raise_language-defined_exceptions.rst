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

*Verification Method* :math:`\rightarrow` GNATcheck rule: ``Raising_Predefined_Exceptions``

"""""""""""
Reference
"""""""""""

[SEI-Java]_ ERR07-J

"""""""""""""
Description
"""""""""""""

In no case should the application explicitly raise a language-defined exception. 

The Ada language-defined exceptions are raised implicitly in specific circumstances defined by the language standard. Explicitly raising these exceptions would be confusing to application developers. The potential for confusion increases as the exception is propagated up the dynamic call chain, away from the point of the raise statement, because this increases the number of paths and thus corresponding language-defined checks that could have been the cause.

""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""

N/A

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. include:: examples/exu01.adb
  :code: Ada
  :start-line: 3
  :end-line: 12

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. include:: examples/exu01.adb
  :code: Ada
  :start-line: 13
  :end-line: 22

"""""""
Notes
"""""""
   
This restriction is detected by GNATcheck with the Raising_Predefined_Exceptions rule applied.
   
