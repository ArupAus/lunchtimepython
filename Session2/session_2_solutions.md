# Session 2: Basics Part B

## How Long is a String

```py
def longer_string(string1, string2):
	if len(string1) >= len(string2):
		return string1
	return string2
```

## Printing Triangles

```py
def build_triangle(height):
	triangle = ''
	for i in range(height):
		triangle += '*'*(i+1)+'\n'
	return triangle.strip('\n')
```

## Multiples of 3 or 5

```py
def sum_multiples(n):
    return sum(i for i in range(n) if i%3==0 or i%5==0)
```

## Prime Numbers

```py
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True 
```
