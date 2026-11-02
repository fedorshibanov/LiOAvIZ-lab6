using System;
using System.Collections.Generic;

namespace Library
{    
    public static class GraphMethods
    {
        public static class Print
        {
            public static void Matrix(int[,] matrix)
            {
                for (int i = 0; i < matrix.GetLength(0); i++)
                {
                    for (int j = 0; j < matrix.GetLength(1); j++)
                    {
                        if (j > 0)
                            Console.Write(" ");
                        Console.Write(matrix[i, j]);
                    }
                    Console.WriteLine();
                }
            }

            public static void GraphList(List<int>[] list)
            {
                for (int i = 0; i < list.Length; i++)
                {
                    Console.WriteLine($"{i}: {string.Join(", ", list[i])}");
                }
            }
        }

        public static class Generate
        {
            public static int[,] Matrix(int size)
            {
                int[,] matrix = new int[size, size];

                for (int i = 0; i < size; i++)
                {
                    for (int j = i; j < size; j++)
                    {
                        int value = Random.Shared.Next(2);
                        matrix[i, j] = value;
                        matrix[j, i] = value;
                    }
                }

                return matrix;
            }

            public static List<int>[] GraphList(int[,] matrix)
            {
                int size = matrix.GetLength(0);
                List<int>[] list = new List<int>[size];

                for (int i = 0; i < size; i++)
                {
                    list[i] = new List<int>();
                    for (int j = 0; j < size; j++)
                    {
                        if (matrix[i,j] == 1)
                            list[i].Add(j);
                    }
                }

                return list;
            }
        }
    }

    public static class GraphOperations
    {
        public static int[,] IdentifyVertices(int[,] matrix, int vertex1, int vertex2, out bool err)
        {
            err = DefaultCheck(matrix, vertex1, vertex2);
            if (err) 
                return matrix;

            int size = matrix.GetLength(0)-1;
            int [,] newMatrix = new int[size, size];

            int counter = 1;
            for (int i = 0; i < size+1; i++)
            {
                if (i == vertex1 || i == vertex2)
                {
                    int column = 1;
                    for (int j = 0; j < size+1; j++)
                    {
                        int newColumn = (j == vertex1 || j == vertex2) ? 0 : column++;
                        newMatrix[0, newColumn] = matrix[i, j] == 1 ? 1 : newMatrix[0, newColumn];
                        newMatrix[newColumn, 0] = newMatrix[0, newColumn];
                    }
                }
                else
                {
                    int column = 1;
                    for (int j = 0; j < size+1; j++)
                    {
                        if (j == vertex1 || j == vertex2)
                            continue;

                        int newColumn = column++;
                        newMatrix[counter, newColumn] = matrix[i, j];
                        newMatrix[newColumn, counter] = matrix[j, i];
                    }

                    counter++;
                }
            }

            err = false;
            return newMatrix;
        }

        public static int[,] ContractEdge(int[,] matrix, int vertex1, int vertex2, out bool err)
        {
            err = DefaultCheck(matrix, vertex1, vertex2);
            if (err) 
                return matrix;
            else if(matrix[vertex1, vertex2] == 0)
            {
                err = true;
                return matrix;
            }

            int[,] newMatrix = IdentifyVertices(matrix, vertex1, vertex2, out err);

            if (err)
                return matrix;
            
            newMatrix[0, 0] = 1;

            return newMatrix;
        }

        public static int[,] SplitVertex(int[,] matrix, int vertex, out bool err)
        {
            int size = matrix.GetLength(0)+1;
            
            if (vertex < 0 || vertex >= size-1)
            {
                err = true;
                return matrix;
            }

            int[,] newMatrix = new int[size, size];

            for (int i = 0;i < size-1; i++)
            {
                for (int j = i;j < size-1; j++)
                {
                    newMatrix[i, j] = matrix[i, j];
                    newMatrix[j, i] = matrix[j, i];
                }

                if (i == vertex)
                {
                    for (int j = 0;j < size-1; j++)
                    {
                        newMatrix[size-1, j] = matrix[i, j];
                        newMatrix[j, size-1] = matrix[j, i];
                    }

                    newMatrix[vertex, size-1] = 1;
                    newMatrix[size-1, vertex] = 1;
                }
            }

            err = false;
            return newMatrix;
        }
        
        private static bool DefaultCheck(int[,] matrix, int vertex1, int vertex2)
        {
            if (vertex1 < 0 || vertex1 >= matrix.GetLength(0) ||
                vertex2 < 0 || vertex2 >= matrix.GetLength(0) ||
                vertex1 == vertex2)
            {
                return true;
            }

            return false;
        }
    }
}
