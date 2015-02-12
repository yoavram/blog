Title: Summary: "Fitness-dependent mutation rates in finite populations" (Shaw and Baer 2011)
Date: 2013-2-19 14:28:00 +2
Category: evolution
Status: draft

## Overview 

### Presentation of Agrawal's results

They start with a summary of the results of @Agrawal2002, who did an infinite population deterministic model:

* In **asexuals**, the mean fitness of SIM at the mutation-selection balance is euqal to $e^{-U}$, just like non-mutators.
* In **sexuals**, the mean fitness of SIM depends on the curveture of the fitness to mutation rate functions - a curveture of $k>1$ will result in a lower equilibrium mean fitness than a curveture of $k<1$.
* The equilibrium genetic load with SIM of asexuals is therefore lower than that of sexuals, increasing the **two-fold cost of sex**.

### Difference from Agrawal's work

* Finite population size - drift, mutational supply?
* non (log)additive fintess - dominance and epistasis

## Model

They used **individual-based simulations** with *birth*, *selection*, *mating* and *death*. The population size is *finite* and *constant*, generations are *non-overlapping generations* and there are *2,000 loci*. The population is mutation-free at the beginning.

### Fitness

Fitness is *Fisherian*, that is 
$$
\omega(i) = (1-s)^i
$$
where *i* is the number of mutations and *s* is the selection coefficient. 

With sex, the fitness is $\omega(i) = \prod_{j=1}^{i}{1-h_j s)}$ where *j* is the deleterious locus and $h_j=1$ and $h_j=h$ in homozygous and heterozygous loci and *h* is the dominance coefficient. When $h=0.5$ there is no dominance. 

There is a technical detail that for **asexuals *s=0.02*** and for **sexuals *s=0.04*** because of these fitness definitions.

A population mean fitness of 0.05 classifies as an **extinction event**.

**Epistasis** was modeled by setting the fitness to be $\omega(i) = e^{-is+\alpha i^2}$.

### Mutation rate

The mutation rate was determined by Agrawal's [-@Agrawal2002] formula:

$$
U_{i} = U_{max}-(U_{max}-U_{min})\omega(i)^k
$$

with $U_{min}=0.1$ and $U_{max}=4$. The number of mutations per reproduction is Poisson distributed. 

### Model flow

- Asexuals:
    - Reproduction: an individual is chosen according to its relative fitness.
    - Mutation: the offspring mutates according to its parent mutation rate.
- Sexuals:
    - Reproduction: two individuals are chosen according to their relative fitness, each produces a gamete by chossing one of the alleles at each locus with 5 random crossovers. Two gametes combine to create a new individual.
    - Mutation: the offspring mutates according to its parent mutation rate.

## Results

In this paper Shaw & Baer [-@Shaw2011] present several lines of results but I will only write about the results which are most interesting to me, for comparison to my work.

### Muller's ratchet

As I discussed in a [previous post](/mean-fitness-at-the-mutation-selection-balance/), in an infinitly large asexual population the mean fitness as the equilibirum, called the *mutation-selection balance*, is equal to $\bar{\omega} = \omega_0 e^(-U)$, where $\omega_0$ is the fitness of the fittest individual and $U$ is the genomic mutation rate per genome per generation.

This does not neccesarily hold for finite populations in which *genetic drift* can have an effect on the dynamics. Genetic drift can cause the fixation of deleterious mutation by *random sampling*, and in time the mean fitness of the population can decrease to levels that are so low that the population, in effect, is extinct. This process has been called **[Muller]'s [ratchet]** [@Muller1964, @Felsenstein1974] - at every 'click' of the 'ratchet' a deleterious mutation is fixed in the population, and assuming no recombination and no back-mutations (or very slow rates of these processes), this fixation is irreversible. The rate at which this ratchet clicks is increasing with the mutation rate and decreasing with selection, recombination and populaiton size.

### Analytical treatment

Haigh [-@Haigh1978] derived the stable distribution of deleterious mutations in an asexual population without beneficial mutations. He started from this equation:
$$
n_ik = \frac{N}{T} \sum_{j=o}^{i} n_{i-j} (1-s)^{i-j} \frac{U^j e^{-U}}{j!}
$$
where $n_i$ is the number of individuals with *i* deleterious mutations, $N=\sum_{i \ge 0} n_i$ is the total population size, *s* is the selection coefficient, *U* is the mutaion rate, and $T = \sum_{i \ge 0} n_i (1-s)^i$. He solved for $n_i$ to get this identity:
$$
n_0 = Ne^{-\lambda/s} \\
n_i = n_o \frac{\lambda^i}{s^i i!}, \; \forall i>1
$$
To find the distribution for SIM, Shaw and Baer modified the mutation rates in Haigh's basic equation:
$$
n_i = \frac{N}{T} \sum_{j=o}^{i} n_{i-j} (1-s)^{i-j} \frac{U_{i-j}^j e^{-U_{i-j}}}{j!}
$$
where $U_{i} = U_{max} - (U_{max} - U_{min})(1-s)^{ik}$ is the mutation rate of an individual with $i$ deleterious mutations.
Without beneficial mutations, the population mean fitness is $e^{-U_0}$ and is also equal to $\frac{T}{N}$, where $U_0 = U_{min}$. Therefore,
$$
n_k = e^{U_0} \sum_{j=o}^{i} n_{i-j} (1-s)^{i-j} \frac{U_{i-j}^j e^{-U_{i-j}}}{j!} = 
\sum_{j=o}^{i} n_{i-j} (1-s)^{i-j} \frac{U_{i-j}^j e^{U_0 - U_{i-j}}}{j!}
$$
which is Eq. (3) in [@Shaw2011]. 

### Numerical treatment 

Since there are no further equations in the paper, I understand that the rest of the treatment of the mutation distribution is numerical. [Figure 1] shows the distribution of mutations in a stable population for different values of *k*, where *k=0* is a constant mutation rate, *k=1* denotes a linear ratio between mutation rate increase and fitness decrease, and very large *k* is almost a step function. The figure shows that the higher *k* is, the more the distribution is biased towards the left, that is, the less loaded classes. As *k=0* gives a Poisson distribution with $U_0/s$ as the parameter (and the mean, and the variance - nothing like a Poisson distribution!), *k>0* gives a different kind of distribution.

### Asexual populations




## References

[Muller]: http://en.wikipedia.org/wiki/Hermann_Joseph_Muller
[ratchet]: http://en.wikipedia.org/wiki/Ratchet_(device)
[Figure 1]: http://onlinelibrary.wiley.com/store/10.1111/j.1420-9101.2011.02320.x/asset/image_n/JEB_2320_f2.gif?v=1&t=hdgbdo6r&s=e408de2de296548126498e914767d39207b9317a