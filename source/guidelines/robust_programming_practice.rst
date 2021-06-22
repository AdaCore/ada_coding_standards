   
===================================
Robust Programming Practice (RPP)
===================================

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: :math:`\checkmark`
   :Performance: :math:`\checkmark`
   :Security: :math:`\checkmark`

Description
   These rules promote the production of robust software.

Rules
   RPP01, RPP02, RPP03, RPP04, RPP05, RPP06, RPP07, RPP07, RPP08, RPP09, RPP10, RPP11, RPP12

-----------------------------------------------
No Use of "others" in Case Constructs (RPP01)
-----------------------------------------------

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

"""""""""""
Reference
"""""""""""

[SEI-C]_ MSC01-C

"""""""""""""
Description
"""""""""""""

Case statement alternatives and case-expressions must not include use of the "others" discrete choice option. This rule prevents accidental coverage of a choice added after the initial case statement is written, when an explicit handler was intended for the addition.

Note that this is opposite to typical C guidelines such as [SEI-C]_ MSC01-C. The reason is that in C, "default" alternative plays the role of defensive code to mitigate the switch statement's non-exhaustivity. In Ada, the case construct is exhaustive: compiler statically verifies that for every possible value of the case expression there is a branch alternative, and there is also a dynamic check against invalid values which serves as implicit defensive code; as a result, Ada's "others" alternative doesn't play C's defensive code role and therefore a stronger guideline can be adopted.

"""""""
Notes
"""""""

GNATcheck can detect violations via the OTHERS_In_CASE_Statements rule. 
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.39.1 "Unanticipated exceptions from library routines [HJW]".
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   type Agency is ( ESA, NASA, RFSA, JAXA, CNSA);
   --  there are dozens...
   Bureau : Agency;
   ...
   case Bureau is
      ...
      when others => ...
   end case;

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   type Agency is ( ESA, NASA, RFSA, JAXA, CNSA);
   --  there are dozens...
   Bureau : Agency;
   ...
   case Bureau is
      when ESA =>  ...
      when NASA => ...
      when RFSA => ...
      when JAXA => ...
      when CNSA => ...
   end case;
   
--------------------------------------------------
No Enumeration Ranges in Case Constructs (RPP02)
--------------------------------------------------

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

"""""""""""
Reference
"""""""""""

Similar to RPP01

"""""""""""""
Description
"""""""""""""

A range of enumeration literals must not be used as a choice in a case statement or a case expression. This includes explicit ranges (A .. B), subtypes, and the 'Range attribute. Much like the use of "others" in case statement alternatives, the use of ranges makes it possible for a new enumeration value to be added but not handled with a specific alternative, when a specific alternative was intended.

"""""""
Notes
"""""""

GNATcheck can detect violations via the Enumeration_Ranges_In_CASE_Statements rule. 
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.5 "Enumerator issues [CCB]".
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   type Agency is (ESA, NASA, RFSA, JAXA, CNSA);
   --  there are dozens...
   Bureau : Agency;
   ...
   case Bureau is
       when ESA .. RFSA => Do_Something;
       when ...
   end case;

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   type Agency is (ESA, NASA, RFSA, JAXA, CNSA);
   --  there are dozens...
   Bureau : Agency;
   ...
   case Bureau is
       when ESA | NASA | RFSA => Do_Something
       when ...
   end case;
   
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
   
-----------------------------------------------------
No Unassigned Mode-Out Procedure Parameters (RPP04)
-----------------------------------------------------

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

*Remediation* :math:`\rightarrow` **High**

"""""""""""
Reference
"""""""""""

MISRA C rule 9.1 "The value of an object with automatic storage duration shall not be read before it has been set"

"""""""""""""
Description
"""""""""""""

For any procedure, all formal parameters of mode "out" must be assigned a value if the procedure exits normally. This rule ensures that, upon a normal return, the corresponding actual parameter has a defined value. Ensuring a defined value is especially important for scalar parameters because they are passed by value, such that some value is copied out to the actual. These undefined values can be especially difficult to locate because evaluation of the actual parameter's value might not occur immediately after the call returns.

"""""""
Notes
"""""""

GNATcheck can detect violations via the Unassigned_OUT_Parameters rule. 
   
