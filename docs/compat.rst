~~~~~~~~~~~~~~~~~~~~
Compatibility Models
~~~~~~~~~~~~~~~~~~~~

.. contents:: Table of Contents

The following are based upon related models for personality coponent
compatibility: the Big Five (FFM; 5-dimentional model) and the IPIP (which
extends the Big Five to including 30 facets, and thus a 30-dimensional model).
We've also proposed a simplified one for reasoning about the basics of
personality interactions.

Do note, however, that we make a departure from the norm for all of these
models: Neuroticism (and its six facets in IPIP) has been replaced with its
opposite, Stability. This was done to simplify the numeric models; with a
ositive category used instead, the fifth personality component can be treated
just like the other four, with no special numerical considerations.

For all models below, a compatibility level of 5 is the highest, and a level of
1 is the lowest.


Simplified Personality Model
============================

To explore the interactions between personalities and the dynamics that arise
between individuals and groups -- and to be able to visualize these interactions
easily -- a simplified 2-dimensional model is provided.

Based on the Big Five, this model combines Openness, Conscientiousness,
Extraversion, and Agreeableness into one: Engagement. The other axis is
Stability.

Our model for the interactions of these components is as follows:

::

           Engag  Stabi
           -----  -----
  Engag  |   5      3   |
  Stabi  |   3      5   |
           ------------

In words, our model states that for a two-personality interaction:

#. The Engagement component in personality 1 has a high affinity for the
   Engagement component in personality 2;
#. The Engagement component in personality 1 has a medium affinity for the
   Stability component in personality 2;
#. The Stability component in personality 1 has a medium affinity for the
   Engagement component in personality 2;
#. The Stability component in personality 1 has a high affinity for the
   Stability component in personality 2;


Personal Interactions in the Simple Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a simple model of 2-dimensional vectors representing simplified
personalities, let's look at ways in which we might interpret these vectors
and their interactions with each other.

For the examples below, let's define some personalities:

* ``alice = [1 1]`` - High engagenement, high stability
* ``bob = [-1 -1]`` - Low engagement, low stability
* ``carol = [0.5 0]`` - Medium-high engagement, medium stability


Component Interactions
----------------------

Let's define "interaction" as the numerical results obtiained by performing
various operations on any given vector or vectors. This section will strive to
identify what these operations may represent in the context of personality
component interactions.


Projection
----------

(dot product)


Angular Momentum
----------------

(cross product)
(volume of parallelogram)


XXX?
----

(distance)


XXX?
----

(scalar multiplication)


XXX?
----

(scalar triple product)


XXX?
----

(vector triple product)


XXX?
----

(vector fields)


XXX?
----

(gradient)


XXX?
----

(curl)


XXX?
----

(divergence)



XXX?
----

(vector laplacian)


XXX?
----

(laplacian)




Big Five Compatibility Matrix
=============================

The chart below explores a possible general model for how each domain in one
personality might be affected, to a lesser or greater extent, by every other
domain in a different personality.

::

           Openn  Consc  Extra  Agree  Stabi
           -----  -----  -----  -----  -----
  Openn  |   5      3      4      4      4   |
  Consc  |   3      5      2      4      4   |
  Extra  |   4      2      5      3      3   |
  Agree  |   3      4      4      5      4   |
  Stabi  |   3      4      3      4      5   |
           ----------------------------------


::

   [OO OC OE OA ON]   [O]   [OO*O + OC*C + OE*E + OA*A + ON*N]
   [CO CC CE CA CN]   [C]   [CO*O + CC*C + CE*E + CA*A + CN*N]
   [EO EC EE EA EN] * [E] = [EO*O + EC*C + EE*E + EA*A + EN*N]
   [AO AC AE AA AN]   [A]   [AO*O + AC*C + AE*E + AA*A + AN*N]
   [NO NC NE NA NN]   [N]   [NO*O + NC*C + NE*E + NA*A + NN*N]

::

                      [O2]   [O1*O2 O1*C2 O1*E2 O1*A2 O1*N2]
                      [C2]   [C1*O2 C1*C2 C1*E2 C1*A2 C1*N2]
   [O1 C1 E1 A1 N1] * [E2] = [E1*O2 E1*C2 E1*E2 E1*A2 E1*N2]
                      [A2]   [A1*O2 A1*C2 A1*E2 A1*A2 A1*N2]
                      [N2]   [N1*O2 N1*C2 N1*E2 N1*A2 N1*N2]


IPIP Compatibility Matrix
=========================

* Openness to experience
    * Imagination / Fantasy
    * Artistic-Interests / Aesthetics
    * Emotionality / Feelings
    * Adventurousness / Actions
    * Intellect / Ideas
    * Liberalism / Values

* Conscientiousness
    * Self-Efficacy / Competence
    * Orderliness
    * Dutifulness
    * Achievement-Striving
    * Self-Discipline
    * Cautiousness / Deliberation

* Extraversion
    * Friendliness / Warmth
    * Gregariousness
    * Assertiveness
    * Activity-Level
    * Excitement-Seeking
    * Cheerfulness / Positive Emotion

* Agreeableness
    * Trust
    * Morality / Straightforwardness
    * Altruism
    * Cooperation / Compliance
    * Modesty
    * Sympathy / Tendermindedness

* Neuroticism
    * Anxiety
    * Anger / Hostility
    * Depression
    * Self-Consciousness
    * Immoderation / Impulsiveness
    * Vulnerability to Stress

- OR -

* Stability
    * Serenity
    * Happiness / Good Will
    * Contentment
    * Confidence
    * Moderation / Self-Control
    * Indefatigability

::

         Imagi Aesth Emoti Adven Intel Liber Compe Order Dutif Achie Disci Delib Warmt Grega Asser Activ Excit Cheer Trust Moral Altru Coope Modes Sympa Anxie Anger Depre Consc Impul Vulne
         -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Imagi    5     4     3     4     5     3     3     2     3     3     3     2     3     3     3     3     4     3     3     3     3     3     3     3     3     3     3     3     4     3
  Aesth    4     5     3     3     4     4     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3
  Emoti    4     3     5     3     3     3     3     3     3     3     3     3     4     4     3     3     3     4     3     3     3     3     3     4     4     4     4     3     3     4
  Adven    4     3     3     5     4     3     3     3     3     4     3     2     3     3     4     5     5     3     3     3     3     3     3     3     3     3     3     2     4     2
  Intel    5     4     3     4     5     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3
  Liber    3     4     3     3     4     5     3     3     3     3     3     2     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3     3
  Compe                                        5
  Order                                              5
  Dutif                                                    5
  Achie                                                          5
  Disci                                                                5
  Delib                                                                      5
  Warmt                                                                            5
  Grega                                                                                  5
  Asser                                                                                        5
  Activ                                                                                              5
  Excit                                                                                                    5
  Cheer                                                                                                          5
  Trust
  Moral
  Altru
  Coope
  Modes
  Sympa
  Anxie
  Anger
  Depre
  Consc
  Impul
  Vulne

