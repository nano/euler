(use '[euler :only [run]])

(defn digit-sum [n]
  (reduce + (map #(- (int %) (int \0)) (str n))))

(defn p020 [n]
  (digit-sum (reduce * (map bigint (range 2 (inc n))))))

(run (p020 100))
