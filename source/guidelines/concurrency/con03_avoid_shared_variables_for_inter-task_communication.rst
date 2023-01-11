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

*GNATcheck Rule* :math:`\rightarrow` Volatile_Objects_Without_Address_Clauses

"""""""""""
Reference
"""""""""""

`Ada RM D.13 - The Ravenscar Profile <http://ada-auth.org/standards/12rm/html/RM-D-13.html>`_

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

.. include:: examples/con03.ads
  :code: Ada
  :start-line: 4
  :end-line: 7
   
Note that variables marked as Atomic are also Volatile, per the
`Ada RM C.6/8(3) - Shared Variable Control <http://www.ada-auth.org/standards/12rm/html/RM-C-6.html>`_

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

When assigned to a memory address, a Volatile variable can be used to interact with a memory-mapped device, among other similar usages.
   
.. include:: examples/con03.ads
  :code: Ada
  :start-line: 10
  :end-line: 14
