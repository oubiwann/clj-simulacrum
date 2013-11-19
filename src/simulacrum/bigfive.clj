(ns simulacrum.bigfive
  (:require [clojure.core.matrix :as m]
            [clojure.core.matrix.operators])
  (:refer clojure.core.matrix.operators :rename
          {/ div
           * mult
           ** pow
           + add
           - sub
           == eql}))

(def min-value 1)
(def mid-value 3)
(def max-value 5)

(def domains
  {:O "Openness"
   :C "Conscientiousness"
   :E "Extraversion"
   :A "Agreeableness"
   :N "Neuroticism"})

(def five-point-compatibility-matrix-model-1
  "The problems observed with this model were:
    * "
  (m/matrix [[5 3 4 4 2]
             [3 5 2 4 3]
             [4 2 5 3 2]
             [3 4 4 5 3]
             [3 2 1 3 5]]))

(def five-point-compatibility-matrix-model-2
  "This model exhibits the following properties:
    * "
  (m/matrix [[5 3 4 4 2]
             [2 5 3 4 1]
             [4 2 5 3 2]
             [3 4 4 5 3]
             [3 2 1 3 5]]))

(def five-point-compatibility-matrix
  "The columns of the compatibilty matrices follow the order of the OCEAN
  acronym:
    1) Openness, 2) Conscientiousness, 3) Extraversion, 4) Agreeableness,
    5) Neuroticism.
  Similarly, the rows number in the same order.

  This function simply points to the matrix that provides the best default
  model for compatibilty.
  For more informtaion, see docs/compat.rst."
  five-point-compatibility-matrix-model-2)

(def signed-compatibility-matrix
  "Convert the compatibilty matrix to one whose values range from -2 to 2, with
  the neurtal value being 0."
  (sub five-point-compatibility-matrix mid-value))

(def normalized-compatibility-matrix
  "Convert the compatibilty matrix to one whose values have been normalized."
  (m/emap
    float
    (div five-point-compatibility-matrix max-value)))

(defn get-scalar-distance
  [pers-matrix-1 pers-matrix-2]
  "Get the scalar value for the distance between the two personality matrices.

  Note that the personality matrices are 1x5."
  (apply m/distance
         (map first [pers-matrix-1 pers-matrix-2])))

(defn get-matrix-difference
  [pers-matrix-1 pers-matrix-2]
  "Get the matrix for the difference between the two given matrices.

  Note that the personality matrices are 1x5 matrices and the resultant matrix
  is the same shape (1x5)."
  (m/emap abs
          (sub pers-matrix-1
               pers-matrix-2)))

(defn get-inverted-matrix-difference
  [pers-matrix-1 pers-matrix-2]
  "Get the matrix for the difference between the two given matrices.

  Note that the personality matrices are 1x5 matrices and the resultant matrix
  is the same shape (1x5)."
  (sub 1
       (get-matrix-difference
         pers-matrix-1
         pers-matrix-2)))

(defn -normalize-matrix
  [matrix normal-mode]
  (cond
    (= normal-mode :dimension)
      (div matrix (last (m/shape matrix)))
    (= normal-mode :largest)
      (div matrix (apply max (flatten matrix)))))

(defn get-normalized-matrix
  ""
  ([matrix-1 matrix-2]
   (get-normalized-matrix matrix-1 matrix-2 :dimension))
  ([matrix-1 matrix-2 normal-mode]
    (let [matrix (m/mmul matrix-1 matrix-2)]
      (-normalize-matrix matrix normal-mode))))

(defn compute-compatibility-matrix
  "Multiply the personality matrices by each other and then the result by the
  compatibilty matrix (the given model).

  'normal-mode' is the method used to select the normalization value. If the
  value of 'normal-mode' is :rank, the matrix rank is used to normalize the
  values in the matrix. If it is :largest, the largest value of the matrix is
  given as the rank."
  ([pers-matrix-1 pers-matrix-2 model]
   (compute-compatibility-matrix
     pers-matrix-1 pers-matrix-2 model :dimension))
  ([pers-matrix-1 pers-matrix-2 model normal-mode]
    (let [pers-combo (m/mmul (m/transpose pers-matrix-1) pers-matrix-2)
          compat-combo (m/mmul pers-combo model)]
      (-normalize-matrix compat-combo normal-mode))))

(def questions-base
  {:instructions (str "Answer each question below by providing a number "
                      "between " min-value " and " max-value ". The values "
                      \newline
                      "of the integers have the following meanings:" \newline
                      \tab "* 5 is 'Agree Strongly'" \newline
                      \tab "* 4 is 'Agree a Little'" \newline
                      \tab "* 3 is 'Neutral'" \newline
                      \tab "* 2 is 'Disagree a Little'" \newline
                      \tab "* 1 is 'Disagree Strongly'. " \newline \newline
                      "How well do the following statements describe your "
                      "personality?")
   :prefix "I see myself as someone who "})

(def questions-short
  (conj
    questions-base
    {:title "Five Factor Model (Big Five) Short Inventory"
     :questions [{:question "is reserved"
                  :domain-key :E
                  :reversed? true}
                 {:question "is generally trusting"
                  :domain-key :A
                  :reversed? false}
                 {:question "tends to be lazy"
                  :domain-key :C
                  :reversed? true}
                 {:question "is relaxed, handles stress well"
                  :domain-key :N
                  :reversed? true}
                 {:question "has few artistic interests"
                  :domain-key :O
                  :reversed? true}
                 {:question "is outgoing, sociable"
                  :domain-key :E
                  :reversed? false}
                 {:question "tends to find fault with others"
                  :domain-key :A
                  :reversed? true}
                 {:question "does a thorough job"
                  :domain-key :C
                  :reversed? false}
                 {:question "gets nervous easily"
                  :domain-key :N
                  :reversed? false}
                 {:question "has an active imagination"
                  :domain-key :O
                  :reversed? false}]}))

(def questions-long
  (conj
    questions-base
    {:title "Five Factor Model (Big Five) Long Inventory"
     :questions [{:number 1
                  :question "is talkative"
                  :domain-key :E
                  :reversed? false}
                 {:number 2
                  :question "tends to find fault with others"
                  :domain-key :A
                  :reversed? true}
                 {:number 3
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 4
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 5
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 6
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 7
                  :question "XXX"
                  :domain-key :A
                  :reversed? false}
                 {:number 8
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 9
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 10
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 11
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 12
                  :question "XXX"
                  :domain-key :A
                  :reversed? true}
                 {:number 13
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 14
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 15
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 16
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 17
                  :question "XXX"
                  :domain-key :A
                  :reversed? false}
                 {:number 18
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 19
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 20
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 21
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 22
                  :question "XXX"
                  :domain-key :A
                  :reversed? false}
                 {:number 23
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 24
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 25
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 26
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 27
                  :question "XXX"
                  :domain-key :A
                  :reversed? true}
                 {:number 28
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 29
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 30
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 31
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 32
                  :question "XXX"
                  :domain-key :A
                  :reversed? false}
                 {:number 33
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 34
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 35
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 36
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 37
                  :question "XXX"
                  :domain-key :A
                  :reversed? true}
                 {:number 38
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 39
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 40
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 41
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 42
                  :question "XXX"
                  :domain-key :A
                  :reversed? false}
                 {:number 43
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
                 {:number 44
                  :question "XXX"
                  :domain-key :E
                  :reversed? true}
     ]}))


