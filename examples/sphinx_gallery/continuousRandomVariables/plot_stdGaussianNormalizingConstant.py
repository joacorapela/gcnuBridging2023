

"""
Derivation of the normalizing constant for the standard Normal distribution
===========================================================================

Below we illustrate how to derive this constant analytically and and how to
approximate it by sampling.

Analytical derivation
---------------------

The probability density function of a standard Normal distribution, :math:`f_Z(z)` is

.. math::
   f_Z(z)=\\frac{1}{K}\exp(-\\frac{z^2}{2})

Because :math:`f_Z(z)` is a probability density function, it follows that

.. math::
   1=\int_{-\infty}^\infty f_Z(z)dz=\\frac{1}{K}\int_{-\infty}^\infty\exp(-\\frac{z^2}{2})dz

Then

.. math::
   \\begin{align}
       K&=\int_{-\infty}^\infty\exp(-\\frac{z^2}{2})dz\\\\
       K^2&=\int_{-\infty}^\infty\int_{-\infty}^\infty\exp(-\\frac{x^2}{2})\exp(-\\frac{y^2}{2})dxdy=\int_{-\infty}^\infty\int_{-\infty}^\infty\exp(-\\frac{x^2+y^2}{2}))dxdy
   \\end{align}


We now make the change of variables

.. math::
   \\begin{align}
       r&=\sqrt{x^2+y^2}\\\\
       \\theta&=\\arctan(\\frac{x}{y})
   \\end{align}


for which

.. math::
   \\begin{align}
       x(r,\\theta)&=r\cos(\\theta)\\\\
       y(r,\\theta)&=r\sin(\\theta)
   \\end{align}

with Jacobian

.. math::
   \\begin{align}
       J(r,\\theta)=\\left |\\begin{array}{cc}
                                \\frac{\\partial x}{\\partial r}(r,\\theta)&\\frac{\\partial x}{\\partial \\theta}(r,\\theta)\\\\
                                \\frac{\\partial y}{\\partial r}(r,\\theta)&\\frac{\\partial y}{\\partial \\theta}(r,\\theta)
                           \\end{array}\\right |
                  =\\left |\\begin{array}{cc}
                                \cos(\\theta) & -r\sin(\\theta)\\\\
                                \sin(\\theta) & r\cos(\\theta)
                           \\end{array}\\right |
                  =r\\cos^2(\\theta)+r\\sin^2(\\theta)=r(\\cos^2(\\theta)+\\sin^2(\\theta))=r
   \\end{align}

and obtain

.. math::
   \\begin{align}
       K^2&=\int_0^{2\pi}\int_0^\infty\exp(-\\frac{r^2}{2}))|J(r,\\theta)|drd\\theta=\int_0^{2\pi}\int_0^\infty
       r\exp(-\\frac{r^2}{2})drd\\theta=\int_0^{2\pi}\left(\left.\exp(-\\frac{r^2}{2}))\\right
       |_0^\infty\\right)d\\theta\\\\
          &=\int_0^{2\pi}1d\\theta=2\pi
   \\end{align}

then :math:`K=\sqrt{2\pi}\simeq 2.51`.

Estimation by sampling
----------------------

We can also estimate :math:`K` by sampling. :math:`K` is the area under the
function :math:`\\tilde{f}_Z(z)=\\exp(-\\frac{z^2}{2})`. To estimate this area
we 


1. enclose most of the function :math:`\\tilde{f}_Z(z)` by a box, 

2. draw uniformly distributed samples in this box.

3. calculate the proportion of samples below :math:`\\tilde{f}_Z(z)`.

Now, the ratio of the area under the function :math:`\\tilde{f}_Z(z)`,
:math:`K`, to the area
of the enclosing box, :math:`B`, should be similar to the proportion of uniformly distributed
samples in the box that fell below function :math:`\\tilde{f}_Z(z)`,
:math:`p\_under`. That is :math:`\\frac{K}{B}\\simeq p\_under`, or
:math:`K\simeq B\;p\_under`.

"""

#%%
# Import requirements
# -------------------

import numpy as np
import plotly.graph_objects as go


#%%
# Define constant
# ---------------

lower_z = -5.0
upper_z =  5.0
n_z = 1000
n_random = 100000

zs = np.linspace(lower_z, upper_z, n_z)
f_hat = lambda z: np.exp(-z**2/2)
f_hat_values = f_hat(zs)
box_height = f_hat(0)
box = np.ones(n_z)

#%%
# Sample uniform points in the box
# --------------------------------

random_x = np.random.uniform(low=lower_z, high=upper_z, size=n_random)
random_y = np.random.uniform(low=0, high=1, size=n_random)

#%%
# Calculate the proportion of samples below unnormalized pdf
# ----------------------------------------------------------

count_under = 0
indices_under = []
indices_above = []
for i in range(n_random):
    if random_y[i]<f_hat(random_x[i]):
        count_under += 1
        indices_under.append(i)
    else:
        indices_above.append(i)

#%%
# Estimate K
# ----------

p_under = float(count_under)/n_random
area_box = box_height*(upper_z-lower_z)
print(f"K={area_box*p_under}")

#%%
# Plot samples above and below the unnormalized pdf
# -------------------------------------------------

fig = go.Figure()
trace = go.Scatter(x=zs, y=f_hat_values, mode="lines", line=dict(color="red"),
                  showlegend=False)
fig.add_trace(trace)
trace = go.Scatter(x=zs, y=box, mode="lines", line=dict(color="blue"),
                   showlegend=False)
fig.add_trace(trace)
fig.update_layout(xaxis_title="z", yaxis_title=r"\tilde{f}_Z(z)")
trace = go.Scatter(x=random_x[indices_under], y=random_y[indices_under],
                   mode="markers", line=dict(color="red"), showlegend=False)
fig.add_trace(trace)
trace = go.Scatter(x=random_x[indices_above], y=random_y[indices_above],
                   mode="markers", line=dict(color="blue"), showlegend=False)
fig.add_trace(trace)
fig

