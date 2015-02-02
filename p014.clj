(use '[euler :only [run]])

(def results (ref {}))

(defn add-to-cache [n c]
  (dosync
    (alter results assoc n c)))

(defn collatz
  ([n] (collatz n n 1))
  ([n n' c]
    (if (= 1 n')
      (do
        (add-to-cache n c)
        c)
      (if-let [r (@results n')]
        (let [c' (+ c r)]
          (add-to-cache n c')
          c')
        (recur
          n
          (if (odd? n')
            (inc (* 3 n'))
            (bit-shift-right n' 1))
          (inc c))))))

(defn p014 [n]
  (->>
    (map (fn [x] [x (collatz x)]) (range 1 n))
    (sort-by last)
    last
    first))

(run (p014 1e6))