Warning: This rule only detects a trivial case of an unassigned variable and doesn't provide a guarantee that there is no uninitialized access. It is not a replacement for a rigorous check for uninitialized access provided by advanced static analysis tools such as SPARK and CodePeer. Note that the GNATcheck rule does not check function parameters (as of Ada 2012 functions can have out parameters). As a result, the better choice is either SPARK or CodePeer.
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.32 "Passing parameters and return values [CSJ]".
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   type Agency is (ESA, NASA, RFSA, JAXA, CNSA);
   --  there are dozens...
   for Agency use 
      (ESA => 1, NASA => 3, RFSA => 5, JAXA => 7, CNSA => 9);
   Bureau : Agency := RFSA;
   
   procedure Update (Input   : in Boolean; 
                     Partner : out Agency) 
   is
   begin
      if Input then
         Partner := ...
      end if;
   end Update;
   
In the above, some value is copied back for the second formal parameter Partner, but the value is only defined if the first parameter is True. That value copied to the actual parameter may not be a valid representation for a value of the type. (We give the enumeration values a non-standard representation for the sake of illustration, i.e., to make it more likely that the undefined value is not valid.)

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   type Agency is (ESA, NASA, RFSA, JAXA, CNSA);
   --  there are dozens...
   for Agency use 
      (ESA => 1, NASA => 3, RFSA => 5, JAXA => 7, CNSA => 9);
   
   Bureau : Agency := RFSA;
   
   procedure Update (Input   : in Boolean; 
                     Partner : out Agency) 
   is
   begin
      if Input then
         Partner := ...
      else
         Partner := ...
      end if;
   end Update;
   
--------------------------------------------------
No Use of "others" in Exception Handlers (RPP05)
--------------------------------------------------

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

"""""""""""
Reference
"""""""""""

N/A

"""""""""""""
Description
"""""""""""""

Much like the situation with "others" in case statements and case expressions, the use of "others" in exception handlers makes it possible to omit an intended specific handler for an exception, especially a new exception added to an existing set of handlers. As a result, a subprogram could return normally without having applied any recovery for the specific exception occurrence, which is likely a coding error.

"""""""
Notes
"""""""

GNATcheck can detect violations via the OTHERS_In_Exception_Handlers rule. 
   
ISO TR 24772-2: 6.50.2 slightly contradicts this when applying exception handlers around calls to library routines: 
   
   * "Put appropriate exception handlers in all routines that call library routines, including the catch-all exception handler when others =>."
   
   * Put appropriate exception handlers in all routines that are called by library routines, including the catch-all exception handler when others =>.
   
It also recommends "All tasks should contain an exception handler at the outer level to prevent silent termination due to unhandled exceptions." for vulnerability 6.62 Concurrency - Premature termination.
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   exception
      when others => 
         ...

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

Code that references all handled exceptions by their names.
   
-------------------------------------
Avoid Function Side-Effects (RPP06)
-------------------------------------

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

*Remediation* :math:`\rightarrow` **Medium**

"""""""""""
Reference
"""""""""""

MISRA C rule 13.3 "The value of an expression and its persistent side effects shall be the same under all permitted evaluation orders"

"""""""""""""
Description
"""""""""""""

Functions cannot update an actual parameter or global variable.

A side effect occurs when evaluation of an expression updates an object. This rule applies to function calls, a specific form of expression. 

Side effects enable one form of parameter aliasing (see below) and evaluation order dependencies.  In general they are a potential point of confusion because the reader expects only a computation of a value.

There are useful idioms based on functions with side effects. Indeed, a random number generator expressed as a function must use side effects to update the seed value.  So-called "memo" functions are another example, in which the function tracks the number of times it is called. Therefore, exceptions to this rule are anticipated but should only be allowed on a per-instance basis after careful analysis.

"""""""
Notes
"""""""

Violations are detected by SPARK as part of a rule disallowing side effects on expression evaluation. 
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.24 "Side-effects and order of evaluation [SAM]".
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   Call_Count : Integer := 0;
   function F return Boolean is
      Result : Boolean;
   begin
      ...
      Call_Count := Call_Count + 1;
      return Result;
   end F;

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

Remove the update to Call_Count. or change the function into a procedure with a parameter for Call_Count.
   
---------------------------------------
Functions Only Have Mode "in" (RPP07)
---------------------------------------

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

"""""""""""
Reference
"""""""""""

RP07

"""""""""""""
Description
"""""""""""""

Functions must have only mode "in".

As of Ada 2012, functions are allowed to have the same modes as procedures. However, this can lead to side effects and aliasing.

This rule disallows all modes except mode "in" for functions.

"""""""
Notes
"""""""

