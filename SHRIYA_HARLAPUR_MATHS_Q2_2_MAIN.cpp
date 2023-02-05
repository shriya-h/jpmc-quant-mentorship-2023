/**
 * @file q2_2.cpp
 * @author Shriya Harlapur, IIT Kharagpur
 * @brief calculating the maximum payoff for each possible configuration of a deck consisting of 4 red and 4 black cards
 * @date 2023-01-26
 */

#include <bits/stdc++.h>
using namespace std;

void printvec(vector<int> vec)
{
    for (int i = 0; i < vec.size(); ++i)
    {
        if (vec[i])
            cout << "R ";
        else
            cout << "B ";
    }
}

int payoff(vector<int> deck)
{
    // current payoff after each card is pulled from the deck, maximum payoff possible for the deck
    int curr_score = 0, max_score = 0;
    for (int i = 0; i < deck.size(); ++i)
    {
        if (deck[i] == 1)
            curr_score += 1;
        else
            curr_score -= 1;

        max_score = max(max_score, curr_score);
    }

    return max_score;
}

// function to calculate factorial of a number n
int factorial(int n)
{
    if (n == 0)
        return 1;
    int prod = 1;
    for (int i = 1; i <= n; ++i)
        prod *= i;
    return prod;
}

bool next_perm(vector<int> &vec)
{
    int n = vec.size();
    // Find the largest index i for which vec[i-1] is strictly less that vec[i]
    int i = n - 1;
    while (vec[i - 1] >= vec[i])
    {
        // if i is the first index of the vector, we are already at the last possible permutation because the vector is in reverse sorted order
        if (--i == 0)
        {
            return false; // next permutation is not possible
        }
    }

    // At this point, vec[i,...,n-1] is in sorted order
    // Now we find the greatest index j such that s[j] > s[i-1]
    int j = n - 1;
    while (j > i && vec[j] <= vec[i - 1])
    {
        j--;
    }

    // swap element at index i-1 with element at index j
    swap(vec[i - 1], vec[j]);

    // Reverse subarray vec[i…n-1] and return true
    reverse(vec.begin() + i, vec.end());

    return true; // it is possible to generate the next permutation
}

int main()
{
    // black cards are represented by 0, red cards are represented by 1
    vector<int> deck = {0, 0, 0, 0, 1, 1, 1, 1};

    // total number of cards
    int len = deck.size();

    // total maximum payoff for all permutations and maximum payoff for current permutation
    int total_payoff = 0, curr_payoff = 0;

    cout << "Configuration   | Payoff" << endl;
    cout << "------------------------" << endl;
    do
    {
        // print permutation
        printvec(deck);
        cout << "|   ";
        // calculate and print payoff
        curr_payoff = payoff(deck);
        total_payoff += curr_payoff;
        cout << curr_payoff << endl;
    } while (next_perm(deck));

    // calculating total number of permutations
    int num_perm = factorial(len) / (factorial(len / 2) * factorial(len / 2));

    cout << "------------------------" << endl;
    cout << "Average maximum payoff is: " << 1.0 * total_payoff / num_perm << endl;

    return 0;
}
