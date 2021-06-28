
==================================
Dynamic Storage Management (DYN)
==================================

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: 
   :Performance: :math:`\checkmark`
   :Security: :math:`\checkmark`

Description
   Have a plan for managing dynamic memory allocation and deallocation.

Rules
   DYN01, DYN02, DYN03, DYN04, DYN05, DYN06

In Ada, objects are created by being either "declared" or "allocated".  Declared objects may be informally thought of as being created "on the stack" although such details are not specified by the language.  "Allocated" objects may be thought of as being allocated "from the heap", which is, again, an informal term. Allocated objects are created by the evaluation of allocators represented by the reserved word "new" and, unlike declared objects, have lifetimes independent of scope.

The terms "static" and "dynamic" tend to be used in place of "declared" and "allocated", although in traditional storage management terminology all storage allocation in Ada is dynamic. In the following discussion, the term "dynamic allocation" refers to storage that is allocated by allocators. "Static" object allocation refers to objects that are declared. "Deallocation" refers to the reclamation of allocated storage.

Unmanaged dynamic storage allocation and deallocation can lead to storage exhaustion; the required analysis is difficult under those circumstances. Furthermore, access values can establish aliases that complicate verification, and explicit deallocation of dynamic storage can lead to specific errors (e.g., "double free", "use after free") having unpredictable results. As a result, the prevalent approach to storage management in high-integrity systems is to disallow dynamic management techniques completely. [SEI-C]_ [MISRA2013]_ [Holzmann2006]_ [ISO2000]_

However, restricted forms of storage management and associated feature usage can support the necessary reliability and analyzability characteristics while retaining sufficient expressive power to justify the analysis expense. The following sections present possible approaches, including the traditional approach in which no dynamic behavior is allowed. Individual projects may then choose which storage management approach best fits their requirements and apply appropriate tailoring, if necessary, to the specific guidelines.  

Realization
   There is a spectrum of management schemes possible, trading ease of analysis against increasing expressive power. At one end there is no dynamic memory allocation (and hence, deallocation) allowed, making analysis trivial. At the other end, nearly the full expressive power of the Ada facility is available, but with analyzability partially retained. In the latter, however, the user must create the allocators in such a manner as to ensure proper behavior.

Rule DYN01 is Required, as it avoids problematic features whatever the strategy chosen. Rules DYN02-05 are marked as Advisory, because one of them should be chosen and enforced throughout a given software project.

*Applicable vulnerability within ISO TR 24772-2*

   * 6.39 "Memory leak and heap fragmentation [XYL].

--------------------------------------------
Common High Integrity Restrictions (DYN01)
--------------------------------------------

*Level* :math:`\rightarrow` **Required**

*Category*
   :Safety: :math:`\checkmark`
   :Cyber: :math:`\checkmark`

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: 
   :Performance: 
   :Security: :math:`\checkmark`

*Remediation* :math:`\rightarrow` **Low**

*GNATcheck Rule* :math:`\rightarrow` TBD

"""""""""""
Reference
"""""""""""

`Ada RM H.4 - High Integrity Restrictions <http://www.ada-auth.org/standards/2xrm/html/RM-H-4.html>`_

"""""""""""""
Description
"""""""""""""

The following restrictions must be in effect:

   * No_Anonymous_Allocators
   * No_Coextensions
   * No_Access_Parameter_Allocators
   * Immediate_Reclamation

The first three restrictions prevent problematic usage that, for example, may cause un-reclaimed (and unreclaimable) storage. The last restriction ensures any storage allocated by the compiler at run-time for representing objects is reclaimed at once. (That restriction does not apply to objects created by allocators in the application.)

"""""""
Notes
"""""""

The compiler will detect violations of the first three restrictions. Note that GNATcheck can detect violations in addition to the compiler.
   
The fourth restriction is a directive for implementation behavior, not subject to source-based violation detection.
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

For No_Anonymous_Allocators:
   
   .. code:: Ada

      X : access String := new String'("Hello");
      ...
      X := new String'("Hello");
   
