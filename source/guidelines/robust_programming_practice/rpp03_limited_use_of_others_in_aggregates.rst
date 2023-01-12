-----------------------------------------------
Limited Use of "others" In Aggregates (RPP03)
-----------------------------------------------

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

*Verification Method* :math:`\rightarrow` GNATcheck rule: ``OTHERS_In_Aggregates``

"""""""""""
Reference
"""""""""""

Similar to RPP01

"""""""""""""
Description
"""""""""""""

Do not use an "others" choice in an extension aggregate. In record and array aggregates, do not use an "others" choice unless it is used either to refer to all components, or to all but one component.

This guideline prevents accidental provision of a general value for a record component or array component, when a specific value was intended. This possibility includes the case in which new components are added to an existing composite type.

""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2
""""""""""""""""""""""""""""""""""""""""""""""""

* 6.5 Enumerator issues [CCB]
* 6.27 Switch statements and static analysis [CLL]

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. include:: examples/rpp03.ads
  :code: Ada
  :start-line: 3
  :end-line: 14

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. include:: examples/rpp03.ads
  :code: Ada
  :start-line: 17
  :end-line: 27

"""""""
Notes
"""""""

GNATcheck can detect violations via the OTHERS_In_Aggregates rule.
