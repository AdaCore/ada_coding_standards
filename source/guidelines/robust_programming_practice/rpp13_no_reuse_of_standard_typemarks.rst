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

*GNATcheck Rule* :math:`\rightarrow` overrides_standard_name

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

""""""""""""""""""""""""""""""""""""""""""""""""
Applicable vulnerability within ISO TR 24772-2 
""""""""""""""""""""""""""""""""""""""""""""""""
   
N/A
   
"""""""""""""""""""""""""""
Noncompliant Code Example
"""""""""""""""""""""""""""

.. include:: examples/rpp13.ads
  :code: Ada
  :start-line: 3
  :end-line: 5

""""""""""""""""""""""""
Compliant Code Example
""""""""""""""""""""""""

.. include:: examples/rpp13.ads
  :code: Ada
  :start-line: 8
  :end-line: 10

"""""""
Notes
"""""""

N/A
   