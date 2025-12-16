# About the **Largest prime factor** solution

## Brute force method

> [!WARNING]
>
> The penalty of this method is that it requires a large number of iterations as
> the number grows.

The first solution, using the algorithm taught in school, is:

> Start by choosing a number $ i $ starting with $ 2 $ (the smallest prime number)
> Test the divisibility of the number $ n $ by $ i $, next for each one:
>
>> - If $ n $ is divisible by $ i $, then the result is
>> the new number $ n $ is reduced, while at the same time
>> the largest number $i$ found is stored.
>>
>> - If $ n $ IS NOT divisible by $ i $, $i$ is incremented by 1
> up to $ n $.
>
> Finally:
>>
>> - If you reach the end without finding any, it is because the number $n$
>> is prime and would be the only factual prime it has.
>>
>> - Otherwise, then the largest number $i$ found would be the largest prime factor.

## Second approach, limiting to half iterations

> [!CAUTION]
>
> Using some test entries, quickly broke the solution at all. So, don't use it.
> This note is just to record the failed idea.

Since by going through and proving the divisibility of a number $ i $ up to
$ n $
there are also "remainder" numbers that are also divisible by their opposite,
let's call it $ j $.

At first it seemed attractive to test numbers $ i $ up to half of $ n $ then
test whether $ i $ or $ j $ are prime. 2 problems arise:

- Testing whether a number is prime could involve increasing the number of
iterations since now the problem would become O(N^2) complex in the worst cases

- Discarding all $ j $ could mean discarding the correct solution.

Both problems were detected when using different sets of test inputs.

## Final solution using some optimization

> [!WARNING]
>
> No source was found with a mathematical proof proving that the highest prime
> factor of a number n (non-prime) always lies under the limit of $ \sqrt{n} $

A solution apparently accepted in the community as an optimization of the first
brute force algorithm consists of limiting the search to $ \sqrt{n} $.

Apparently it is a mathematical conjecture without proof
(if it exists, please send it to me).

Found the correct result in all test cases.
