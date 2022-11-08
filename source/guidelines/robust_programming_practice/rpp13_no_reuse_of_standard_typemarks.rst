----------------------------------------
No Reuse of Standard Typemarks (RPP13)
----------------------------------------

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

*GNATcheck Rule* :math:`\rightarrow` override_standard_name

"""""""""""
Reference
"""""""""""

N/A

"""""""""""""
Description
"""""""""""""

Do not reuse the names of standard Ada typemarks
(e.g. ``type Integer is range -1_000 .. 1_000;``)

When a developer uses an identifier that has the same name as a standard
typemark, such as ``Integer``, a subsequent maintainer might be unaware that
this identifier does not actually refer to ``Standard.Integer`` and might
unintentionally use the locally-scoped ``Integer`` rather than the original
``Standard.Integer``. The locally-scoped ``Integer`` can have different
attributes (and may not even be of the same base type).

"""""""
Notes
"""""""

N/A
   
""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
N/A
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. code:: Ada

   package Example is
      type Word8 is mod 256;
      type Words is array ( Positive range <> ) of Word8;
      subtype Integer is Words(1..4);
   end Example;

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. code:: Ada

   package Example is
      type Word8 is mod 256;
      type Words is array ( Positive range <> ) of Word8;
      subtype Integer_T is Words(1..4);
   end Example;
