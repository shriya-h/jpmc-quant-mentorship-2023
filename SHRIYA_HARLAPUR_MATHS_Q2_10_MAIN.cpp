/**
 * @file q2_10.cpp
 * @author Shriya Harlapur, IIT Kharagpur
 * @brief calculating the expected payoff value in a deck of 26 red and 26 black cards
 * @date 2023-01-27
 */

#include <bits/stdc++.h>
using namespace std;

/* function to find the probability of k being the payoff of a randomly chosen configuration of the deck */
double findprob(double f, int n, int k)
{
    return f * (2 * k + 1) / (n + k + 1);
}

int main()
{
    int n = 26;             // half the number of cards in the deck, i.e. the number of black and red cards each
    double f = 1.0;         // the value of f_k at each iteration
    int k = 0;              // the iteration number which represents every possible payoff value, which goes from 0 to n
    double exp_pay = 0.0;   // expected payoff

    do
    {
        exp_pay += k * findprob(f, n, k); // updating expected payoff
        ++k;                              // incrementing the payoff value
        f = f * (n - k + 1) / (n + k);    // finding the new value of f_k

    } while (k <= n);

    cout << "Expected payoff for a " << 2 * n << " card deck: " << exp_pay << endl;

    return 0;
}