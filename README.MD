# Graph Connectivity Checker

## Overview

Welcome to the Graph Connectivity Checker project! This tool helps you parse, analyze, and check the connectivity of graph data. Whether you're working with large datasets or generating random graphs for testing, this project has you covered.

## Project Structure

Here's a quick rundown of the project files:

```
├── LICENSE
├── README.MD
├── decorators.py
├── graph_parser.py
├── main.py
├── requirements.txt
├── sample_filepaths.py
└── sample_graph_generator.py
```

### File Descriptions

- **`decorators.py`**: Contains helpful decorators for measuring execution time and handling errors in a colorful and informative way.
- **`graph_parser.py`**: This is where the magic happens. The `GraphParser` class reads and processes graph files, extracting nodes and edges to build a comprehensive graph structure.
- **`main.py`**: The heart of the project. This script ties everything together, running the graph parsing and connectivity checks.
- **`requirements.txt`**: This file is currently empty as all required packages are part of Python's standard library.
- **`sample_filepaths.py`**: A template for specifying the path to your dataset. Rename this to `filepaths.py` and set the `DATASET_PATH` variable.
- **`sample_graph_generator.py`**: A handy tool for generating random graphs, perfect for testing.

## Getting Started

### Prerequisites

Before you start, make sure you have Python 3.x installed. Since all the packages used are part of the Python standard library, you don't need to install any additional packages.

### Setting Up Your Dataset

1. **Rename the File**:
   - Rename `sample_filepaths.py` to `filepaths.py`.

2. **Set the Dataset Path**:
   - Open `filepaths.py` and set the `DATASET_PATH` variable to the location of your graph files.

### Running the Project

1. **Launch the Main Script**:

```sh
python main.py
```

2. **Provide Dataset Details**:
   - Choose `1` to create a new graph with specified nodes and edges, or choose `2` to use a prepared graph from files.
   - If creating a new graph, enter the number of nodes and edges.
   - If using a prepared graph, provide the path to the folder containing the graph files and their names.

### Example Output

When you run the script, you might see something like this:

```sh
Enter your choice:
1. Create a new graph
2. Use a prepared graph
Choice: 1
Enter the number of nodes for the new graph: 50
Enter the number of edges for the new graph: 100
Generated graph with 50 nodes and 100 edges.
The graph is connected.
```

If your graph isn't connected (when using a prepared graph), it will list the connected components for you.

## How It Works

### `decorators.py`

We have two decorators here:
- **`measure_time`**: Logs how long each function takes to execute.
- **`handle_errors`**: Catches and logs errors, so you know exactly what's going wrong and where.

### `graph_parser.py`

This file defines the `GraphParser` class. It:
- **Finds and reads your graph files**: Looks for coordinate and edge files in your dataset.
- **Parses the data**: Extracts nodes and edges, turning them into a usable graph structure.
- **Combines graphs**: Merges different types of graphs (coordinates, distances, travel times) into a unified format.

### `main.py`

The main script does the heavy lifting:
- **Reads user's choice**: Based on the choice (`1` for new graph, `2` for prepared graph), it either generates a random graph or loads and parses a graph from files.
- **Connectivity Check**: Uses `GraphConnectivityChecker` to check if the graph is connected. If not, it identifies and lists the connected components.

### `sample_graph_generator.py`

This script can generate random graphs for testing. You can specify the number of nodes and edges, and it will create a graph with random connections and weights.

## Graph Data Sources

This project was developed using graph data from the [9th DIMACS Implementation Challenge - Shortest Paths](https://www.diag.uniroma1.it/challenge9/download.shtml). You can test the project with graphs from this site, generate new graphs using the `sample_graph_generator.py`, or use any other graph dataset you have.

## License

This project is licensed under the MIT License. For more details, see the `LICENSE` file.

---

That's it! Dive in, explore the code, and feel free to contribute. Whether you're analyzing real-world data or just playing around with generated graphs, we hope you find this project useful and fun. Happy graphing!