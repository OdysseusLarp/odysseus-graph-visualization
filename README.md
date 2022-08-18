# Odysseus graph visualization

This is an experiment for visualizing relations between factions and characters using [GraphViz](https://graphviz.org/).

## Getting started

Requirements:

* Python 3 (tested: 3.10)
* Graphviz (mac: `brew install graphviz`)
* Google OAuth credentials in a file called `credentials.json` (see [getting started](https://developers.google.com/sheets/api/quickstart/python) and [creating credentials](https://developers.google.com/workspace/guides/create-credentials))

Install deps and run the example:

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python -m odysseus_graph_visualization.org_graph > org_graph.dot
    sfdp -x -Goverlap=scale -Tpng -O org_graph.dot
    open org_graph.dot.png
