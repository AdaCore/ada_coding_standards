----------------------------------
No Multiple Reclamations (RCL01)
----------------------------------

*Level* :math:`\rightarrow` **Mandatory**

*Category*
   :Safety: :math:`\checkmark`
   :Cyber: :math:`\checkmark`

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: :math:`\checkmark`
   :Performance: 
   :Security: :math:`\checkmark`

*Remediation* :math:`\rightarrow` **High**

*GNATcheck Rule* :math:`\rightarrow` TBD

"""""""""""
Reference
"""""""""""

[CWE2019]_ CWE-415: Double Free

"""""""""""""
Description
"""""""""""""

Never deallocate the storage designated by a given access value more than once.

"""""""
Notes
"""""""

Enforcement of this rule can be provided by manual code review, unless deallocation is forbidden via No_Unchecked_Deallocation or SPARK is used, as ownership analysis in SPARK detects such cases. Note that storage utilization analysis tools such as Valgrind can usually find this sort of error. In addition, a GNAT-defined storage pool is available to help debug such errors.
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

      type String_Reference is access all String;
      procedure Free is new Ada.Unchecked_Deallocation
    	(Object => String,  Name => String_Reference);
      S : String_Reference := new String'("Hello");
      Y : String_Reference;
   begin
      Y := S;
      Free (S);
      Free (Y);
   
""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

Remove the call to Free (Y).