For No_Coextensions:

   .. code:: Ada
   
      type Object (Msg : access String) is ...
      Obj : Object (Msg => new String'("Hello"));
   
For No_Access_Parameter_Allocators:
   
   .. code:: Ada
   
      procedure P (Formal : access String);
      ...
      P (Formal => new String'("Hello"));
   
""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

For No_Anonymous_Allocators, use a named access type:
   
   .. code:: Ada

      type String_Reference is access all String;   
      S : constant String_Reference := new String'("Hello");
      X : access String := S;
      ...
      X := S;
   
For No_Coextensions, use a variable of a named access type:
   
   .. code:: Ada

      type Object (Msg : access String) is ...
      type String_Reference is access all String;   
      S : String_Reference := new String'("Hello");
      Obj : Object (Msg => S);
   
For No_Access_Parameter_Allocators, use a variable of a named access type:
   
   .. code:: Ada

      procedure P (Formal : access String);
      type String_Reference is access all String;   
      S : String_Reference := new String'("Hello");
      ...
      P (Formal => S);
   
----------------------------------------------
Traditional Static Allocation Policy (DYN02)
----------------------------------------------

*Level* :math:`\rightarrow` **Advisory**

*Category*
   :Safety: :math:`\checkmark`
   :Cyber: :math:`\checkmark`

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: 
   :Performance: 
   :Security: :math:`\checkmark`

*Remediation* :math:`\rightarrow` **Low**

*GNATcheck Rule* :math:`\rightarrow` TBD

"""""""""""
Reference
"""""""""""

MISRA C Dir 4.12 "Dynamic memory allocation shall not be used"

"""""""""""""
Description
"""""""""""""

The following restrictions must be in effect:

   * No_Allocators

   * No_Task_Allocators

Under the traditional approach, no dynamic allocations and no deallocations occur.  Only declared objects are used and no access types of any kind appear in the code.

Without allocations there is no issue with deallocation as there would be nothing to deallocate. "Heap" storage exhaustion and fragmentation are clearly prevented although storage may still be exhausted due to insufficient stack size allotments.

In this approach the following constructs are not allowed:

   * Allocators
   * Access-to-constant access types
   * Access-to-variable access types
   * User-defined storage pools
   * Unchecked Deallocations

"""""""
Notes
"""""""

The compiler, and/or GNATcheck, will detect violations of the restrictions. 

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

Any code using the constructs listed above.

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

N/A

------------------------------------------------
Access Types Without Allocators Policy (DYN03)
------------------------------------------------

*Level* :math:`\rightarrow` **Advisory**

*Category*
   :Safety: :math:`\checkmark`
   :Cyber: :math:`\checkmark`

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: 
   :Performance: 
   :Security: :math:`\checkmark`

*Remediation* :math:`\rightarrow` **Low**

*GNATcheck Rule* :math:`\rightarrow` TBD

"""""""""""
Reference
"""""""""""

MISRA rule 21.3 "The memory allocation and deallocation functions of <stdlib.h> shall not be used"

"""""""""""""
Description
"""""""""""""

The following restrictions must be in effect:

   * No_Allocators
   * No_Dependence => Ada.Unchecked_Deallocation

In this approach dynamic access values are only created via the attribute 'Access applied to aliased objects. Allocation and deallocation never occur. As a result, storage exhaustion cannot occur because no "dynamic" allocations occur. Fragmentation cannot occur because there are no deallocations.  

In this approach the following constructs are not allowed:

   * Allocators
   * User-defined storage pools
   * Unchecked Deallocations

Notes

Aspects should be applied to all access types in this approach, specifying a value of zero for the storage size.  Although the restriction No_Allocators is present, such clauses may be necessary to prevent any default storage pools from being allocated for the access types, even though the pools would never be used. A direct way to accomplish this is to use pragma Default_Storage_Pool with a parameter of "null" like so:

   pragma Default_Storage_Pool (null);

The above would also ensure no allocations can occur with access types that have the default pool as their associated storage pool (per
`Ada RM 13.11.3(6.1/3) - Default Storage Pools <http://ada-auth.org/standards/12rm/html/RM-13-11-3.html>`_)

"""""""
Notes
"""""""

The compiler, and/or GNATcheck, will detect violations of the restrictions. 
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

Any code using the constructs listed above.

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   type Descriptor is ...;
   type Descriptor_Ref is access all Descriptor;
   ...
   Device : aliased Descriptor;
   ...
   P : Descriptor_Ref := Device'Access;
   ...
   
-------------------------------------------
Minimal Dynamic Allocation Policy (DYN04)
-------------------------------------------

*Level* :math:`\rightarrow` **Advisory**

*Category*
   :Safety: :math:`\checkmark`
   :Cyber: :math:`\checkmark`

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: 
   :Performance: 
   :Security: 

*Remediation* :math:`\rightarrow` **Low**

*GNATcheck Rule* :math:`\rightarrow` TBD

"""""""""""
Reference
"""""""""""

Power of Ten rule 3 "Do not use dynamic memory allocation after initialization"

"""""""""""""
Description
"""""""""""""

The following restrictions must be in effect:

   * No_Local_Allocators
   * No_Dependence => Ada.Unchecked_Deallocation

In this approach dynamic allocation is only allowed during "start-up" and no later.  Deallocations never occur.  As a result, storage exhaustion should never occur assuming the initial allotment is sufficient.  This assumption is as strong as when using only declared objects on the "stack" because in that case a sufficient initial storage allotment for the stack must be made.  

In this approach the following constructs are not allowed:

   * Unchecked Deallocations

Note that some operating systems intended for this domain directly support this policy.

"""""""
Notes
"""""""

The compiler, and/or GNATcheck, will detect violations of the restrictions. 
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

Any code using the constructs listed above.

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

Code performing dynamic allocations any time prior to an arbitrary point designated as the end of the "startup" interval.
   
-------------------------------------------
User-Defined Storage Pools Policy (DYN05)
-------------------------------------------

*Level* :math:`\rightarrow` **Advisory**

*Category*
   :Safety: :math:`\checkmark`
   :Cyber: :math:`\checkmark`

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: 
   :Performance: 
   :Security: :math:`\checkmark`

*Remediation* :math:`\rightarrow` **Low**

*GNATcheck Rule* :math:`\rightarrow` TBD

"""""""""""
Reference
"""""""""""

MISRA rule 21.3 "The memory allocation and deallocation functions of <stdlib.h> shall not be used"

"""""""""""""
Description
"""""""""""""

There are two issues that make storage utilization analysis difficult: 1) the predictability of the allocation and deallocation implementation, and 2) how access values are used by the application. The behavior of the underlying implementation is largely undefined and may, for example, consist of calls to the operating-system (if present). Application code can manipulate access values beyond the scope of analysis.