Violations are detected by SPARK. 
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.24 "Side-effects and order of evaluation [SAM]".
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   function Square (Input : in out Integer) return Integer is
      Result : Integer;
   begin
      Result := Input * Input;
      Input := Input + 1;
      return Result;
   end Square;

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   function Square (Input : in Integer) return Integer is
      Result : Integer;
   begin
      Result := Input * Input;
      return Result;
   end Square;
   
or
   
.. code:: Ada

   function Square (Input : in Integer) return Integer is
      (Input * Input);
   
-----------------------------------
Limit Parameter Aliasing  (RPP08)
-----------------------------------

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

*Remediation* :math:`\rightarrow` **High**

"""""""""""
Reference
"""""""""""

Ada RM section 6.2

SPARK RM section 6.4.2

"""""""""""""
Description
"""""""""""""

In software, an alias is a name which refers to the same object as another name. In some cases, it is an error in Ada to reference an object through a name while updating it through another name in the same subprogram. Most of these cases cannot be detected by a compiler. Even when not an error, the presence of aliasing makes it more difficult to understand the code for both humans and analysis tools, and thus it may lead to errors being introduced during maintenance.

This rule is meant to detect problematic cases of aliasing that are introduced through the actual parameters and between actual parameters and global variables in a subprogram call. It is a simplified version of the SPARK rule for anti-aliasing defined in SPARK Reference Manual section 6.4.2.

A formal parameter is said to be immutable when the subprogram cannot modify its value or modify the value of an object by dereferencing a part of the parameter of access type (at any depth in the case of SPARK). In Ada and SPARK, this corresponds to either an anonymous access-to-constant parameter or a parameter of mode "in" and not of an access type. Otherwise, the formal parameter is said to be mutable.

A procedure call shall not pass two actual parameters which potentially introduce aliasing via parameter passing unless either:

   * both of the corresponding formal parameters are immutable; or
   * at least one of the corresponding formal parameters is immutable and is of a by-copy type that is not an access type.

If an actual parameter in a procedure call and a global variable referenced by the called procedure potentially introduce aliasing via parameter passing, then:

   * the corresponding formal parameter shall be immutable; and
   * if the global variable is written in the subprogram, then the corresponding formal parameter shall be of a by-copy type that is not an access type.

Where one of the rules above prohibits the occurrence of an object or any of its subcomponents as an actual parameter, the following constructs are also prohibited in this context:

   * A type conversion whose operand is a prohibited construct;
   * A call to an instance of Unchecked_Conversion whose operand is a prohibited construct;
   * A qualified expression whose operand is a prohibited construct;
   * A prohibited construct enclosed in parentheses.

"""""""
Notes
"""""""

All violations are detected by SPARK. The GNAT compiler switch "-gnateA[1]" enables detection of some cases, but not all.
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

      type R is record
        Data : Integer := 0;
      end record;
   
      procedure Detect_Aliasing (Val_1 : in out R; 
                                 Val_2 : in R) 
      is
      begin
         null;
      end Detect_Aliasing;
   
      Obj : R;
   
   begin   
      Detect_Aliasing (Obj, Obj);

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

Don't pass Obj as the actual parameter to both formal parameters.
   
------------------------------------------------------
Use Precondition and Postcondition Contracts (RPP09)
------------------------------------------------------

*Level* :math:`\rightarrow` **Advisory**

*Category*
   :Safety: :math:`\checkmark`
   :Cyber: :math:`\checkmark`

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: :math:`\checkmark`
   :Performance: 
   :Security: :math:`\checkmark`

*Remediation* :math:`\rightarrow` **Low**

"""""""""""
Reference
"""""""""""

Power of Ten rule 5 "The assertion density of the code should average to a minimum of two assertions per function."

"""""""""""""
Description
"""""""""""""

Subprograms should declare Pre and/or Post contracts.  Developers should consider specifying the Global contract as well, when the default does not apply.

Subprogram contracts complete the Ada notion of a specification, enabling clients to know what the subprogram does without having to know how it is implemented.

Preconditions define those logical (Boolean) conditions required for the body to be able to provide the specified behavior. As such, they are obligations on the callers. These conditions are checked at run-time in Ada, prior to each call, and verified statically in SPARK.

Postconditions define those logical (Boolean) conditions that will hold after the call returns normally. As such, they express obligations on the implementer, i.e., the subprogram body. The implementation must be such that the postcondition holds, either at run-time for Ada, or statically in SPARK.

Not all subprograms will have both a precondition and a postcondition, some will have neither.

The Global contract specifies interactions with those objects not local to the corresponding subprogram body. As such, they help complete the specification because, otherwise, one would need to examine the body of the subprogram itself and all those it calls, directly or indirectly, to know whether any global objects were accessed.

