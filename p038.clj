(use '[euler :only [run]])

(defn concat-product [n fs]
  (Long. (reduce str "" (map #(* n %) fs))))

(defn concat-products [n]
  (for [x (drop 2 (range))
        :let [fs (vec (range 1 x))
              cp (concat-product n fs)]
        :while (<= cp 987654321)]
    cp))

(defn digits [n]
  (map #(mod (int (/ n (Math/pow 10 %))) 10)
       (range (int (/ (Math/log n) (Math/log 10))) -1 -1)))

(defn pandigital? [n l]
  (let [d (digits n)]
    (if (= (count d) l)
      (not (nil? (reduce (fn [a b]
                           (if (nil? a)
                             nil
                             (if (= a (dec b))
                               b
                               nil)))
                         (sort d))))
      false)))

(defn p038 []
  (->>
    (range 2 10001)
    (map concat-products)
    flatten
    (filter #(pandigital? % 9))
    (apply max)))

(run (p038))
