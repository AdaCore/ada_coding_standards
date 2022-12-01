--------------------------------------------------
No Enumeration Ranges in Case Constructs (RPP02)
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

*Verification Method* :math:`\rightarrow` GNATcheck rule: ``Enumeration_Ranges_In_CASE_Statements``

"""""""""""
Reference
"""""""""""

Similar to RPP01

"""""""""""""
Description
"""""""""""""

A range of enumeration literals must not be used as a choice in a case statement or a case expression. This includes explicit ranges (A .. B), subtypes, and the 'Range attribute. Much like the use of "others" in case statement alternatives, the use of ranges makes it possible for a new enumeration value to be added but not handled with a specific alternative, when a specific alternative was intended.

"""""""
Notes
"""""""

N/A
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.5 "Enumerator issues [CCB]".
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   type Agency is (ESA, NASA, RFSA, JAXA, CNSA);
   --  there are dozens...
   Bureau : Agency;
   ...
   case Bureau is
       when ESA .. RFSA => Do_Something;
       when ...
   end case;

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   type Agency is (ESA, NASA, RFSA, JAXA, CNSA);
   --  there are dozens...
   Bureau : Agency;
   ...
   case Bureau is
       when ESA | NASA | RFSA => Do_Something
       when ...
   end case;
