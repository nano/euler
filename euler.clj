(ns euler)

(defmacro run
  [& body]
  `(let [start-time# (System/nanoTime)
         result#     ~@body
         end-time#   (System/nanoTime)
         diff-time#  (/ (- end-time# start-time#) 1e6)]
     (println result#)
     (println diff-time# "msec")))

(defn gcd [a b]
  (if (= b 0)
    a
    (gcd b (mod a b))))

(defn lcm [a b]
  (/ (* a b) (gcd a b)))

(def primes
  (concat
    [2 3]
    (lazy-seq
      (let [f (fn f [n]
                (if (some zero? (map (partial mod n)
                                     (take-while #(<= (* % %) n)
                                                 primes)))
                  (recur (+ n 2))
                  (lazy-seq (cons n (f (+ n 2))))))]
        (f 5)))))

(defn factorize [n]
  (if (= 1 n)
    [1]
    (let [f (fn f [x]
              (let [d (first (filter #(zero? (mod x %)) primes))
                    q (/ x d)]
                (lazy-seq (if (> q 1)
                            (cons d (f q))
                            [d]))))]
      (f n))))

(defn totient [n]
  (int (reduce * (map (fn [[n e]] (* (dec n) (Math/pow n (dec e))))
                      (reduce (fn [a b]
                                (if-let [x (a b)]
                                  (assoc a b (inc x))
                                  (assoc a b 1)))
                              {}
                              (factorize n))))))

(defn number-of-divisors [n]
  (reduce * (map (fn [[_ e]] (inc e))
                 (reduce (fn [a b]
                           (if-let [x (a b)]
                             (assoc a b (inc x))
                             (assoc a b 1)))
                         {}
                         (factorize n)))))

(def pascal-triangle
  ((fn f [t]
     (let [t' (concat [1]
                      (map #(+ (nth t %) (nth t (inc %))) (range 0 (dec (count t))))
                      [1])]
       (lazy-seq (cons t (f t')))))
     [1]))
