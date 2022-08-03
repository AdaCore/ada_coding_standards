
===================================
Object-Oriented Programming (OOP)
===================================

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: 
   :Performance: 
   :Security: :math:`\checkmark`

Description
   Have a plan for selecting the OOP facilities of the language to use.

Rules
   OOP01, OOP02, OOP03, OOP04, OOP05, OOP06, OOP07

There are many issues to consider when planning the use of Object Oriented features in a high-integrity application. Choices should be made based on the desired expressive power of the OO features and the required level of certification or safety case. 

For example, the use of inheritance can provide abstraction and separation of concerns. However, the extensive use of inheritance, particularly in deep hierarchies, can lead to fragile code bases. 

Similarly, when new types of entities are added, dynamic dispatching provides separation of the code that must change from the code that manipulates those types and need not be changed to handle new types. However, analysis of dynamic dispatching must consider every candidate object type and analyze the associated subprogram for appropriate behavior.

Therefore, the system architect has available a range of possibilities for the use of OOP constructs, with tool enforcement available for the selections. Note that full use of OOP, including dynamic dispatching, may not be unreasonable.

The following rules assume use of tagged types, a requirement for full OOP in Ada.

-----------------------------------------
No Class-wide Constructs Policy (OOP01)
-----------------------------------------

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

*Remediation* :math:`\rightarrow` **N/A**

*GNATcheck Rule* :math:`\rightarrow` no_classwide_constructs

*Mutually Exclusive* :math:`\rightarrow` OOP02

"""""""""""
Reference
"""""""""""

N/A

"""""""""""""
Description
"""""""""""""

In this approach, tagged types are allowed and type extension (inheritance) is allowed, but there are no class-wide constructs. 

This restriction ensures there are no class-wide objects or formal parameters, nor access types designating class-wide types.

In this approach there are no possible dynamic dispatching calls because such calls can only occur when a class-wide value is passed as the parameter to a primitive operation of a tagged type.

"""""""
Notes
"""""""

The compiler will detect violations with the standard Ada restriction No_Dispatch applied. 
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.43 "Redispatching [PPH]"
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   X : Object'Class := Some_Object;

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   X : Object := Some_Object;
   
----------------------------------------
Static Dispatching Only Policy (OOP02)
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

*Remediation* :math:`\rightarrow` **N/A**

*GNATcheck Rule* :math:`\rightarrow` no_dynamic_dispatching

*Mutually Exclusive* :math:`\rightarrow` OOP01

"""""""""""
Reference
"""""""""""

N/A

"""""""""""""
Description
"""""""""""""

In this approach, class-wide constructs are allowed, as well as tagged types and type extension (inheritance), but dynamic dispatching remains disallowed (i.e., as in OOP01).

This rule ensures there are no class-wide values passed as the parameter to a primitive operation of a tagged type, hence there are no dynamically dispatched calls.

Note that this rule should not be applied without due consideration.

"""""""
Notes
"""""""

