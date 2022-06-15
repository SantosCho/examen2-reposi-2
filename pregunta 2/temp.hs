
 fibo :: Int -> Int
 fibo 1 = 1
 fibo 2 = 1
 fibo n = fibo (n-1) + fibo (n-2)
 
 fc :: Int -> Int 
 fc = \a -> fibo(a)


 main = do
  print "ingrese los valor :"
  x <- getLine
  putStr "El resultado de la fibo temporal: "
  print $ (fc (read x))