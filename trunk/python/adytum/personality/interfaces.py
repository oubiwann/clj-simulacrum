from protocols import Interface

class IOCEAN(Interface):
    '''
    The personality of an individual can be parameterized into five dimensions:
    surgency, agreeableness, conscientiousness, emotional stability, and
    openness to new experiences.  Each of these dimensions is implemented as
    scored from 0 to 1, and acts as a weight upon certain emotions when
    combining into utility.

    This is called the OCEAN personality mapping, due to the use of the
    following terms:
	extraversion, agreeableness, conscientiousness, natural reactions (some
	times referred to as 'neuroticism'), openness to experience

    However, we use the following properties:
        surgency, agreeableness, conscientiousness, emotionalstability,
        openness, 
    '''
    openness = property( ''' Openness to Experience captures the observation
    that occasionally agents will choose an emotionally-neutral, not previously
    explored course of action over one proven to provide some degree of
    gratification.  This is accomplished by having this parameter act as a
    negative weight upon the most intense emotion generated by a course of
    action.  

    Contributing factors: Imagination, Adventurousness, Artistic Interests, 
    Intellect, Emotions, Liberalism
    ''')

    conscientiousness = property( ''' Measures the degree to which agents
    consider the full ramifications of their actions before taking them.  Those
    strongly exhibiting this trait avoid courses of actions leading to negative
    consequences, even if accompanied by substantial positive ones.  Such agents
    are unlikely to choose courses of action considered dishonorable, or risky,
    often at the expense of opportunities to achieve goal successes.  This trait
    is used as a weight for distress, fearsconfirmed, disappointment, disliking,
    pride, shame, admiration, and reproach.  

    Contributing factors: Resourcefulness, Orderliness, Sense of Duty, 
    Achievement Striving, Self-Discipline, Cautiousness
    ''')

    surgency = property( ''' The term surgency refers to the degree to which
    agents are proactive in achieving their goals.  Individuals strongly
    exhibiting this trait consider advancement of their own goals to be of
    paramount importance, potentially at the expense of failing standards and
    preferences, or negative emotional outcomes for others.  A surgent
    individual will not think twice given an opportunity to wade through raw
    sewage for a chance to surprise an unprepared enemy.  As implemented, this
    trait weights the importance of and joy, satisfaction, relief, and liking.
 
    Contributing factors: Friendliness, Activity Level, Gregariousness, Excitement 
    Seeking, Assertiveness, Cheerfulness
    ''')

    agreeableness = property( ''' Agreeable individuals are strongly concerned
    about the goals of others, and will often suppress their own to see them
    satisfied.  An agent dominated by this trait will often betray his instincts
    to follow orders.  This trait weights contribution to utility of gloating,
    pity, happy-for, and resentment.  

    Contributing factors: Trust, Morality, Altruism, Co-operation, Modesty, 
    Sympathy
    ''')

    emotionalstability = property( ''' For decision-making purposes, governs the
    degree to which an agent is willing to endure pain along the path to goal
    achievement.  An emotionally stable person, despite moral and other
    objections to a course of action, may still choose it if under the
    impression that it will have a significantly positive effect on things later
    on.  This term weights the importance of immediate gratification by
    recursively adding the utilities of an imagined successor states.  

    Contributing factors: Anxiety, Anger, Depression, Vulnerability, 
    Immoderation, Self-Consciousness
    ''')

    def setFactors():
        '''
        The factors are set and stored as a 5-tuple.
        '''

    def getFactors():
        '''
        '''

    def mergeFactors(new, previous=(0.5,0.5,0.5,0.5,0.5)):
        '''
	This method allows for additive, averaging adjustments. Use this method
	to update an OCEAN type with new personality data from outside sources.
        '''

class IQuadComponentPersonality(Interface):
    '''
    '''

    def getType():
        '''
        '''

    def setType():
        '''
        '''

    def getCompatibility():
        '''
        '''

    def getOCEANMap():
        '''
	Each of the four elements that comprise the quad type will contribute to
	each of the five OCEAN components. As much as is determinable, they will
	be applied on a sliding scale from 0 to 1. For quad elements that cannot
	effectively be mapped with any degress of usefulness, a neutral value of
	0.5 will be assigned.
        '''

class IMyersBriggs(IQuadComponentPersonality):
    '''
    '''
    def getIndexForLetter(letter):
        '''
        This tells us which index of the reference pair array
        the input letter matches. This is how we standardize
        the ordering, so that the signed integers have
        meaning.
        '''
    def getValueForLetter(letter):
        '''
        This function doesn't care what grouping (index of RP) the letter is
        in, it just returns a 1 or -1, based on the constants defined above.
        '''
    def getLetterForValue(letter_value, pair_index):
        '''
        '''
    def getProperOrder(type_abbr):
        '''
        Order the input temperament type according to the order
        defined in the reference pairs.
        '''
    def getTemperamentList(type_abbr):
        '''
        This accepts a myers-briggs type (4 character string) as input,
        and returns a list of 1s and -1s representing the type components.
        '''
    def getTemperamentArray(type_abbr):
        '''
        This is the same thing as getTemperamentList(), except that it
        returns the result as an numarray array type for linear algebra
        calculations, etc.
        '''
    def getTemperamentString(type_list):
        '''
        Process a list (or numeric array) and return the personality type
        as a standard 4 character myers-briggs string.
        '''
    def checkTemperament(type_abbr):
        '''
        This is a way of standardizing a string value for personality
        type. The called functions perform proper ordering and capitalization.
        '''
    def getDominantFunction(type_list):
        '''
        Dominant functions are either in the T/F grouping or the S/P grouping.
        This function returns the letter abbreviation of the type (one of 'T', 'F',
        'S', or 'P').
        '''
    def getMatchTypes(type_list):
        '''
        Returns a tuple of possible good matches.

        The principles behind establishing "matches" or compatibilies between temperaments
        involve two things:
            1) temperaments that share dominant functions are well-suited for each other
            2) temperaments that have opposite "directions" (Introversion or Extroversion) 
            can well-suited for each other
            3) temperaments that have opposite ways of dealing with the world can be
            well-suited for each other.
            4) temperaments that share "information gathering" methods (Sensing or
            Intuition) can be well-suited for each other.

        This results in the following logic for possible good matches for a given 
        temperament:
            * switch the first index: if it was 'E', makd it 'I' and vice versa
            * find the dominant function, and keep that the same.
            * flip the last index: if it was 'J', make it 'P', and vice versa
            * there now remain two possibilities, provided be the two choices of
            the remaining index.
        '''
    def getCompatibilityScale(person1, person2):
        '''
        This function attempts to scale between 0 and 1 the level of compatibility
        between two individuals, where 1 would be one of the two best matches and 0
        represent the oposite types. Decimal values between 0 and 1 attempt to 
        represent degree of compatibility. 
        '''
    def getCompleteTemperamentStrings():
        '''
        '''
    def getGeneticTemperament(parent1, parent2):
        '''
        The basic jist of this function is this: I wanted some way to produce semi-
        random "off-spring" that were the result of combinations of temperament types. 
        This is not meant to realistically model personality types of children based on
        the types of their parents. However, it does offer a nice way of auto-generating
        family trees/generations of temperaments.
        '''

class IOkCupid(IQuadComponentPersonality):
    '''
    '''
