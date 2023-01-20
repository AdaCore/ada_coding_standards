-------------------------------------------------------------------
Limit Statically-Dispatched Calls To Primitive Operations (OOP04)
-------------------------------------------------------------------

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

*Remediation* :math:`\rightarrow` **Medium (easy fix, but a difficult to detect bug)**

*Verification Method* :math:`\rightarrow` GNATcheck rule: ``Direct_Calls_To_Primitives``

"""""""""""
Reference
"""""""""""

   TBD

"""""""""""""
Description
"""""""""""""

This rule applies only to tagged types, when visibly tagged at the point of a call from one primitive to another of that same type.

By default, subprogram calls are statically dispatched. Dynamic dispatching only occurs when a class-wide value is passed to a primitive operation of a specific type. Forcing an otherwise optional dynamic dispatching call in this case is known as "redispatching."

When one primitive operation of a given tagged type invokes another distinct primitive operation of that same type, use redispatching so that an overriding version of that other primitive will be invoked if it exists. Otherwise an existing overridden version would not be invoked, which is very likely an error.

This rule does not apply to the common case in which an overriding of a primitive operation calls the "parent" type's version of the overridden operation. Such calls occur in the overridden body when the new version is not replacing, but rather, is augmenting the parent type's version. In this case the new version must do whatever the parent version did, and can then add functionality specific to the new type.

By default, this rule applies to another common case in which static calls from one primitive operation to another make sense.  Specifically, "constructors" are often implemented in Ada as functions that create a new value of the tagged type.  As constructors, these functions are type-specific. They must call the primitive operations of the type being created, not operations that may be overridden for some type later derived from it. (Note that there is a GNATcheck rule parameter to not flag this case.)

Typically constructor functions only have the tagged type as the result type, not as the type for formal parameters, if any, because actual parameters of the tagged type would themselves likely require construction. This specific usage is the case ignored by the GNATcheck rule parameter.

Note that constructors implemented as procedures also call primitive operations of the specific type, for the same reasons as constructor functions. This usage is allowed by this rule and does not require the GNATcheck parameter. (The difference between function and procedure constructors is that these procedures will have a formal parameter of the tagged type, of mode "out".)

""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2
""""""""""""""""""""""""""""""""""""""""""""""""

* 6.42 Violations of the Liskov substitution principle of the contract model [BLP]
* 6.43 Redispatching [PPH]
* 6.44 Polymorphic variables [BKK]

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

Class constructs

.. include:: examples/oop04.adb
  :code: Ada
  :start-line: 2
  :end-line: 18

Noncompliant Code

.. include:: examples/oop04.adb
  :code: Ada
  :start-line: 21
  :end-line: 26

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. include:: examples/oop04.adb
  :code: Ada
  :start-line: 27
  :end-line: 32

"""""""
Notes
"""""""

N/A