The compiler will detect violations with the GNAT-defined restriction No_Dispatching_Calls applied. 
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.43 "Redispatching [PPH]"
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   Some_Primitive (Object'Class (X));

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   Some_Primitive (X);
   
-------------------------------------------
Limit Inheritance Hierarchy Depth (OOP03)
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

*Remediation* :math:`\rightarrow` **High**

*GNATcheck Rule* :math:`\rightarrow` Deep_Inheritance_Hierarchies:2

"""""""""""
Reference
"""""""""""

[AdaOOP2016]_ section 5.1

"""""""""""""
Description
"""""""""""""

A class inheritance hierarchy consists of a set of types related by inheritance. Each class, other than the root class, is a subclass of other classes, and each, except for "leaf" nodes, is a base class for those that are derived from it. 

Improperly designed inheritance hierarchies complicate system maintenance and increase the effort in safety certification, in any programming language.

A common characteristic of problematic hierarchies is "excessive" depth, in which a given class is a subclass of many other classes. Depth can be a problem because a change to a class likely requires inspection, modification, recompilation, and retesting/reverification of all classes below it in the hierarchy. The extent of that effect increases as we approach the root class. This rippling effect is known as the "fragile base class" problem. Clearly, the greater the depth the more subclasses there are to be potentially affected. In addition, note that a change to one class may cause a cascade of other secondary changes to subclasses, so the effect is often not limited to a single change made to all the subclasses in question.

Deep inheritance hierarchies also contribute to complexity, rather than lessening it, by requiring the reader to understand multiple superclasses in order to understand the behavior of a given subclass.

"""""""
Notes
"""""""

Violations can be detected with the GNATcheck tool parameter Deep_Inheritance_Hierarchies, specifying a maximum inheritance depth as a parameter of the rule. 

""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""

   * 6.41 "Inheritance [RIP]"

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

The threshold for "too deep" is inexact, but beyond around 4 or 5 levels the complexity accelerates rapidly.

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

N/A

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

*GNATcheck Rule* :math:`\rightarrow` Direct_Calls_To_Primitives

"""""""""""
Reference
"""""""""""

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

"""""""
Notes
"""""""

This rule can be enforced by GNATcheck with the Direct_Calls_To_Primitives rule applied. The rule parameter Except_Constructors may be added for constructor functions.
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   package Graphics is
      type Shape is tagged  -- really, abstract and private
         record
            X : Float := 0.0;
            Y : Float := 0.0;
         end record;

      function Area (This : Shape) return Float;   
        -- would really be abstract
   
      function Momentum (This : Shape) return Float;
      ...
   end Graphics;
   
   package body Graphics is
      function Area (This : Shape) return Float is (0.0);
      function Momentum (This : Shape) return Float is
      begin
     	return This.X * Area (This);   -- wrong, but legal
      end Momentum;
      ...
   end Graphics;
   
In the (somewhat artificial) example above, Momentum always returns zero because it always calls the Area function for type Shape.

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   package body Graphics is
      ...
      function Momentum (This : Shape) return Float is
      begin
     	return This.X * Area (Shape'Class (This)); 
             -- redispatch to an overriding for Area, if any
      end Momentum;
      ...
   end Graphics;
   
---------------------------------------------
Use Explicit Overriding Annotations (OOP05)
---------------------------------------------

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

*GNATcheck Rule* :math:`\rightarrow` Style_Checks:O

"""""""""""
Reference
"""""""""""

[AdaOOP2016]_ section 4.3

"""""""""""""
Description
"""""""""""""

The declaration of a primitive operation that overrides an inherited operation must include an explicit "overriding" annotation.

The semantics of inheritance in mainstream object-oriented languages may result in two kinds of programming errors: 1) intending, but failing, to override an inherited subprogram, and 2) intending not to override an inherited subprogram, but doing so anyway. Because an overridden  subprogram may perform subclass-specific safety or security checks, the invocation of the parent subprogram on a subclass instance can introduce a vulnerability.

The first issue (intending but failing to override) typically occurs when the subprogram name is misspelled. In this case  a new or overloaded subprogram is actually declared. 

The second issue (unintended overriding) can arise when a new subprogram is added to a parent type in an existing inheritance hierarchy. The new subprogram happens to cause one or more inherited subprograms below it to override the new superclass version. This mistake typically happens during program maintenance.

In Ada, much like other modern languages, one can annotate a subprogram declaration (and body) with an indication that the subprogram is an overriding of an inherited version. This is done with the "overriding" reserved word preceding the subprogram specification. 

Similarly, in Ada one can explicitly indicate that a subprogram is not an overriding. To do so, the programmer includes the reserved words "not overriding" immediately prior to the subprogram specification. 

Of course, incorrect marking errors are flagged by the compiler. If a subprogram is explicitly marked as overriding but is not actually overriding, the compiler will reject the code.  Likewise, if a primitive subprogram is explicitly marked as not overriding, but actually is overriding, the compiler will reject the code

However, most subprograms are not overriding so it would be a heavy burden on the programmer to make them explicitly indicate that fact. That's not to mention the relatively heavy syntax required. 

In addition, both annotations are optional for the sake of compatibility with prior versions of the language. Therefore, a subprogram without either annotation might or might not be overriding. A legal program could contain some explicitly annotated subprograms and some that are not annotated at all. But because the compiler will reject explicit annotations that are incorrect, all we require is that one of the two cases be explicitly indicated, for all such subprograms. Any unannotated subprograms not flagged as errors are then necessarily not that case, they must be the other one.

Since overriding is less common and involves slightly less syntax to annotate, the guideline requires explicit annotations only for overriding subprograms. It follows that any subprograms not flagged as errors by the compiler are not overriding, so they need not be marked explicitly as such.

This guideline is implemented by compiler switches, or  alternatively, by a GNATcheck rule (specified below the table). With this guideline applied and enforced, the two inheritance errors described in the introduction cannot happen.

Note that the compiler switches will also require the explicit overriding indicator when overriding a language-defined operator. The switches also apply to inherited primitive subprograms for non-tagged types.

"""""""
Notes
"""""""

