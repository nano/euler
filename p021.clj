(use '[euler :only [run factorize]])

(defn divisors-sum [n]
  (- (int (reduce * (map (fn [[x e]]
                           (/ (dec (Math/pow x (inc e)))
                              (dec x)))
                         (reduce (fn [a b]
                                   (if-let [x (a b)]
                                     (assoc a b (inc x))
                                     (assoc a b 1)))
                                 {}
                                 (factorize n)))))
     n))

(defn ^boolean amicable? [n]
  (let [d  (divisors-sum n)
        d' (divisors-sum d)]
    (and (not (= d n))
         (= n d'))))

(defn p021 [n]
  (reduce + (filter amicable? (range 2 n))))

(run (p021 10000))
