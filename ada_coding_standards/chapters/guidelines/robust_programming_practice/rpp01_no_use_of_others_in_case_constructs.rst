-----------------------------------------------
No Use of "others" in Case Constructs (RPP01)
-----------------------------------------------

.. include:: ../../../../global.txt

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
:rule:`OTHERS_In_CASE_Statements`

+++++++++++
Reference
+++++++++++

[SEI-C]_ MSC01-C

+++++++++++++
Description
+++++++++++++

Case statement alternatives and case-expressions must not include use of the
:ada:`others` discrete choice option. This rule prevents accidental coverage
of a choice added after the initial case statement is written, when an explicit
handler was intended for the addition.

Note that this is opposite to typical C guidelines such as [SEI-C]_ MSC01-C.
The reason is that in C, :c:`default` alternative plays the role of defensive
code to mitigate the switch statement's non-exhaustivity. In Ada, the case
construct is exhaustive: compiler statically verifies that for every possible
value of the case expression there is a branch alternative, and there is also
a dynamic check against invalid values which serves as implicit defensive code;
as a result, Ada's :ada:`others` alternative doesn't play C's defensive code
role and therefore a stronger guideline can be adopted.

++++++++++++++++++++++++++++++++++++++++++++++++
Applicable vulnerability within ISO TR 24772-2
++++++++++++++++++++++++++++++++++++++++++++++++

* 6.27 Switch statements and static analysis [CLL]

+++++++++++++++++++++++++++
Noncompliant Code Example
+++++++++++++++++++++++++++

.. include:: examples/rpp01.adb
  :code: Ada
  :start-line: 5
  :end-line: 11

++++++++++++++++++++++++
Compliant Code Example
++++++++++++++++++++++++

.. include:: examples/rpp01.adb
  :code: Ada
  :start-line: 15
  :end-line: 21

+++++++
Notes
+++++++

N/A
