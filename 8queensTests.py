# -*- coding: utf-8 -*-
"""
Email: parssataghipour@gmail.com
@author: SF1917
"""

import unittest
import datetime
import genetic

class EightQueensTests(unittest.TestCase):
    def test(self, size=8):
        geneset = [i for i in range(size)]
        startTime = datetime.datetime.now()
        
        def fnDisplay(candidate):
            display(candidate, startTime, size)
            
        def fnGetFitness(genes):
            return get_fitness(genes, size)
        
        optimalFitness = Fitness(0)
        best = genetic.get_best(fnGetFitness, 2 * size, 
                                optimalFitness, geneset, fnDisplay)
        self.assertTrue(not optimalFitness > best.Fitness)
    '''    
    def test_benchmark(self):
        genetic.Benchmark.run(lambda: self.test(20))'''
        
        
class Board:
    def __init__(self, genes, size):
        board = [['.'] * size for _ in range(size)] 
        for index in range(0, len(genes), 2):
            row = genes[index]
            column = genes[index + 1]
            board[column][row] = 'Q' 
        self._board = board
    
    def print(self):
        for i in reversed(range(0, len(self._board))):
            print(' '.join(self._board[i]))
            
    def get(self, row, column):
        return self._board[column][row]        
        
def display(candidate, startTime, size):
    timeD = datetime.datetime.now() - startTime
    board = Board(candidate.Genes, size)
    board.print()
    print("{0}\t- {1}\t{2}".format(
            ' '.join(map(str, candidate.Genes)),
            candidate.Fitness,
            str(timeD)))
    
    
class Fitness:
    Total = None

    def __init__(self, total):
        self.Total = total
        
    def __gt__(self, other):
        return self.Total < other.Total
    
    def __str__(self):
        return "{0}".format(self.Total)
    
def get_fitness(genes, size):
    board = Board(genes, size)
    rowsWithQueens = set()
    colsWithQueens = set()
    northEastDiagonalsWithQueens = set()
    southEastDiagonalsWithQueens = set()
    for row in range(size):
        for col in range(size):
            if board.get(row, col) == 'Q':
                rowsWithQueens.add(row)
                colsWithQueens.add(col)
                northEastDiagonalsWithQueens.add(row + col)
                southEastDiagonalsWithQueens.add(size - 1 - row + col)
                
    total = size - len(rowsWithQueens) \
            + size - len(colsWithQueens) \
            + size - len(northEastDiagonalsWithQueens) \
            + size - len(southEastDiagonalsWithQueens)

    return Fitness(total)            
                
if __name__ == "__main__":
    unittest.main()                 
                
        
    
   
    
    
    























        