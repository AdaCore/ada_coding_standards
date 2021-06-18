   
============================
Software Engineering (SWE)
============================

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

Description
   These rules promote "best practices" for software development.

Rules
   SWE01, SWE02, SWE03, SWEP04

-------------------------------
Use SPARK Extensively (SWE01)
-------------------------------

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
     - False

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
     - True
     - True

"""""""""""""
Description
"""""""""""""

SPARK has proven itself highly effective, both in terms of low defects, low development costs, and high productivity. The guideline advises extensive of SPARK, especially for the sake of formally proving the most critical parts of the source code. The rest of the code can be in SPARK as well, even if formal proof is not intended, with some parts in Ada when features outside the SPARK subset are essential.

"""""""""""
Reference
"""""""""""

[8] Section 8 "Applying SPARK in Practice"

"""""""""""""
Remediation
"""""""""""""

High, as retrofit can be extensive

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   Any code outside the (very large) SPARK subset is flagged by the compiler.

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

N/A

Violations are detected by the SPARK toolset.

-------------------------------------------------------
Enable Optional Warnings and Treat As Errors  (SWE02)
-------------------------------------------------------

.. list-table::
   :stub-columns: 1
   :align: left

   * - Safety 

     - Cyber
     - Required
     - Mandatory

   * -

     - True
     - True
     - False

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
     - False
     - True

"""""""""""""
Description
"""""""""""""

The Ada compiler does a degree of static analysis itself, and generates many warnings when they are enabled. These warnings likely indicate very real problems so they should be examined and addressed, either by changing the code or disabling the warning for the specific occurrence flagged in the source code.

To ensure that warnings are examined and addressed one way or the other, the compiler must be configured to treat warnings as errors, i.e.,  preventing object code generation.

Note that warnings will occasionally be given for code usage that is intentional. In those cases the warnings should be disabled by using pragma Warnings with the parameter Off, and a string indicating the error message to be disabled. In other cases, a different mechanism might be appropriate, such as aspect (or pragma) Unreferenced.

"""""""""""
Reference
"""""""""""

Power of 10 rule #10: All code must be compiled, from the first day of development, with all compiler warnings enabled at the most

pedantic setting available. All code must compile without warnings.

"""""""""""""
Remediation
"""""""""""""

Low

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
   
   This rule can be applied via the GNAT "-gnatwae" compiler switch, which both enables warnings and treats them as errors. Note that the switch enables almost all optional warnings, but not all. Some optional warnings correspond to very specific circumstances, and would otherwise generate too much noise for their value.
   
   Applicable vulnerability within ISO TR 24772-2: 
   
   ? 6.18 "Dead Store [WXQ]"
   
   ? 6.19 Unused variable [YZS]"
   
   ? 6.20 "Identifier name reuse [YOW]"
   
   ? 6.22 "Initialization of variables [LAV]".
   
------------------------------------------------
Use A Static Analysis Tool Extensively (SWE03)
------------------------------------------------

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
     - True
     - True

"""""""""""""
Description
"""""""""""""

If not using SPARK for regular development, use a static analyzer, such as CodePeer, extensively. No warnings or errors should remain unresolved at the given level adopted for analysis (which can be selected to adjust the false positive ratio).

Specifically, any code checked into the configuration management system must be checked by the analyzer and be error-free prior to check-in. Similarly, each nightly build should produce a CodePeer baseline for the project. 

"""""""""""
Reference
"""""""""""

Power of 10 rule #10: All code must also be checked daily with at least one, but preferably more than one, strong static source code analyzer and should pass all analyses with zero warnings.

"""""""""""""
Remediation
"""""""""""""

High

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

N/A

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

N/A

CodePeer is the recommended static analyzer. Note that CodePeer can detect GNATcheck rule violations (via the "--gnatcheck" CodePeer switch and a rules file).

Applicable vulnerability within ISO TR 24772-2: 

? 6.6 "Conversion errors [FLC]"

? 6.18 "Dead store [WXQ]"

? 6.19 "Unused variable [YZS]"

? 6.20 "Identifier name reuse [YOW]"

? 6.24 "Side-effects and order of evaluation [SAM]"

? 6.25 "Likely incorrect expression [KOA]"

----------------------------------------
Hide Implementation Artifacts  (SWE04)
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
     - False

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
     - False
     - True

"""""""""""""
Description
"""""""""""""

Do not make implementation artifacts compile-time visible to clients. Only make available those declarations that define the abstraction presented to clients by the component. In other words, define Abstract Data Types and use the language to enforce the abstraction. This is a fundamental Object-Oriented Design principle.

This guideline minimizes client dependencies and thus allows the maximum flexibility for changes in the underlying implementation. It minimizes the editing changes required for client code when implementation changes are made. 

This guideline also limits the region of code required to find any bugs to the package and child packages, if any, defining the abstraction.

This guideline is to be followed extensively, as the design default for components. Once the application code size becomes non-trivial, the cost of retrofit is extremely high.

"""""""""""
Reference
"""""""""""

MISRA C rule 8.7 "Functions and objects should not be defined with external linkage if they are referenced in only one translation unit"

[1]	"SEI CERT C Coding Standard," The Software Engineering Institute.

[2]	"Guidelines for the Use of the C Language in Critical Systems," MISRA, 2013.

[3]	G. J. Holzmann, "The Power of 10: Rules for Developing Safety-Critical Code," 2006.

[4]	"ISO/IEC TR 15942:2000 Guide for the Use of the Ada Programming Language in High Integrity Systems," ISO/IEC TR 15942:2000, High Integrity Rapporteur Group, July, 2000.

[5]	"ISO/IEC JTC 1/SC 22/WG9 Ada Reference Manual-Language and Standard Libraries-ISO/IEC 8652:2012/Cor 1:2016," 2016.

[6]	"ISO/IEC JTC 1/SC 22/WG9 Ada Reference Manual-Language and Standard

Libraries-ISO/IEC 8652:2020", publication expected in 2020.

[7]	High-Integrity Object-Oriented Programming in Ada, Version 1.4, AdaCore,

	October 24, 2016.

[8]	SPARK 2014 User's Guide, AdaCore,

      http://docs.adacore.com/spark2014-docs/html/ug/index.html

[9]	GNAT User's Guide for Native Platforms, AdaCore,

	http://docs.adacore.com/live/wave/gnat_ugn/html/gnat_ugn/gnat_ugn.html

[10]	B. Liskov and J. Wing. "A behavioral notion of subtyping",ACM Transactions

      on Programming Languages and Systems (TOPLAS), Vol. 16, Issue 6

      (November 1994), pp 1811-1841.

[11]	RTCA DO-178C/EUROCAE ED-12C.Software Considerations in

      Airborne Systems and Equipment Certification. December 2011

[12]	B. Meyer. "Object-Oriented Software Construction", Prentice Hall Professional

      Technical Reference, 2nd Edition, 1997.

[13]	GNATstack User's Guide, AdaCore,

      http://docs.adacore.com/live/wave/gnatstack/html/gnatstack_ug/index.html

[14]	Common Weakness Enumeration (CWE), MITRE, 2019

[15]	"SEI CERT Oracle Coding Standard for Java," The Software Engineering Institute.

"""""""""""""
Remediation
"""""""""""""

High

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
   
   This rule can be partially enforced by the GNATcheck switches Visible_Components applied. 
[15]	"SEI CERT Oracle Coding Standard for Java," The Software Engineering Institute.
