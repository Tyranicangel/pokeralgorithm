# Winning Poker Hand
  - Main
  - Generator
  - TestCaseGenerator

### Main
  - Create a csv file in the given format
  - Run main.py with the filename excluding the extension as a parameter
  - Use Python version 2.x

CSV File Format:
  - Use comma as the delimiter
  - First row must contain the word table followed by the cards on the table
  - Next rows correspond to playername, bet amount and their cards

For example:
Table,AD,TS,AC,9H,JS
Player1,1000,2D,7S
Player2,2000,5S,3D

### Generator

The algorithm requires hands.json which serves as a look-up. If you dont find the file in the current folder run generator.py using python 2.x.

### TestCaseGenerator

Use testCaseGenerator.py followed by filename to generate a sample test case with 9 players and random cards and bet amount in the correct file format. You can see a csv file with the filename once you run.