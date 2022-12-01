-------------------------------------------------------------
Avoid Shared Variables for Inter-task Communication (CON03)
-------------------------------------------------------------

*Level* :math:`\rightarrow` **Advisory**

*Category*
   :Safety: :math:`\checkmark`
   :Cyber: :math:`\checkmark`

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: :math:`\checkmark`
   :Performance: :math:`\checkmark`
   :Security: 

*Remediation* :math:`\rightarrow` **High**

*Verification Method* :math:`\rightarrow` GNATcheck rule: ``Volatile_Objects_Without_Address_Clauses``

"""""""""""
Reference
"""""""""""

`Ada RM D.13 - The Ravenscar Profile <http://ada-auth.org/standards/12rm/html/RM-D-13.html>`_

"""""""""""""
Remediation
"""""""""""""

Medium

"""""""""""""
Description
"""""""""""""

Although the Ravenscar and Jorvik profiles allow the use of shared variables for inter-task communication, such use is less robust and less reliable than encapsulating shared variables within protected objects.

"""""""
Notes
"""""""

GNATcheck can detect violations via the Volatile_Objects_Without_Address_Clauses rule. SPARK and CodePeer can also detect conflicting access to unprotected variables. 
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.56 "Undefined behaviour [EWF]".
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

A variable marked as Volatile but not assigned to a specific address in memory:
   
   .. code:: Ada

      X : Integer with Volatile;
   
Note that variables marked as Atomic are also Volatile, per the
`Ada RM C.6/8(3) - Shared Variable Control <http://www.ada-auth.org/standards/12rm/html/RM-C-6.html>`_

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

When assigned to a memory address, a Volatile variable can be used to interact with a memory-mapped device, among other similar usages.
   
   .. code:: Ada

      GPIO_A : GPIO_Port 
         with Import, Volatile, Address => GPIOA_Base;
