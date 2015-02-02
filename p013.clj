(use '[euler :only [run]])

(defn p013 [file]
  (let [content (slurp file)
        lines   (clojure.string/split content #"\n")]
    (subs (str (reduce + (map bigint lines))) 0 10)))

(run (p013 "data/p013.txt"))