"""""""
Notes
"""""""

This rule must be enforced by manual inspection.
   
Moreover, the program must be compiled with enabled assertions (GNAT "-gnata" switch) to ensure that the contracts are executed, or a sound static analysis tool such as CodePeer or SPARK toolset should be used to prove that the contracts are always true.
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.42 "Violations of the Liskov substitution principle or the contract model [BLP]".
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   type Stack is private;
   procedure Push (This : in out Stack;  Item : Element);

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   type Stack is private;
   procedure Push (This : in out Stack;  Item : Element) with
      Pre  => not Full (This),
      Post => not Empty (This)
              and Top_Element (This) = Item
              and Extent (This) = Extent (This)'Old + 1
              and Unchanged (This'Old, Within => This),
      Global => null;
   
-------------------------------------------------------------
Do Not Re-Verify Preconditions In Subprogram Bodies (RPP10)
-------------------------------------------------------------

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

"""""""""""
Reference
"""""""""""

RPP10

"""""""""""""
Description
"""""""""""""

Do not re-verify preconditions in the corresponding subprogram bodies. It is a waste of cycles and confuses the reader as well.

"""""""
Notes
"""""""

This rule can be enforced by CodePeer or SPARK, via detection of dead code.
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   type Stack is private;
   procedure Push (This : in out Stack;  Item : Element) with
      Pre  => not Full (This),
      Post => ...
   ...
   procedure Push (This : in out Stack;  Item : Element) is
   begin
      if Full (This) then  -- redundant check 
         raise Overflow; 
      end if;
      This.Top := This.Top + 1;
      This.Values (This.Top) := Item;
   end Push;

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   type Stack is private;
   procedure Push (This : in out Stack;  Item : Element) with
      Pre  => not Full (This),
      Post => ...
   ...
   procedure Push (This : in out Stack;  Item : Element) is
   begin
      This.Top := This.Top + 1;
      This.Values (This.Top) := Item;
   end Push;
   
-------------------------------------------------
Always Use the Result of Function Calls (RPP11)
-------------------------------------------------

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

"""""""""""
Reference
"""""""""""

MISRA C rule 17.7 "The value returned by a function having 

non-void return type shall be used" and directive 4.7 "  If a function 

returns error information, that error information shall be tested."

"""""""""""""
Description
"""""""""""""

In Ada and SPARK, it is not possible to ignore the object returned by a function call. The call must be treated as a value, otherwise the compiler will reject the call. For example, the value must be assigned to a variable, or passed as the actual parameter to a formal parameter of another call, and so on. 

However, that does not mean that the value is actually used to compute some further results. Although almost certainly a programming error, one could call a function, assign the result to a variable (or constant), and then not use that variable further. 

Note that functions will not have side-effects (due to RPP06) so it is only the returned value that is of interest here.

"""""""
Notes
"""""""

The GNAT compiler warning switch "-gnatwu" (or the more general "-gnatwa" warnings switch) will cause the compiler to detect variables assigned but not read. CodePeer will detect these unused variables as well. SPARK goes further by checking that all computations contribute all the way to subprogram outputs.

""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""

   * 6.47 "Inter-language calling [DJS]" 

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

N/A

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

N/A

----------------------
No Recursion (RPP12)
----------------------

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

"""""""""""
Reference
"""""""""""

MISRA C rule 17.2 "Functions shall not call themselves, either directly or indirectly"

"""""""""""""
Remediation
"""""""""""""

Low

"""""""""""""
Description
"""""""""""""

No subprogram shall be invoked, directly or indirectly, as part of its own execution.

In addition to making static analysis more complex, recursive calls make static stack usage analysis extremely difficult, requiring manual supply of call limits (for example).

"""""""
Notes
"""""""

The compiler will detect violations with the restriction No_Recursion in place. Note this is a dynamic check. GNATcheck enforces it statically with +RRecursive_Subprograms, subject to the limitations described in http://docs.adacore.com/live/wave/asis/html/gnatcheck_rm/gnatcheck_rm/predefined_rules.html#recursive-subprograms.
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.35 "Recursion [GDL]"
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   function Factorial (N : Positive) return Positive is
   begin
      if N = 1 then
     	return 1;
      else
     	return N * Factorial (N - 1); -- could overflow
      end if;
   end Factorial;

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   function Factorial (N : Positive) return Positive is
      Result : Positive := 1;
   begin
     for K in 2 .. N loop
     	Result := Result * K;  -- could overflow
      end loop;
      return Result;
   end Factorial;
   
