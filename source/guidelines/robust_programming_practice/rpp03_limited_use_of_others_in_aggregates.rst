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

*GNATcheck Rule* :math:`\rightarrow` OTHERS_In_Aggregates

"""""""""""
Reference
"""""""""""

Similar to RPP01

"""""""""""""
Description
"""""""""""""

Do not use an "others" choice in an extension aggregate. In record and array aggregates, do not use an "others" choice unless it is used either to refer to all components, or to all but one component.

This guideline prevents accidental provision of a general value for a record component or array component, when a specific value was intended. This possibility includes the case in which new components are added to an existing composite type.

"""""""
Notes
"""""""

GNATcheck can detect violations via the OTHERS_In_Aggregates rule. 
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   type Agency is (ESA, NASA, RFSA, JAXA, CNSA);
   --  there are dozens...
   type Agencies_Mask is array (Agency) of Boolean;
   Partners : Agencies_Mask := (NASA | ESA | JAXA | RFSA => True, others => False);

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   Partners : constant Agencies_Mask := (CNSA => False, others => True);
   
In this example, the "others" is allowed because it refers to all but one component.
