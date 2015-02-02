(use '[euler :only [run primes]])

(defn p010 [n]
  (reduce + (take-while #(< % n) primes)))

(run (p010 2e6))
