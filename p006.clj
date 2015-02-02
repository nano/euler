(use '[euler :only [run]])

(defn p006 [n]
  (let [r (range (+ n 1))]
    (long (- (Math/pow (reduce + r) 2)
          (reduce + (map #(Math/pow % 2) r))))))

(run (p006 100))
