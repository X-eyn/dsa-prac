def is_prime(n):
  p=False

  if n==1:
    p=False

  else:

    for i in range (2,n):
      if n%i==0:
        p=False
        break
    else:
      p=True

  return(p)
  