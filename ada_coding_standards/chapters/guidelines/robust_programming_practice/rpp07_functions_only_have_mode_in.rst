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

*Verification Method* :math:`\rightarrow` GNATcheck rule:
``function_out_parameters``

+++++++++++
Reference
+++++++++++

RP07

+++++++++++++
Description
+++++++++++++

Functions must have only mode "in".

As of Ada 2012, functions are allowed to have the same modes as procedures.
However, this can lead to side effects and aliasing.

This rule disallows all modes except mode "in" for functions.

++++++++++++++++++++++++++++++++++++++++++++++++
Applicable vulnerability within ISO TR 24772-2
++++++++++++++++++++++++++++++++++++++++++++++++

* 6.24 Side-effects and order of evaluation [SAM]

+++++++++++++++++++++++++++
Noncompliant Code Example
+++++++++++++++++++++++++++

.. include:: examples/rpp07.adb
  :code: Ada
  :start-line: 3
  :end-line: 10

++++++++++++++++++++++++
Compliant Code Example
++++++++++++++++++++++++

.. include:: examples/rpp07.adb
  :code: Ada
  :start-line: 11
  :end-line: 15

OR

.. include:: examples/rpp07.adb
  :code: Ada
  :start-line: 16
  :end-line: 22

+++++++
Notes
+++++++

Violations are detected by SPARK.
