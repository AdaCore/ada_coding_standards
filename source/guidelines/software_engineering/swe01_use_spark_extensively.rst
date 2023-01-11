-------------------------------
Use SPARK Extensively (SWE01)
-------------------------------

*Level* :math:`\rightarrow` **Advisory**

*Category*
   :Safety: :math:`\checkmark`
   :Cyber: :math:`\checkmark`

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: :math:`\checkmark`
   :Performance: :math:`\checkmark`
   :Security: :math:`\checkmark`

*Remediation* :math:`\rightarrow` **High, as retrofit can be extensive**

*GNATcheck Rule* :math:`\rightarrow` TBD

"""""""""""
Reference
"""""""""""

[SPARK2014]_ Section 8 "Applying SPARK in Practice"

"""""""""""""
Description
"""""""""""""

SPARK has proven itself highly effective, both in terms of low defects, low development costs, and high productivity. The guideline advises extensive of SPARK, especially for the sake of formally proving the most critical parts of the source code. The rest of the code can be in SPARK as well, even if formal proof is not intended, with some parts in Ada when features outside the SPARK subset are essential.

"""""""
Notes
"""""""

Violations are detected by the SPARK toolset.

""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""

   * TBD

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

Any code outside the (very large) SPARK subset is flagged by the compiler.

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

N/A
