from mock import MagicMock

from remotespark.datawidgets.plotlygraphs.graphrenderer import GraphRenderer
from remotespark.datawidgets.encoding import Encoding


def test_support_all_graph_types():
    renderer = GraphRenderer(testing=True)

    for chart_type in Encoding.supported_chart_types:
        graph = renderer._get_graph(chart_type)
        assert graph is not None
        getattr(graph, "render")
        getattr(graph, "display_x")
        getattr(graph, "display_y")
        getattr(graph, "display_logarithmic_x_axis")
        getattr(graph, "display_logarithmic_y_axis")


def test_display_controls():
    renderer = GraphRenderer(testing=True)

    GraphRenderer.display_x = MagicMock(return_value=True)
    GraphRenderer.display_y = MagicMock(return_value=True)
    assert renderer.display_controls(Encoding.chart_type_line)

    GraphRenderer.display_x = MagicMock(return_value=True)
    GraphRenderer.display_y = MagicMock(return_value=False)
    assert renderer.display_controls(Encoding.chart_type_line)

    GraphRenderer.display_x = MagicMock(return_value=False)
    GraphRenderer.display_y = MagicMock(return_value=True)
    assert renderer.display_controls(Encoding.chart_type_line)

    GraphRenderer.display_x = MagicMock(return_value=False)
    GraphRenderer.display_y = MagicMock(return_value=False)
    assert not renderer.display_controls(Encoding.chart_type_line)
