#!python
from __future__ import division, print_function
from pyPRISM.potential.LennardJones import LennardJones

class WeeksChandlerAndersen(LennardJones):
    r'''Purely repulsive Weeks-Chandler-Andersen potential


    **Mathematical Definition**

    .. math::

	U_{\alpha,\beta}(r)  =
            \begin{cases}
                4\epsilon_{\alpha,\beta}\left[\left(\frac{\sigma_{\alpha,\beta}}{r}\right)^{12.0}
                - \left(\frac{\sigma_{\alpha,\beta}}{r}\right)^{6.0}\right] +
                \epsilon_{\alpha,\beta} & r<r_{cut}

                0.0      &  r \geq r_{cut}
            \end{cases}

    .. math::

	r_{cut} = 2^{1/6}\sigma_{\alpha,\beta}


    **Variable Definitions**

    :math:`\epsilon_{\alpha,\beta}`
        Strength of repulsion between sites
	:math:`\alpha` and :math:`\beta`.

    :math:`\sigma_{\alpha,\beta}`
        Length scale of interaction between sites
	:math:`\alpha` and :math:`\beta`.

    :math:`r`
        Distance between sites.

    :math:`r_{cut}`
        Cutoff distance where the value of the potential goes to zero.


    **Description**

    	The Weeks-Chandler-Andersen potential for purely repulsive interactions.
    	This potential is equivalent to the Lennard-Jones potential cut and
    	shifted at the minimum of the potential, which occurs at
    	:math:`r=2^{1/6}\sigma`.

    Example
    -------
    .. code-block:: python

        import pyPRISM

        #Define a PRISM system and set the A-B interaction potential
	sys = pyPRISM.System(['A','B'],kT=1.0)
	sys.domain = pyPRISM.Domain(dr=0.1,length=1024)
        sys.potential['A','B'] = pyPRISM.potential.WeeksChandlerAndersen(epsilon=1.0,sigma=1.0)



    .. math::


    Parameters
    ----------

    '''
    def __init__(self, epsilon, sigma):
        r''' Constructor

        Arguments
        ---------
    	epsilon: float
            Repulsive strength modifier

    	sigma: float
            Contact distance

        '''
        rcut = sigma * 2**(1.0/6.0)
        super(WeeksChandlerAndersen, self).__init__(epsilon, sigma, rcut=rcut, shift=True)

    def __repr__(self):
        return '<Potential: WeeksChandlerAndersen>'
