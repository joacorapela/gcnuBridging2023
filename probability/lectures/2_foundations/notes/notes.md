
# Goals

- demonstrate that probability is deductive

- provide many examples of probability problems

- compare the analytical and simulation approach of computing probabilities

# Expected from introduction

- notion of random experiment

- histogram of outcomes from random experiments

- frequency-based interpretation of probability

# Source Tijms, 2012

# 7. History

- explain the frequency-based interpretation of probability.

- constructing the mathematical foundations of probability theory has proven to be a long-lasting process of trial an error.  

- the approach of defining probability as relative frequencies of repeatable experiments lead to unsatisfactory theory (why?)
https://www.jstor.org/stable/pdf/20115155.pdf

- the frequency view of probability has a long history that goes back to Aristotle.

- in 1933 the Russian mathematician Andrej Kolmogrov (1903-1987) laid a satisfactory mathematical foundation of probability theory.

He created a set of axioms. Axioms state a number of minimal requirements that the probability objects should satisfy. From these few algorithms all claims of probability can be derived, as we will see.

# 7.1 Probabilistic foundation

- sample space
    - examples of finite, countable and uncountable
    - mention the proof by Cantor that the real numbers are not countable

# 7.1.1 Axioms of probability theory
- events in countable and uncountable sample spaces (hint about sigma algebras)
- probability measure
    - three axioms
        - explain what an infinite union means
- probability space: sample space + events + probability measure = probability space
- building a probability measure for a finite or countable sample space.
- probability model = sample space + probability measure

## Equally likely outcomes
- examples
- uncountable sample space

# 7.3 Some basic rules
- Rules 7-1 to 7-3
- problems
    - example 7.7 (rule 7-2): Chevalier de Mere to Blaise Pascal 1654
    - example 7.8 (rule 7-3, addition rule, easy)
    - example 7.9 (rule 7-3): uses counting tools (binomial coefficient)
        - wrong, but simple, approach
        - correct, but more complicated, approach
        - sampling approach
    - example 7.10 (rule 7-1, birthday problem, used in example 8.6): uses counting tools (binomial coefficient)

# 8 Conditional probability and Bayes

- p. 256: good motivation of conditional probability in the cards example

## 8.1 Conditional probability

- Definition 8.1

- interpretation of condition probability with relative frequencies

- Example 8.1 (first ask students their intuition, as the problem is counter intuitive)

- do NOT present example 8.2 at this point, as it requires the concept of independence

## 8.1.1 Assigning probabilities by conditioning

- Rule 8.1: $P(A_1, ..., A_N) = P(A_N|A_1, ..., A_{N-1}) \ldots P(A_1)$

- two examples that follow the previous rule:

    - redo Example 7.9

    - probability that it takes 10 or more cards before the first ace appears

## 8.1.2 Independent events

- motivation of independence definition with conditional probabilities

- Definition 8.2

- Example 8.5

- Example 8.6 (uses birthday problem, example 7.10)

# 8.2 Law of conditional probability

- example of dice followed by coin tosses

- Rule 8.2: law of conditional probability

- example 8.6: tour the France (difficult!)

# 8.3 Baye's rule in odds form

- true/false hypothesis

- Rule 8.3

- interpretation of rule 8.3

    - avoid need of P(E)

    - prior odds + likelihood ratio or Bayes factor

    - prior odds update with new evidence

    - sequential update -> Bayesian linear regression

- example 8.8

- example 8.11

    - add to the problem statement:

        - in 1992, 4936 women were murdered in the US, of which roughly 1430 were murdered by their (ex)husbands or boyfriends

        - 5% of the married women in the US have at some point been physically abused by their husbands.

        - assume that a woman who has been murdered by some other than her husband had the same same chance of being abused by her husband as a randomly selected woman

        - Alan Dershowitz admitted that a substantial percentage of the husbands who murder their wives, previous to the murder, also physically abuse their wives. Given this statement, we assume that the proability that a husband physically abused his wife, given that he killed her, is 50 percent.

# 8.4 Bayesian inference -- discrete case

- explain posterior sequential update

- example 8.13 (solve it analytically and by sampling)

