   
=======================
Exception Usage (EXU)
=======================

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: :math:`\checkmark`
   :Performance: :math:`\checkmark`
   :Security: :math:`\checkmark`

Description
   Have a plan for managing the use of Ada exceptions at the application level.

Rules
   EXU01, EXU02, EXU03, EXU04

Exceptions in modern languages present the software architect with a dilemma. On one hand, exceptions can increase integrity by allowing components to signal specific errors in a manner that cannot be ignored, and, in general, allow residual errors to be caught. (Although there should be no unexpected errors in high integrity code, there may be some such errors due, for example, to unforeseeable events such as radiation-induced single-event upsets.)  On the other hand, unmanaged use of exceptions increases verification expense and difficulty, especially flow analysis, perhaps to an untenable degree. In that case overall integrity is reduced or unwarranted.

In addition, programming languages may define some system-level errors in terms of language-defined exceptions. Such exceptions may be unavoidable, at least at the system level. For example, in Ada, stack overflow is signalled with the language-defined "Storage_Error" exception. Other system events, such as bus error, may also be mapped to language-defined or vendor-defined exceptions.

Complicating the issue further is the fact that, if exceptions are completely disallowed, there will be no exception handling code in the underlying run-time library. The effects are unpredictable if any exception actually does occur.

Therefore, for the application software the system software architect must decide whether to allow exceptions at all, and if they are to be used, decide the degree and manner of their usage. At the system level, the architect must identify the exceptions that are possible and how they will be addressed.

*Applicable vulnerability within ISO TR 24772-2*

   * 6.36 "Ignored error status and unhandled exceptions [OYB]"
   * 6.50 "Unanticipated exceptions from library routines [HJW]"

-------------------------------------------------
Don't Raise Language-Defined Exceptions (EXU01)
-------------------------------------------------

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

*GNATcheck Rule* :math:`\rightarrow` Raising_Predefined_Exceptions

"""""""""""
Reference
"""""""""""

[SEI-Java]_ ERR07-J

"""""""""""""
Description
"""""""""""""

In no case should the application explicitly raise a language-defined exception. 

The Ada language-defined exceptions are raised implicitly in specific circumstances defined by the language standard. Explicitly raising these exceptions would be confusing to application developers. The potential for confusion increases as the exception is propagated up the dynamic call chain, away from the point of the raise statement, because this increases the number of paths and thus corresponding language-defined checks that could have been the cause.

"""""""
Notes
"""""""
   
This restriction is detected by GNATcheck with the Raising_Predefined_Exceptions rule applied.
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   if Fuel_Exhaused (This) then
      raise Constraint_Error;
   end if;

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   Fuel_Limits : exception;
   ...
   if Fuel_Exhaused (This) then
      raise Fuel_Limits;
   end if;

-----------------------------------------------------
No Unhandled Application-Defined Exceptions (EXU02)
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

*Remediation* :math:`\rightarrow` **Low**

*GNATcheck Rule* :math:`\rightarrow` TBD

"""""""""""
Reference
"""""""""""

N/A

"""""""""""""
Description
"""""""""""""

All application-defined exceptions must have at least one corresponding handler that is applicable. Otherwise, if an exception is raised, undesirable behavior is possible. The term "applicable" means that there is no dynamic call chain that can reach the active exception which does not also include a handler that will be invoked for that exception, somewhere in that chain.

When an unhandled exception occurrence is raised in the sequence of statements of an application task and reaches the body of that task, the task completes abnormally. No "notification" of some sort is required or defined by the language, although some vendors' implementations may print out a log message or provide some other non-standard response. (Note that such a notification implies an external persistent environment, such as an operating system, that may not be present in all platforms.) The task failure does not affect any other tasks unless those other tasks attempt to communicate with it. In short, failure is silent. 

Although the language-defined package Ada.Task_Termination can be used to provide a response using standard facilities, not all run-time libraries provide that package. For example, under the  Ravenscar profile, application tasks are not intended to terminate, neither normally nor abnormally, and the language does not define what happens if they do. A run-time library for a memory-constrained target, especially a bare-metal target without an operating system, might  not include any support for task termination when the tasking model is Ravenscar. The effects of task termination in that case are not defined by the language.

