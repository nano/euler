(use '[euler :only [run]])

(def fib-seq
  ((fn rfib [a b]
     (lazy-seq (cons a (rfib b (+ a b)))))
     1 1))

(defn p002 [max]
  (reduce + (filter #(even? %)
                    (take-while #(<= % max) fib-seq))))

(run (p002 4000000))
