class IDecision:
    '''
    serves as the point where diverse emotions, stressors, coping style memories,
    and object affordances are all integrated into a decision for action/inaction,
    for transitioning into a new state or remaining in the old state.

    At each tick of the simulation clock, each agent must be able to process the
    following information:

    * current state name or ID
    * stress-based coping mode (Omega_i where i = 1,5)
    * currently afforded transitions and what actions might cause those state
    transitions (a_nm in A(Omega))
    * subjective desires for each state based on 11 pairs of emotional scales
    summed into an overall utility score, U

    Using all of this information, the agent must select a decision style Phi and
    process the information in order to produce a best repsonse (BR) that maximizes
    expected, discounted rewards or utilities in the current iteration of the world.

    '''
