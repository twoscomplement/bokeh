import unittest

import bokeh.plotting as plt
from ..models import (Grid, LinearAxis, PanTool, BoxZoomTool, LassoSelectTool,
                      PanTool, PreviewSaveTool, ResetTool, ResizeTool)

class TestPlotting(unittest.TestCase):

    def test_reset_output(self):
        plt._default_document = 10
        plt._default_session = 10
        plt._default_file = 10
        plt._default_notebook = 10
        plt.reset_output()
        self.assertTrue(isinstance(plt._default_document, plt.Document))
        self.assertEqual(plt._default_session, None)
        self.assertEqual(plt._default_file, None)
        self.assertEqual(plt._default_notebook, None)

    def test_figure(self):
        p = plt.figure()
        q = plt.figure()
        q.circle([1,2,3], [1,2,3])
        self.assertNotEqual(p, q)
        r = plt.figure()
        self.assertNotEqual(p, r)
        self.assertNotEqual(q, r)

    def test_xaxis(self):
        p = plt.figure()
        p.circle([1,2,3], [1,2,3])
        self.assertEqual(len(p.xaxis), 1)

        expected = set(p.xaxis)

        ax = LinearAxis()
        expected.add(ax)
        p.above.append(ax)
        self.assertEqual(set(p.xaxis), expected)

        ax2 = LinearAxis()
        expected.add(ax2)
        p.above.append(ax2)
        self.assertEqual(set(p.xaxis), expected)

        p.left.append(LinearAxis())
        self.assertEqual(set(p.xaxis), expected)

        p.right.append(LinearAxis())
        self.assertEqual(set(p.xaxis), expected)

    def test_yaxis(self):
        p = plt.figure()
        p.circle([1,2,3], [1,2,3])
        self.assertEqual(len(p.yaxis), 1)

        expected = set(p.yaxis)

        ax = LinearAxis()
        expected.add(ax)
        p.right.append(ax)
        self.assertEqual(set(p.yaxis), expected)

        ax2 = LinearAxis()
        expected.add(ax2)
        p.right.append(ax2)
        self.assertEqual(set(p.yaxis), expected)

        p.above.append(LinearAxis())
        self.assertEqual(set(p.yaxis), expected)

        p.below.append(LinearAxis())
        self.assertEqual(set(p.yaxis), expected)

    def test_axis(self):
        p = plt.figure()
        p.circle([1,2,3], [1,2,3])
        self.assertEqual(len(p.axis), 2)

        expected = set(p.axis)

        ax = LinearAxis()
        expected.add(ax)
        p.above.append(ax)
        self.assertEqual(set(p.axis), expected)

        ax2 = LinearAxis()
        expected.add(ax2)
        p.below.append(ax2)
        self.assertEqual(set(p.axis), expected)

        ax3 = LinearAxis()
        expected.add(ax3)
        p.left.append(ax3)
        self.assertEqual(set(p.axis), expected)

        ax4 = LinearAxis()
        expected.add(ax4)
        p.right.append(ax4)
        self.assertEqual(set(p.axis), expected)

    def test_xgrid(self):
        p = plt.figure()
        p .circle([1,2,3], [1,2,3])
        self.assertEqual(len(p.xgrid), 1)
        self.assertEqual(p.xgrid[0].dimension, 0)

    def test_ygrid(self):
        p = plt.figure()
        p.circle([1,2,3], [1,2,3])
        self.assertEqual(len(p.ygrid), 1)
        self.assertEqual(p.ygrid[0].dimension, 1)

    def test_grid(self):
        p = plt.figure()
        p .circle([1,2,3], [1,2,3])
        self.assertEqual(len(p.grid), 2)

    def test_default_resources_minified(self):
        plt.output_file("foo.html")
        self.assertEqual(plt._default_file['resources'].minified, True)
        plt.reset_output()

    def test_tools(self):
        TOOLS = "resize,pan,box_zoom,reset,lasso_select"
        fig = plt.figure(tools=TOOLS)
        expected = [ResizeTool, PanTool,  BoxZoomTool, ResetTool, LassoSelectTool]

        self.assertEqual(len(fig.tools), len(expected))
        for i, _type in enumerate(expected):
            self.assertIsInstance(fig.tools[i], _type)

        # need to change the expected tools because categorical scales
        # automatically removes pan and zoom tools
        factors = ["a", "b", "c", "d", "e", "f", "g", "h"]
        fig = plt.figure(tools=TOOLS, y_range=factors)
        expected = [ResizeTool, ResetTool, LassoSelectTool]
        self.assertEqual(len(fig.tools), len(expected))
        for i, _type in enumerate(expected):
            self.assertIsInstance(fig.tools[i], _type)


