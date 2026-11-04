using System;
using Library;

public class Program
{
    public static void Main()
    {
        Console.Write("Enter the 1 matrix size (number of vertices): ");
        int size;
        while (true)
        {
            string? input = Console.ReadLine();
            if (input == null)
                return;

            if (int.TryParse(input, out size) && size > 0)
                break;

            Console.Write("Enter a positive integer: ");
        }

        int[,] matrix1 = GraphMethods.Generate.Matrix(size);
        int[,] matrix2 = GraphMethods.Generate.Matrix(size);
        var list1 = GraphMethods.Generate.GraphList(matrix1);
        var list2 = GraphMethods.Generate.GraphList(matrix2);

        Console.WriteLine("\nAdjacency matrix of graph G1:");
        GraphMethods.Print.Matrix(matrix1);
        Console.WriteLine("Adjacency lists of graph G1:");
        GraphMethods.Print.GraphList(list1);

        Console.WriteLine("\nAdjacency matrix of graph G2:");
        GraphMethods.Print.Matrix(matrix2);
        Console.WriteLine("Adjacency lists of graph G2:");
        GraphMethods.Print.GraphList(list2);

        Console.WriteLine("\nTask 2.1: operations on G1 (vertex numbers start at 0).");

        Console.WriteLine("\nIdentify vertices:");
        if (!ReadVertex("First vertex: ", out int vertex1) ||
            !ReadVertex("Second vertex: ", out int vertex2))
            return;

        int[,] result = GraphOperations.IdentifyVertices(matrix1, vertex1, vertex2, out bool err);
        if (err)
            Console.WriteLine("Error");
        else
            GraphMethods.Print.Matrix(result);

        Console.WriteLine("\nContract an edge:");
        if (!ReadVertex("First vertex: ", out vertex1) ||
            !ReadVertex("Second vertex: ", out vertex2))
            return;

        result = GraphOperations.ContractEdge(matrix1, vertex1, vertex2, out err);
        if (err)
            Console.WriteLine("Error");
        else
            GraphMethods.Print.Matrix(result);

        Console.WriteLine("\nSplit a vertex:");
        if (!ReadVertex("Vertex: ", out int vertex))
            return;

        result = GraphOperations.SplitVertex(matrix1, vertex, out err);
        if (err)
            Console.WriteLine("Error");
        else
            GraphMethods.Print.Matrix(result);

        bool ReadVertex(string text, out int value)
        {
            Console.Write(text);
            while (true)
            {
                string? input = Console.ReadLine();
                if (input == null)
                {
                    value = 0;
                    return false;
                }

                if (int.TryParse(input, out value) && value >= 0 && value < size)
                    return true;

                Console.Write($"Enter a vertex number from 0 to {size - 1}: ");
            }
        }
    }
}

