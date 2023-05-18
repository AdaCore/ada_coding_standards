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

*Verification Method* :math:`\rightarrow` GNATcheck rule:
``Non_Visible_Exceptions``

+++++++++++
Reference
+++++++++++

RPP05

+++++++++++++
Description
+++++++++++++

An active exception can be propagated dynamically past the point where the name
of the exception is visible (the scope of the declaration). The exception can
only be handled via "others" past that point. That situation prevents handling
the exception specifically, and violates RPP05.

++++++++++++++++++++++++++++++++++++++++++++++++
Applicable vulnerability within ISO TR 24772-2
++++++++++++++++++++++++++++++++++++++++++++++++

N/A

+++++++++++++++++++++++++++
Noncompliant Code Example
+++++++++++++++++++++++++++

.. include:: examples/exu03.adb
  :code: Ada
  :start-line: 3
  :end-line: 11

As a result the exception name cannot be referenced outside the body:

.. include:: examples/exu03.adb
  :code: Ada
  :start-line: 12
  :end-line: 19

++++++++++++++++++++++++
Compliant Code Example
++++++++++++++++++++++++

.. include:: examples/exu03.adb
  :code: Ada
  :start-line: 20
  :end-line: 36


+++++++
Notes
+++++++

N/A
