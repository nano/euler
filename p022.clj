(use '[euler :only [run]])

(defn value [name]
  (reduce + (map #(inc (- (int %) (int \A))) name)))

(defn p022 [file]
  (let [content (clojure.string/replace (slurp file) "\"" "")
        names   (sort (clojure.string/split content #","))
        values  (map value names)]
    (reduce + (map #(* (inc %) (nth values %)) (range (count values))))))

(run (p022 "data/p022.txt"))
