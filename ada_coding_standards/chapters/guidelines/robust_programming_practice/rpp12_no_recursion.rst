----------------------
No Recursion (RPP12)
----------------------

.. include:: ../../../../global.txt

**Level** :math:`\rightarrow` Advisory

Category
   :Safety: :math:`\checkmark`
   :Cyber: :math:`\checkmark`

Goal
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: :math:`\checkmark`
   :Performance:
   :Security:

**Remediation** :math:`\rightarrow` Low

**Verification Method** :math:`\rightarrow` GNATcheck rule:
:rule:`Recursive_Subprograms`

+++++++++++
Reference
+++++++++++

MISRA C Rule 17.2 "Functions shall not call themselves, either directly or
indirectly"

+++++++++++++
Description
+++++++++++++

No subprogram shall be invoked, directly or indirectly, as part of its own
execution.

In addition to making static analysis more complex, recursive calls make static
stack usage analysis extremely difficult, requiring, for example, manual supply of call
limits.

++++++++++++++++++++++++++++++++++++++++++++++++
Applicable vulnerability within ISO TR 24772-2
++++++++++++++++++++++++++++++++++++++++++++++++

* 6.35 Recursion [GDL]

+++++++++++++++++++++++++++
Noncompliant Code Example
+++++++++++++++++++++++++++

.. include:: examples/rpp12.adb
  :code: Ada
  :start-line: 6
  :end-line: 14

++++++++++++++++++++++++
Compliant Code Example
++++++++++++++++++++++++

.. include:: examples/rpp12.adb
  :code: Ada
  :start-line: 15
  :end-line: 23

+++++++
Notes
+++++++

The compiler will detect violations with the restriction No_Recursion in place.
Note this is a dynamic check.

The GNATcheck rule specified above is a static check, subject to the
limitations
described in
`GNATcheck Reference Manual (Recursive Subprograms)
<https://docs.adacore.com/live/wave/lkql/html/gnatcheck_rm/gnatcheck_rm/predefined_rules.html#recursive-subprograms>`_
