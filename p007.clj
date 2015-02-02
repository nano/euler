(use '[euler :only [run primes]])

(defn p007 [n]
  (first (drop (- n 1) primes)))

(run (p007 10001))
