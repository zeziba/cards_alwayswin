[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/zeziba/cards_alwayswin.svg?branch=master)](https://travis-ci.org/zeziba/cards_alwayswin)



This is a game to show a algorithm that allows the house to always win.

This module will simulate random chance using poker dice.

Using https://en.wikipedia.org/wiki/Poker_dice as a template for the probabilities
I have created a game that the house always wins. Currently there is only one roll
to determine if you have a winning hand. This decreases the chances of getting a five of a kind
dramatically.

Using this simple algorithm I have demonstrated that it is a simple matter of
generating something where the house will win frequently but there is enough incentive
for a player to keep hitting go again.

With the simple values returned with the hand, we can use the value returned to give
out prizes based on that value. With anything 3(Three of a kind) or lower only giving marginally
good prizes and the rest giving gifts that are magnitudes better than the last.
This ensures that there is always incentive to roll again but the odds of getting the best prizes
are marginal at best ensuring the player does not feel ripped off.
