(use '[euler :only [run lcm]])

(defn p005 [n]
  (reduce lcm (range 2 (+ n 1))))

(run (p005 20))
