
===================
Concurrency (CON)
===================

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: :math:`\checkmark`
   :Performance: :math:`\checkmark`
   :Security: 

Description
   Have a plan for managing the use of concurrency in high-integrity applications having real-time requirements.

Rules
   CON01, CON02, CON02

The canonical approach to applications having multiple periodic and aperiodic activities is to map those activities onto independent tasks, i.e., threads of control. The advantages for the application are both a matter of software engineering and also ease of implementation. For example, when the different periods are not harmonics of one another, the fact that each task executes independently means that the differences are trivially represented. In contrast, such periods are not easily implemented in a cyclic scheduler, which, by definition, involves only one (implicit) thread of control with one frame rate.

High integrity applications are subject to a number of stringent analyses, including, for example, safety analyses and certification against rigorous industry standards. In addition, high integrity applications with real-time requirements must undergo timing analysis because they must be shown to meet deadlines prior to deployment -- failure to meet hard deadlines is unacceptable in this domain.

These analyses are applied both to the application and to the implementation of the underlying run-time library.  However, analysis of the complete set of general Ada tasking features is not tractable, neither technically nor in terms of cost. A subset of the language is required.

The Ravenscar profile [AdaRM2016]_ is a subset of the Ada concurrency facilities that supports determinism, schedulability analysis, constrained memory utilization, and certification to the highest integrity levels. Four distinct application domains are specifically intended:

   * Hard real-time applications requiring predictability,  
   * Safety-critical systems requiring formal, stringent certification, 
   * High-integrity applications requiring formal static analysis and verification,
   * Embedded applications requiring both a small memory footprint and low execution overhead.

Those tasking constructs that preclude analysis at the source level or analysis of the tasking portion of the underlying run-time library are disallowed. 

The Ravenscar profile is necessarily strict in terms of what it removes so that it can support the stringent analyses, such as safety analysis, that go beyond the timing analysis required for real-time applications. In addition, the strict subset facilitates that timing analysis in the first place. 

However, not all high-integrity applications are amenable to expression in the Ravenscar profile subset. The Jorvik profile [AdaRM2020]_ is an alternative subset of the Ada concurrency facilities. It is based directly on the Ravenscar profile but removes selected restrictions in order to increase expressive power, while retaining analyzability and performance. As a result, typical idioms for protected objects can be used, for example, and relative delays statements are allowed. Timing analysis is still possible but slightly more complicated, and the underlying run-time library is slightly larger and more complex.

When the most stringent analyses are required and the tightest timing is involved, use the Ravenscar profile. When a slight increase in complexity is tolerable, i.e., in those cases not undergoing all of these stringent analyses, consider using the Jorvik profile.

-----------------------------------
Use the Ravenscar Profile (CON01)
-----------------------------------

*Safety*
   :Cyber: :math:`\checkmark`
   :Required: 

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: :math:`\checkmark`
   :Performance: :math:`\checkmark`
   :Security: 

*Remediation* :math:`\rightarrow` **High**

"""""""""""
Reference
"""""""""""

Ada RM section D.13

"""""""""""""
Description
"""""""""""""

The following profile must be in effect:

   pragma Profile (Ravenscar);

The profile is equivalent to the following set of pragmas:

pragma Task_Dispatching_Policy (FIFO_Within_Priorities);

pragma Locking_Policy (Ceiling_Locking);

pragma Detect_Blocking;

pragma Restrictions (

          	No_Abort_Statements,

          	No_Dynamic_Attachment,

          	No_Dynamic_CPU_Assignment,

          	No_Dynamic_Priorities,

          	No_Implicit_Heap_Allocations,

          	No_Local_Protected_Objects,

          	No_Local_Timing_Events,

          	No_Protected_Type_Allocators,

          	No_Relative_Delay,

          	No_Requeue_Statements,

          	No_Select_Statements,

          	No_Specific_Termination_Handlers,

          	No_Task_Allocators,

          	No_Task_Hierarchy,

          	No_Task_Termination,

          	Simple_Barriers,

          	Max_Entry_Queue_Length => 1,

          	Max_Protected_Entries => 1,

          	Max_Task_Entries => 0,

          	No_Dependence => Ada.Asynchronous_Task_Control,

          	No_Dependence => Ada.Calendar,

          	No_Dependence => Ada.Execution_Time.Group_Budgets,

          	No_Dependence => Ada.Execution_Time.Timers,

          	No_Dependence => Ada.Synchronous_Barriers,

          	No_Dependence => Ada.Task_Attributes,

          	No_Dependence => System.Multiprocessors.Dispatching_Domains);

