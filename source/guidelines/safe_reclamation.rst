
========================
Safe Reclamation (RCL)
========================

.. list-table::
   :stub-columns: 1
   :align: left

   * - Goal 

     - Maintainability
     - Reliability
     - Portability
     - Performance
     - Security

   * -

     - True
     - True
     - False
     - True
     - True

Description
   Related to managing dynamic storage at the system (policy) level, these statement-level rules concern the safe reclamation of access ("pointer") values.

Rules
   RCL01, RCL02, RCL03

----------------------------------
No Multiple Reclamations (RCL01)
----------------------------------

.. list-table::
   :stub-columns: 1
   :align: left

   * - Safety 

     - Cyber
     - Required
     - Mandatory

   * -

     - True
     - False
     - True

.. list-table::
   :stub-columns: 1
   :align: left

   * - Goal 

     - Maintainability
     - Reliability
     - Portability
     - Performance
     - Security

   * -

     - True
     - True
     - True
     - False
     - True

"""""""""""""
Description
"""""""""""""

Never deallocate the storage designated by a given access value more than once.

"""""""""""
Reference
"""""""""""

[14] CWE-415: Double Free

"""""""""""""
Remediation
"""""""""""""

High

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

.. code:: Ada

   Remove the call to Free (Y).
   
   Enforcement of this rule can be provided by manual code review, unless deallocation is forbidden via No_Unchecked_Deallocation or SPARK is used, as ownership analysis in SPARK detects such cases. Note that storage utilization analysis tools such as Valgrind can usually find this sort of error. In addition, a GNAT-defined storage pool is available to help debug such errors.
   
----------------------------------------
Only Reclaim Allocated Storage (RCL02)
----------------------------------------

.. list-table::
   :stub-columns: 1
   :align: left

   * - Safety 

     - Cyber
     - Required
     - Mandatory

   * -

     - True
     - False
     - True

.. list-table::
   :stub-columns: 1
   :align: left

   * - Goal 

     - Maintainability
     - Reliability
     - Portability
     - Performance
     - Security

   * -

     - True
     - True
     - True
     - False
     - True

"""""""""""""
Description
"""""""""""""

Only deallocate storage that was dynamically allocated by the evaluation of an allocator (i.e., "new").

This is a possibility because Ada allows creation of access values designating declared (aliased) objects.

"""""""""""
Reference
"""""""""""

[1] MEM34-C: Only Free Memory Allocated Dynamically

"""""""""""""
Remediation
"""""""""""""

High

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

      type String_Reference is access all String;
   
      procedure Free is new Ada.Unchecked_Deallocation
   
    	(Object => String,  Name => String_Reference);
   
      S : aliased String := "Hello";
   
      Y : String_Reference := S'Access;
   
   begin
   
      Free (Y);
   
""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   Remove the call to Free (Y).
   
   Enforcement of this rule can only be provided by manual code review, unless deallocation is forbidden via No_Unchecked_Deallocation.
   
---------------------------------------
Only Reclaim To The Same Pool (RCL03)
---------------------------------------

.. list-table::
   :stub-columns: 1
   :align: left

   * - Safety 

     - Cyber
     - Required
     - Mandatory

   * -

     - True
     - False
     - True

.. list-table::
   :stub-columns: 1
   :align: left

   * - Goal 

     - Maintainability
     - Reliability
     - Portability
     - Performance
     - Security

   * -

     - True
     - True
     - True
     - False
     - True

"""""""""""""
Description
"""""""""""""

When deallocating, ensure that the pool to which the storage will be returned was the same pool from which it was allocated. Execution is erroneous otherwise, meaning anything can happen (RM 13.11.2(16)).

Each access type has an associated storage pool, either implicitly by default, or explicitly with a storage pool specified by the programmer. The implicit default pool might not be the same pool used for another access type, even an access type designating the same subtype.

"""""""""""
Reference
"""""""""""

N/A

"""""""""""""
Remediation
"""""""""""""

High

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

      type Pointer1 is access all Integer;
   
      type Pointer2 is access all Integer;
   
      P1 : Pointer1;
   
      P2 : Pointer2;
   
      procedure Free is new Ada.Unchecked_Deallocation
   
         (Object => Integer,
   
          Name   => Pointer2);
   
   begin
   
      P1 := new Integer;
   
      P2 := Pointer2 (P1); 
   
      ...
   
      Free (P2);
   
   In the above, P1.all was allocated from Pointer1'Storage_Pool, but, via the type conversion, the code above is attempting to return it to Pointer2'Storage_Pool, which may be a different pool.

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   Don't deallocate converted access values.
   
   Enforcement of this rule can only be provided by manual code review, unless deallocation is forbidden via No_Unchecked_Deallocation.
   
