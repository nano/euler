(use '[euler :only [run number-of-divisors]])

(def triangulars
  ((fn f [n i] (lazy-seq (cons n (f (+ n i) (inc i))))) 1 2))

(defn p012 [n]
  (first (filter #(> (number-of-divisors %) n)
                 triangulars)))

(run (p012 500))
