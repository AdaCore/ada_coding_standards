   
============================
Software Engineering (SWE)
============================

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: :math:`\checkmark`
   :Performance: 
   :Security: :math:`\checkmark`

Description
   These rules promote "best practices" for software development.

Rules
   SWE01, SWE02, SWE03, SWEP04

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

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

Any code outside the (very large) SPARK subset is flagged by the compiler.

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

N/A

-------------------------------------------------------
Enable Optional Warnings and Treat As Errors  (SWE02)
-------------------------------------------------------

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

Power of 10 rule #10: All code must be compiled, from the first day of development, with all compiler warnings enabled at the most

pedantic setting available. All code must compile without warnings.

"""""""""""""
Description
"""""""""""""

The Ada compiler does a degree of static analysis itself, and generates many warnings when they are enabled. These warnings likely indicate very real problems so they should be examined and addressed, either by changing the code or disabling the warning for the specific occurrence flagged in the source code.

To ensure that warnings are examined and addressed one way or the other, the compiler must be configured to treat warnings as errors, i.e.,  preventing object code generation.

Note that warnings will occasionally be given for code usage that is intentional. In those cases the warnings should be disabled by using pragma Warnings with the parameter Off, and a string indicating the error message to be disabled. In other cases, a different mechanism might be appropriate, such as aspect (or pragma) Unreferenced.

"""""""
Notes
"""""""

This rule can be applied via the GNAT "-gnatwae" compiler switch, which both enables warnings and treats them as errors. Note that the switch enables almost all optional warnings, but not all. Some optional warnings correspond to very specific circumstances, and would otherwise generate too much noise for their value.
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.18 "Dead Store [WXQ]"
   * 6.19 Unused variable [YZS]"
   * 6.20 "Identifier name reuse [YOW]"
   * 6.22 "Initialization of variables [LAV]".
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   procedure P (This : Obj) is
   begin
      ... code not referencing This
   end P;
   
The formal parameter controls dispatching for the sake of selecting the subprogram to be called but does not participate in the implementation of the body.

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   procedure P (This : Obj) is
      pragma Unreferenced (This);
   begin
      ... code not referencing This
   end P;
   
The compiler will no longer issue a warning that the formal Parameter This is not referenced. Of course, if that changes and This becomes referenced, the compiler will flag the pragma.
   
------------------------------------------------
Use A Static Analysis Tool Extensively (SWE03)
------------------------------------------------

*Level* :math:`\rightarrow` **Mandatory**

*Category*
   :Safety: :math:`\checkmark`
   :Cyber: :math:`\checkmark`

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: :math:`\checkmark`
   :Performance: :math:`\checkmark`
   :Security: :math:`\checkmark`

*Remediation* :math:`\rightarrow` **High**

*GNATcheck Rule* :math:`\rightarrow` TBD

"""""""""""
Reference
"""""""""""

Power of 10 rule #10: All code must also be checked daily with at least one, but preferably more than one, strong static source code analyzer and should pass all analyses with zero warnings.

"""""""""""""
Description
"""""""""""""

If not using SPARK for regular development, use a static analyzer, such as CodePeer, extensively. No warnings or errors should remain unresolved at the given level adopted for analysis (which can be selected to adjust the false positive ratio).

Specifically, any code checked into the configuration management system must be checked by the analyzer and be error-free prior to check-in. Similarly, each nightly build should produce a CodePeer baseline for the project. 

"""""""
Notes
"""""""

CodePeer is the recommended static analyzer. Note that CodePeer can detect GNATcheck rule violations (via the "--gnatcheck" CodePeer switch and a rules file).

""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""

   * 6.6 "Conversion errors [FLC]"
   * 6.18 "Dead store [WXQ]"
   * 6.19 "Unused variable [YZS]"
   * 6.20 "Identifier name reuse [YOW]"
   * 6.24 "Side-effects and order of evaluation [SAM]"
   * 6.25 "Likely incorrect expression [KOA]"

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

N/A

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

N/A

----------------------------------------
Hide Implementation Artifacts  (SWE04)
----------------------------------------

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

*Remediation* :math:`\rightarrow` **High, as retrofit can be extensive**

*GNATcheck Rule* :math:`\rightarrow` Visible_Components

"""""""""""
Reference
"""""""""""

MISRA C rule 8.7 "Functions and objects should not be defined with external linkage if they are referenced in only one translation unit"

"""""""""""""
Remediation
"""""""""""""

High

"""""""""""""
Description
"""""""""""""

Do not make implementation artifacts compile-time visible to clients. Only make available those declarations that define the abstraction presented to clients by the component. In other words, define Abstract Data Types and use the language to enforce the abstraction. This is a fundamental Object-Oriented Design principle.

This guideline minimizes client dependencies and thus allows the maximum flexibility for changes in the underlying implementation. It minimizes the editing changes required for client code when implementation changes are made. 

This guideline also limits the region of code required to find any bugs to the package and child packages, if any, defining the abstraction.

This guideline is to be followed extensively, as the design default for components. Once the application code size becomes non-trivial, the cost of retrofit is extremely high.

"""""""
Notes
"""""""

This rule can be partially enforced by the GNATcheck switches Visible_Components applied. 

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   generic
      ...
   package Bounded_Stacks is
   
      type Content is 
         array (Physical_Capacity range <>) of Element;
      type Stack (Capacity : Physical_Capacity) is 
         tagged record
            Values : Content (1 .. Capacity);
            Top    : Element_Count := 0;
         end record;
      procedure Push (This : in out Stack; ...
      -- additional primitives ...
   
   end Bounded_Stacks;
   
Note that both type Content, as well as the record type components of type Stack, are visible to clients. Client code may declare variables of type Content and may directly access and modify the record components. Bugs introduced via this access could be anywhere in the entire client codebase.

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   generic
      ...
   package Bounded_Stacks is
      type Stack (Capacity : Physical_Capacity) is 
         tagged private;
      procedure Push (This : in out Stack; ...
      -- additional primitives ...
   private
      type Content is 
         array (Physical_Capacity range <>) of Element;
      type Stack (Capacity : Physical_Capacity) is 
         tagged record
            Values : Content (1 .. Capacity);
            Top    : Element_Count := 0;
         end record;
   end Bounded_Stacks;
   
Type Content, as well as the record type components of type Stack, are no longer visible to clients. Any bugs in the Stack code must be in this package, or its child packages, if any.
   
