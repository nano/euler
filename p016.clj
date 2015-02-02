(use '[euler :only [run]])

(defn p016 [b e]
  (reduce + (map #(- (int %) (int \0))
                 (str (reduce * (take 1000
                                      (cycle [(bigint 2)])))))))

(run (p016 2 1000))
