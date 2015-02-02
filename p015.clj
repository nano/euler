(use '[euler :only [run pascal-triangle]])

(defn p015 [size]
  (nth (last (take (inc (* 2 size)) pascal-triangle)) size))

(run (p015 20))