This rule requires the GNAT compiler switches "-gnatyO" and "-gnatwe" in order for the compiler to flag missing overriding annotations as errors. The first causes the compiler to generate the warnings, and the second causes those warnings to be treated as errors. Alternatively, GNATcheck will flag those errors via the "+Style_Checks:O" rule.
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.41 "Inheritance [RIP]"
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   type Generator is new Ada.Finalization.Controlled with ...
   
   --  really overriding, but not marked as such
   procedure Initialize (This : in out Generator);
   
   overriding -- marked but not really overriding
   procedure Initialise (This : in out Generator);

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   type Generator is new Ada.Finalization.Controlled with ...
   
   overriding
   procedure Initialize (This : in out Generator);
   
   procedure Initialise (This : in out Generator);
   
-------------------------------------------
Use Class-wide Pre/Post Contracts (OOP06)
-------------------------------------------

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

*GNATcheck Rule* :math:`\rightarrow` Specific_Pre_Post

"""""""""""
Reference
"""""""""""

[AdaOOP2016]_ section 6.1.4 

[SPARK2014]_ section 7.5.2

"""""""""""""
Description
"""""""""""""

For primitive operations of tagged types, use only class-wide pre/post contracts, if any.

The class-wide form of precondition and postcondition expresses conditions that are intended to apply to any version of the subprogram. Therefore, when a subprogram is derived as part of inheritance, only the class-wide form of those contracts is inherited from the parent subprogram, if any are defined. As a result, it only makes sense to use the class-wide form in this situation. 

(The same semantics and recommendation applies to type invariants.)

Note: this approach will be required for OOP07 (Ensure Local Type Consistency).

"""""""
Notes
"""""""

Violations can be detected with the GNATcheck rule Specific_Pre_Post.  SPARK enforces this guideline automatically.
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.42 "Violations of the Liskov substitution principle or the contract model [BLP]"
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   type Stack is tagged ...
   function Top_Element (This : Stack) return Element with
      Pre => not Empty (This),
      ...

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   type Stack is tagged ...
   function Top_Element (This : Stack) return Element with
      Pre'Class => not Empty (This),
      ...
   
---------------------------------------
Ensure Local Type Consistency (OOP07)
---------------------------------------

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

*Remediation* :math:`\rightarrow` **N/A**

*GNATcheck Rule* :math:`\rightarrow` Unimplemented_Use_SPARK_Analysis

"""""""""""
Reference
"""""""""""

[AdaOOP2016]_ See section 4.2.

[GNATUG]_ See section 5.10.11.

"""""""""""""
Remediation
"""""""""""""

High (the correction is syntactically trivial individually, but would be required throughout the tree).

"""""""""""""
Description
"""""""""""""

Either:

* Formally verify local type consistency, or
* Ensure that each tagged type passes all the tests of all the parent types which it can replace.

Rationale:

One of the fundamental benefits of OOP is the ability to manipulate objects in a class inheritance hierarchy without "knowing" at compile-time the specific classes of the objects being manipulated. By "manipulate" we mean invoking the primitive operations, the "methods" defined by the classes.

We will use the words "class" and "type" interchangeably, because classes are composed in Ada and SPARK using a combination of building blocks, especially type declarations. However, we will use the term "subclass" rather than "subtype" because the latter has a specific meaning in Ada and SPARK that is unrelated to OOP.

The objects whose operations are being invoked can be of types anywhere in the inheritance tree, from the root down to the bottom. The location, i.e., the specific type, is transparent to the manipulating code. This type transparency is possible because the invoked operations are dynamically dispatched at run-time, rather than statically dispatched at compile-time. 

Typically, the code manipulating the objects does so in terms of superclasses closer to the root of the inheritance tree. Doing so increases generality because it increases the number of potential subclasses that can be manipulated. The actual superclass chosen will depend on the operations required by the manipulation.  In Ada and SPARK, subclasses can add operations but can never remove them, so more operations are found as we move down from the root. That is the nature of specialization. Note that the guarantee of an invoked operations' existence is essential for languages used in this domain.

However, for this transparent manipulation to be functionally correct -- to accomplish what the caller intends -- the primitive operations of subclasses must be functionally indistinguishable from those of the superclasses. That doesn't mean the subclasses cannot make changes. Indeed, the entire point of subclasses is to make changes. In particular, functional changes can be either introduction of new operations, or overridings of inherited operations. It is these overridings that must be functionally transparent to the manipulating code. (Of course, for an inherited operation that is not overridden, the functionality is inherited as-is, and is thus transparent trivially.)

The concept of functional transparency was introduced, albeit with different terminology, by Liskov and Wing in 1994 [LiskovWing1994]_  and is, therefore, known as the Liskov Substitution Principle, or LSP.  The "substitution" in LSP means that a subclass must be substitutable for its superclass, i.e., a subclass instance should be usable whenever a superclass instance is required. 

Unfortunately, requirements-based testing will not detect violations of LSP because unit-level requirements do not concern themselves with superclass substitutability.

