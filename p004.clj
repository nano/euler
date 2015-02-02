(use '[euler :only [run]])

(defn palindrome? [n]
  (let [s (str n)]
    (= s (clojure.string/reverse s))))

(defn products [digits]
  (for [a (range (Math/pow 10 (- digits 1)) (Math/pow 10 digits))
        b (range (Math/pow 10 (- digits 1)) (Math/pow 10 digits))]
    (int (* a b))))

(defn p004 [digits]
  (apply max (filter palindrome? (products digits))))

(run (p004 3))
