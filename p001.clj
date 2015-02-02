(use '[euler :only [run]])

(defn p001 [n]
  (reduce + (filter #(or (zero? (mod % 3))
                         (zero? (mod % 5))) (range n))))

(run (p001 1000))
