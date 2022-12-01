.. role:: ada(code)
    :language: Ada 

--------------------------------------------------
No Use of "others" in Exception Handlers (RPP05)
--------------------------------------------------

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

*Verification Method* :math:`\rightarrow` GNATcheck rule: ``OTHERS_In_Exception_Handlers``

"""""""""""
Reference
"""""""""""

N/A

"""""""""""""
Description
"""""""""""""

Much like the situation with "others" in case statements and case expressions, the use of "others" in exception handlers makes it possible to omit an intended specific handler for an exception, especially a new exception added to an existing set of handlers. As a result, a subprogram could return normally without having applied any recovery for the specific exception occurrence, which is likely a coding error.

"""""""
Notes
"""""""

ISO TR 24772-2: 6.50.2 slightly contradicts this when applying exception handlers around calls to library routines: 
   
   * Put appropriate exception handlers in all routines that call library routines,
     including the catch-all exception handler :ada:`when others =>`
   
   * Put appropriate exception handlers in all routines that are called by library routines,
     including the catch-all exception handler :ada:`when others =>`
   
It also recommends "All tasks should contain an exception handler at the outer level to prevent silent termination due to unhandled exceptions." for vulnerability 6.62 Concurrency - Premature termination.
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   exception
      when others => 
         ...

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

Code that references all handled exceptions by their names.
