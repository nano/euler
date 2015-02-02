(use '[euler :only [run]])

(defn p008 [file]
  (let [content    (slurp file)
        nstr       (clojure.string/replace content #"[^0-9]" "")
        partitions (map #(subs nstr % (+ % 5)) (range (- (count nstr) 4)))
        make-prod  (fn [partition]
                     (reduce * (map #(- % (int \0)) (map int partition))))
        prods      (map make-prod partitions)]
    (apply max prods)))

(run (p008 "data/p008.txt"))
