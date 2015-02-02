(use '[euler :only [run factorize]])

(defn p003 [n]
  (apply max (factorize n)))

(run (p003 600851475143))
