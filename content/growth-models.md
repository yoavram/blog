Title: Growth models
Date: 2015-10-25 21:32:00 +2
Category: growth

# The logistic model from a resource consumption view

Consider a **resource consumption** model that follows 
the density of a single microbial species through time $N(t)$ 
and the density of that species' limiting resource $R(t)$:

$$
\frac{dR}{dt} = -a R N \\
\frac{dN}{dt} = \epsilon a R N
$$

where $a$ is the uptake rate of the microbes in question, in units of $(\rho T)^{-1}$ 
(where $\rho$ is density and $T$ is time),
and $\epsilon$ is the dimensionless conversion rate of resource to biomass.

The following treatment follows [@Arditi2015]. 
By definition:

$$
\frac{d(\epsilon R + N)}{dt} = \\
\epsilon \frac{dR}{dt} + \frac{dN}{dt} = \\
-\epsilon a R N + \epsilon a R N \equiv 0
$$

Therefore, $\epsilon R + N$ is constant:

$$
M \equiv \epsilon R(t) + N(t) = \\
 \epsilon R(0) + N(0) \Rightarrow \\
M - N = \epsilon R \Rightarrow \\
\frac{dN}{dt} = a N (M-N) = aM N (1 - \frac{N}{M})
$$

By substituting $K=M$ and $r=aK$ we get the **logistic model**:

$$
\frac{dN}{dt} = r N \Big(1 - \frac{N}{K}\Big)
$$

This derivation gives an interesting interpretation to the model parameters:
We usually refer to $K$ as the _carrying capacity_, _maximum population size_, _yield_ or _density_.
Under this interpretation, $K=M=N(0) + \epsilon R(0)$ is the initial population density plus whatever population density there is to make from converting **all** the resource.
This is in line with the standard interpretation.

We usually refer to $r$ as the _proportional increase of the population density_ in one unit of time.
Under this interpretation, $r=aK=a \epsilon R + a N$ is in $T^{-1}$;
since $a$ is the rate of resource uptake per resource density per population density per time unit, 
if $N \approx 0$ then $r \approx a \epsilon R$ is 
the rate at which each population density unit uptakes and converts the resources at hand ($R$),
which is in line with the standard interpretation.

Another derivation in [@Arditi2015] assumes that the resource is biotic (prey) that has a logistic growth of its own; McArthur showed that the predator growth is logistic if the conversion rate is slow enough to allow separation of time scales.

Yet another derivations in [@Arditi2015] assumes direct intraspecific interference.
Assume the population grows exponentialy:

$$
\frac{dN}{dt} = r N
$$

but that encounters between individuals can lead to mortality. Assuming perfect mixing, the number of individulas dying due to interferece is $\lambda N^2$ and we get:

$$
\frac{dN}{dt} = r N - \lambda N^2 = r N \Big(1 - \frac{N}{K}\Big)
$$

where $K=r/\lambda$.

# Richards model

The Richards model is ana extension ofthe logistic model, introducting the parameter $\nu$:

$$
\frac{dN}{dt} = r N (1 - \Big( \frac{N}{K})^{\nu} \Big)
$$

This model is also called the Generalized logistic model or, in its discrete time version, the $\theta$-logistic model [@Gilpin1973].

When $\nu=1$, this is the logistic model; when $\nu=0$ this is the **Gompertz model**.

According to [@Richards1959], one interpretation of $\nu$ is that $(1+\nu)^{-1/\nu}$ *states explicitly the proportion of the final size ($K$) at which the growth rate ($\frac{dN}{dt}$) is maximal*; 
*i.e.*, this is the value of $N/K$ at which the inflexion point of the growth curve ($\frac{d^2N}{dt^2}=0$) occurs
(note that Richards uses the symbol $m=\nu+1$ and therefore the inflexion point occurs as $N/K=m^{1/(1-m)}$).
When $\nu=0$, this occurs at $N/K=e^{-1}$; when $\nu=1$, this occurs at 1/2.

## Solution

To solve this model [@Skiadas2010], we define $y=N/K$ and $z=y^{-\nu}$ to get:

$$
\frac{dz}{dt} = -r \nu (z - 1) \\
z(0) = \Big( \frac{N_0}{K} \Big)^{-\nu}
$$

which is solved to 
$$
z(t) = 1 + e^{-r \nu t} \cdot C \\
z(0) = 1 + C \Rightarrow
C = \Big(\frac{N_0}{K}\Big)^{-\nu} - 1 \Rightarrow \\
z(t) = 1 + e^{-r \nu t} \Big(\frac{N_0}{K}\Big)^{-\nu} \Rightarrow \\
N(t) = \frac{K}{\Big[1 - \Big( 1- \Big( \frac{K}{N_0}\Big)^{\nu}\Big) e^{-r \nu t} \Big]^{1/\nu}}
$$

## Derivation

Following [@Schnute1981], we define the population size $N$ and the per capita growth rate $Z$:

$$
\frac{dN}{dt} = N Z \Rightarrow Z = \frac{1}{N} \frac{dN}{dt} \\\\
\frac{dZ}{dt} = \nu Z ( Z-r) = \nu Z^2 -\nu r Z
$$

Integrating this system with the initial conditions $N(0)=N_0, \lim_{t \to \infty}{N(t)} = K$ gives the same solution as above.