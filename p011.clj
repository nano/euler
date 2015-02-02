(use '[euler :only [run]])

(defn horizontals [rows size]
  (let [f (fn [row] (map #(subvec (vec row) % (+ % 4))
                         (range (- size 3))))]
    (reduce into (map f rows))))

(defn verticals-in-col [rows col size]
  (let [f (fn [i] (map #(nth (nth rows %) col)
                       (range i (+ i 4))))]
    (map f (range (- size 3)))))

(defn verticals [rows size]
  (reduce into (map #(verticals-in-col rows % size)
                    (range size))))

(defn diagonal [rows size x y dir]
  (map #(nth (nth rows (+ y %)) (+ x (* % dir)))
       (range 4)))

(defn right-diagonals [rows size]
  (let [f (fn [i] (map #(diagonal rows size % i 1)
                       (range (- size 3))))]
    (reduce into (map f (range (- size 3))))))

(defn left-diagonals [rows size]
  (let [f (fn [i] (map #(diagonal rows size % i -1)
                       (range 3 size 3)))]
    (reduce into (map f (range (- size 3))))))

(defn p011 [file size]
  (let [content (slurp file)
        numbers (map #(Integer/parseInt %) (clojure.string/split content #"\s+"))
        rows    (partition size numbers)
        fours   (reduce into [(verticals rows size)
                              (horizontals rows size)
                              (right-diagonals rows size)
                              (left-diagonals rows size)])
        prods   (map #(reduce * %) fours)]
    (apply max prods)))

(run (p011 "data/p011.txt" 20))