When an unhandled exception occurrence reaches the main subprogram and is not handled there, the exception occurrence is propagated to the environment task, which then completes abnormally.  Even if the main subprogram does handle the exception, the environment task still completes (normally in that case). 

When the environment task completes (normally or abnormally) it waits for the completion of dependent application tasks, if any. Those dependent tasks continue executing normally, i.e., they do not complete as a result of the environment task completion. Alternatively, however, instead of waiting for them, the implementation has permission to abort the dependent application tasks, per
`Ada RM 10.2(30) - Program Execution <http://www.ada-auth.org/standards/2xrm/html/RM-10-2.html>`_.
The resulting application-specific effect is undefined.

Finally, whether the environment task waited for the dependent tasks or aborted them, the semantics of further execution beyond that point are undefined. There is no concept of a calling environment beyond the environment task
(`Ada RM 10.2(30) - Program Execution <http://www.ada-auth.org/standards/2xrm/html/RM-10-2.html>`_)
In some systems there is no calling environment, such as bare-metal platforms with only an Ada run-time library and no operating system.

"""""""
Notes
"""""""
   
SPARK can prove that no exception will be raised (or fail to prove it and indicate the failure).

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

N/A

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

N/A

---------------------------------------------------------
No Exception Propagation Beyond Name Visibility (EXU03)
---------------------------------------------------------

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

*GNATcheck Rule* :math:`\rightarrow` Non_Visible_Exceptions

"""""""""""
Reference
"""""""""""

RPP05

"""""""""""""
Description
"""""""""""""

An active exception can be propagated dynamically past the point where the name of the exception is visible (the scope of the declaration). The exception can only be handled via "others" past that point. That situation prevents handling the exception specifically, and violates RPP05.

"""""""
Notes
"""""""

GNATcheck can detect violations via the Non_Visible_Exceptions rule. 
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   package P is
      procedure Q;
   end P;
   
   package body P is
      Error : exception;
      procedure Q is
      begin
         ...
         raise Error;   -- under some circumstance
         ...
      end Q;
   end P;
   
As a result the exception name cannot be referenced outside the body:
   
.. code:: Ada

   begin -- some code outside of P
      P.Q;
   exception
      when P.Error =>   -- illegal

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

Either make the exception name visible to clients:

.. code:: Ada
   
   package P is
      Error : exception;   -- moved from package body
      procedure Q;
   end P;
   
or ensure the exception is not propagated beyond the scope of its declaration:
   
.. code:: Ada

   package body P is
      Error : exception;
      procedure Q is
      begin
         ...
         raise Error;   -- under some circumstance
         ...
      exception
         when Error => ...
      end Q;
   end P;
   
----------------------------------------------
Prove Absence of Run-time Exceptions (EXU04)
----------------------------------------------

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

*GNATcheck Rule* :math:`\rightarrow` TBD

"""""""""""
Reference
"""""""""""

MISRA C rule 1.3 "There shall be no occurrence of undefined or critical unspecified behaviour"

"""""""""""""
Remediation
"""""""""""""

High

"""""""""""""
Description
"""""""""""""

In many high-integrity systems the possible responses to an exception are limited or nonexistent.  In these cases the only approach is to prove exceptions cannot occur in the first place.  Additionally, the cost of proving exceptions cannot happen may be less than the cost of analyzing code in which they are allowed to be raised.

The restriction No_Exceptions can be used with pragma Restrictions to enforce this approach.  Specifically, the restriction ensures that "raise" statements and exception handlers do not appear in the source code and that language-defined checks are not emitted by the compiler.  However, a run-time check performed automatically by the hardware is permitted because it typically cannot be prevented.  An example of such a check would be traps on invalid addresses.  If a hardware check fails, or if an omitted language-defined check would have failed, execution is unpredictable. As a result, enforcement with the restriction is not ideal. However, proof of the absence of run-time errors is possible using the SPARK subset of Ada.

"""""""
Notes
"""""""

This restriction is detected by SPARK, in which any statements explicitly raising an exception must be proven unreachable (or proof fails and the failure is indicated), and any possibility of run-time exception should be proved not to happen.

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

N/A

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

N/A

