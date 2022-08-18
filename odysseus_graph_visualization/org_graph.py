from distutils.command.build import build
import logging

import graphviz

from odysseus_graph_visualization.sheets import get_organization_data

logger = logging.getLogger(__name__)


def build_org_graph(
    org_data,
    ignore_nodes=[
        "None",
        "Other",
        "None (Dynasty)",
        "None (Politics)",
        "None (Ship)",
        "Unknown ship",
    ],
):
    graph = graphviz.Digraph()

    for edge in org_data:
        if edge.get("From Type") != "Character":
            logger.warning("Did not understand edge: %s", org_data)
            continue

        if edge["To Name"] in ignore_nodes:
            continue

        graph.edge(edge["From Name"], edge["To Name"])

    return graph


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    graph = build_org_graph(get_organization_data())
    print(graph.source)
