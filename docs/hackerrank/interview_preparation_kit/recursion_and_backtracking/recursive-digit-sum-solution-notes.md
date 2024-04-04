# [Recursive Digit Sum](https://www.hackerrank.com/challenges/recursive-digit-sum)

- Difficulty:  `#medium`
- Category: `#ProblemSolvingBasic`

## Language Difficulties

The first attempt solved most of the cases.
The failed test cases reported a "Runtime error".
Initially, it seemed pointless, since there are
no edge cases in the calculations that could cause
typical runtime errors like division by zero or
performing operations on a null value.

Unlocking a failed test case, and locally replicating the given input,
found the real problem:

```text
ValueError: Exceeds the limit (4300) for integer string conversion
```

The input number is too high for some reason in Python.

A [little reseach](https://stackoverflow.com/a/75162528/6366150) give some answers:

### Problem fixes

So, the problem arises from a limitation imposed in Python, which fixes
the size of a number that will be transformed from a string to an integer.

The limit can be increased via a parameter or programmatically.
However, if the value is set as a hardcoded integer (in test cases),
it will still fail at runtime.

> [!IMPORTANT]
>
> The solution is then to enter the number (from the large test case)
> as a string and then do the transformation at runtime,
> including the parameter that arbitrarily extends the length of the number.

## Sources

- [Stackoverflow: ValueError: Exceeds the limit (4300) for integer string conversion](https://stackoverflow.com/a/75162528/6366150)
- [CVE: CVE-2020-10735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10735)
- [Multiline String in Python - GeeksforGeeks](https://www.geeksforgeeks.org/multiline-string-in-python/)
- [string splitterworld's simplest string tool](https://onlinestringtools.com/split-string)