"""""""
Notes
"""""""

The Ada builder will detect violations if the programmer specifies this profile or corresponding pragmas. GNATcheck also can detect violations of profile restrictions.

""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""

   * 6.63 "Lock protocol errors [CGM]".

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

Any code disallowed by the profile. Remediation is "high" because use of the facilities outside the subset can be difficult to retrofit into compliance.

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

N/A

--------------------------------
Use the Jorvik Profile (CON02)
--------------------------------

*Safety*
   :Cyber: :math:`\checkmark`
   :Required: 

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: :math:`\checkmark`
   :Performance: :math:`\checkmark`
   :Security: 

*Remediation* :math:`\rightarrow` **High**

"""""""""""
Reference
"""""""""""

Ada 202x RM section D.13

"""""""""""""
Description
"""""""""""""

The following profile must be in effect:

   pragma Profile (Jorvik);

The profile is equivalent to the following set of pragmas:

pragma Task_Dispatching_Policy (FIFO_Within_Priorities);

pragma Locking_Policy (Ceiling_Locking);

pragma Detect_Blocking;

pragma Restrictions (

              No_Abort_Statements,

              No_Dynamic_Attachment,

              No_Dynamic_CPU_Assignment,

              No_Dynamic_Priorities,

              No_Local_Protected_Objects,

              No_Local_Timing_Events,

              No_Protected_Type_Allocators,

              No_Requeue_Statements,

              No_Select_Statements,

              No_Specific_Termination_Handlers,

              No_Task_Allocators,

              No_Task_Hierarchy,

              No_Task_Termination,

              Pure_Barriers,

              Max_Task_Entries => 0,

              No_Dependence => Ada.Asynchronous_Task_Control,

              No_Dependence => Ada.Execution_Time.Group_Budgets,

              No_Dependence => Ada.Execution_Time.Timers,

              No_Dependence => Ada.Task_Attributes,

              No_Dependence => System.Multiprocessors.Dispatching_Domains);

These restrictions are removed from Ravenscar:

    No_Implicit_Heap_Allocations

    No_Relative_Delay

    Max_Entry_Queue_Length => 1

    Max_Protected_Entries => 1

    No_Dependence => Ada.Calendar

    No_Dependence => Ada.Synchronous_Barriers

Jorvik also replaces restriction Simple_Barriers with Pure_Barriers (a weaker requirement than Simple_Barriers).

"""""""
Notes
"""""""

The Ada builder will detect violations. GNATcheck can also detect violations.

"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

Any code disallowed by the profile. Remediation is "high" because use of the facilities outside the subset can be difficult to retrofit into compliance.

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

N/A

-------------------------------------------------------------
Avoid Shared Variables for Inter-task Communication (CON03)
-------------------------------------------------------------

*Safety*
   :Cyber: :math:`\checkmark`
   :Required: 

*Goal*
   :Maintainability: :math:`\checkmark`
   :Reliability: :math:`\checkmark`
   :Portability: :math:`\checkmark`
   :Performance: :math:`\checkmark`
   :Security: 

"""""""""""
Reference
"""""""""""

Ada RM section D.13

"""""""""""""
Remediation
"""""""""""""

Medium

"""""""""""""
Description
"""""""""""""

Although the Ravenscar and Jorvik profiles allow the use of shared variables for inter-task communication, such use is less robust and less reliable than encapsulating shared variables within protected objects.

"""""""
Notes
"""""""

GNATcheck can detect violations via the Volatile_Objects_Without_Address_Clauses rule. SPARK and CodePeer can also detect conflicting access to unprotected variables. 
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
   * 6.56 "Undefined behaviour [EWF]".
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

A variable marked as Volatile but not assigned to a specific address in memory:
   
   .. code:: Ada

      X : Integer with Volatile;
   
Note that variables marked as Atomic are also Volatile, per the Ada RM  C.6/8(3).

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

When assigned to a memory address, a Volatile variable can be used to interact with a memory-mapped device, among other similar usages.
   
   .. code:: Ada

      GPIO_A : GPIO_Port 
         with Import, Volatile, Address => GPIOA_Base;
   