Under this policy, the full expressive power of access-to-object types is provided but one of the two areas of analysis difficulty is removed.  Specifically, predictability of the allocation and deallocation implementation is achieved via user-defined storage pools.  (With these  storage pools, the implementation of allocation ("new") and deallocation (instances of Ada.Unchecked_Deallocation) is defined by the pool type.)

If the pool type is implemented with fixed-size blocks on the stack, allocation and deallocation timing behavior are predictable.

Such an implementation would also be free from fragmentation.

Given an analysis providing the worst-case allocations and deallocations, it would be possible to verify that pool exhaustion does not occur.  However, as mentioned such analysis can be quite difficult. A mitigation would be the use of the "owning" access-to-object types provided by SPARK.

In this approach no storage-related constructs are disallowed unless the SPARK subset is applied.

"""""""
Notes
"""""""

Enforcement of this approach can only be provided by manual code review unless SPARK is used.
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

Allocation via an access type not tied to a user-defined storage pool.

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   Heap : Sequential_Fixed_Blocks.Storage_Pool
            (Storage_Size => Required_Storage_Size,
             Element_Size => Representable_Obj_Size,
             Alignment    => Representation_Alignment);
   type Pointer is access all Unsigned_Longword with
      Storage_Pool => Heap;
   Ptr : Pointer;
   ...
   Ptr := new Unsigned_Longword; -- from Heap
   
---------------------------------------------------------
Statically Determine Maximum Stack Requirements (DYN06)
---------------------------------------------------------

*Level* :math:`\rightarrow` **Required**

*Category*
   :Safety: :math:`\checkmark`
   :Cyber: :math:`\checkmark`

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: 
   :Performance: 
   :Security: 

X
 Security

"""""""""""
Reference
"""""""""""

N/A

"""""""""""""
Remediation
"""""""""""""

High

"""""""""""""
Description
"""""""""""""

Each Ada application task has a stack, as does the "environment task" that elaborates library packages and calls the main subprogram. A tool to statically determine the maximum storage required for these stacks must be used, per task.

This guideline concerns another kind of dynamic memory utilization. The previous guidelines concerned the management of storage commonly referred to as the "heap." This guideline concerns the storage commonly referred to as the "stack."  (Neither term is defined by the language, but both are commonly recognized and are artifacts of the underlying run-time library or operating system implementation.)

"""""""
Notes
"""""""

The GNATstack [GNATstack]_ tool can statically determine the maximum requirements per task. 

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

N/A

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

N/A

