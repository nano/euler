(use '[euler :only [run]])

(defn triplet? [[a b c]]
  (= (* c c) (+ (* a a) (* b b))))

(defn p009 [sum]
  (first (map #(reduce * %)
              (filter triplet?
                      (for [c (range 2 sum)
                            b (range 1 c)]
                        (let [a (- sum b c)]
                          [a b c]))))))

(run (p009 1000))
