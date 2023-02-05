
/**
 * @file q2_8.cpp
 * @author Shriya Harlapur, IIT Kharagpur
 * @brief calculating the probability of each payoff value in a deck of 26 red and 26 black cards
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
    cout << "k  | P(X=k)" << endl;
    cout << "----------------" << endl;

    int n = 26;     // half the number of cards in the deck, i.e. the number of black and red cards each
    double f = 1.0; // the value of f_k at each iteration
    int k = 0;      // the iteration number which represents every possible payoff value, which goes from 0 to n

    do
    {
        cout << k << " ";
        if (k <= 9)
            cout << " ";
        cout << "| " << findprob(f, n, k) << endl;  // printing the probability of the current payoff
        ++k;                                        // incrementing the payoff value
        f = f * (n - k + 1) / (n + k);              // finding the new value of f_k

    } while (k <= n);

    cout << "----------------" << endl;

    return 0;
}