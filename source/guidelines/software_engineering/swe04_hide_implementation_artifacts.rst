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

*Verification Method* :math:`\rightarrow` GNATcheck rule: ``Visible_Components``

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