However, the OO supplement of DO-178C [DO178C]_ offers solutions, two of which are in fact the options recommended by this guideline.

Specifically, the supplement suggests adding a specific verification activity it defines as Local Type Consistency Verification. This activity ensures LSP is respected and, in so doing, addresses the vulnerability. 

Verification can be accomplished statically with formal methods in SPARK, or dynamically via a modified form of testing.

For the static approach, type consistency is verified by examining the properties of the overriding operation's preconditions and postconditions. These are the properties required by Design by Contract, as codified by Bertrand Meyer [Meyer1997]_. Specifically, an overridden primitive may only replace the precondition with one weaker than that of the parent version, and may only replace the postcondition with one stronger. In essence, relative to the parent version, an overridden operation can only require the same or less, and provide the same or more. Satisfying that requirement is sufficient to ensure functional transparency because the manipulating code only "knows" the contracts of the class it manipulates, i.e., the view presented by the type, which may very well be a superclass of the one actually invoked.

In Ada and SPARK, the class-wide form of preconditions and postconditions are inherited by overridden primitive operations of tagged types. The inherited precondition and that of the overriding (if any) are combined into a conjunction. All must hold, otherwise the precondition fails. Likewise, the inherited postcondition is combined with the overriding postcondition into a disjunction. At least one of them must hold. In Ada these are tested at run-time. In SPARK, they are verified statically (or not, in which case proof fails and an error is indicated).

To verify substitutability via testing, all the tests for all superclass types are applied to objects of the given subclass type. If all the parent tests pass, this provides a high degree of confidence that objects of the new tagged type can properly substitute for parent type objects. Note that static proof of consistency provides an even higher degree of confidence.

For further discussion of this topic, see the sections cited in the Reference entry in this table.

"""""""
Notes
"""""""

Verification can be achieved dynamically with the GNATtest tool, using the "---validate-type-extensions" switch. SPARK enforces this rule.

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   package P is
      pragma Elaborate_Body;
      type Rectangle is tagged private;
      procedure Set_Width (This  : in out Rectangle;
                           Value : Positive)
      with
         Post => Width (This) = Value and
                 Height (This) = Height (This'Old);
   
      function Width (This : Rectangle) return Positive;
   
      procedure Set_Height (This  : in out Rectangle;
                            Value : Positive)
      with
         Post => Height (This) = Value and
                 Width (This) = Width (This'Old);
   
      function Height (This : Rectangle) return Positive;
   
   private
      ...
   end P;
   
The postcondition for Set_Width states that the Height is not changed. Likewise, for Set_Height, the postcondition asserts that the Width is not changed. However, these postconditions are not class-wide so they are not inherited by subclasses.
   
Now, in a subclass Square, the operations are overridden so that setting the width also sets the height to the same value, and vice versa. Thus the overridden operations do not maintain type consistency, but this fact is neither detected at run-time, nor could SPARK verify it statically (and SPARK is not used at all in these versions of the packages).
   
.. code:: Ada

   with P; use P;
   package Q is
      pragma Elaborate_Body;
      type Square is new Rectangle with private;
   
      overriding
      procedure Set_Width (This  : in out Square;
     	                   Value : Positive)
      with
    	Post => Width (This) = Height (This);
   
      overriding
      procedure Set_Height (This  : in out Square;
     	                    Value : Positive)
      with
    	Post  => Width (This) = Height (This);
   
   private
      ...
   end Q;

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   package P with SPARK_Mode is
      pragma Elaborate_Body;
      type Rectangle is tagged private;
   
      procedure Set_Width (This  : in out Rectangle;
                           Value : Positive)
      with
         Post'Class => Width (This) = Value and
                       Height (This) = Height (This'Old);
   
      function Width (This : Rectangle) return Positive;
   
      procedure Set_Height (This  : in out Rectangle;
                            Value : Positive)
      with
         Post'Class => Height (This) = Value and
                       Width (This) = Width (This'Old);
   
      function Height (This : Rectangle) return Positive;
   
   private
      ...
   end P;
   
Now the postconditions are class-wide so they are inherited by subclasses. In the subclass Square, the postconditions will not hold at run-time. Likewise, SPARK can now prove that type consistency is not verified because the postconditions are weaker than those inherited:
   
.. code:: Ada

   with P; use P;
   package Q with SPARK_Mode is
      pragma Elaborate_Body;
      type Square is new Rectangle with private;
   
      overriding
      procedure Set_Width (This  : in out Square;
                           Value : Positive)
      with
    	Post'Class => Width (This) = Height (This);
   
      overriding
      procedure Set_Height (This  : in out Square;
                            Value : Positive)
      with
    	Post'Class => Width (This) = Height (This);
   
   private
      type Square is new Rectangle with null record;
   end Q;
   
