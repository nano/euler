(use '[euler :only [run]])

(defn p067 [file]
  (let [content  (slurp file)
        lines    (clojure.string/split content #"\n")
        to-int   #(Integer/parseInt %)
        triangle (map #(map to-int (clojure.string/split % #" ")) lines)]
    (first (reduce (fn [a b]
                     (map #(+ (nth b %) (apply max (subvec (vec a) % (+ 2 %))))
                          (range 0 (count b))))
                   (reverse triangle)))))


(run (p067 "data/p067.txt"))
