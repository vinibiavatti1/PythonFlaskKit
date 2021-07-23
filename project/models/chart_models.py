import json


class Chart:
    """
    Chart model to render chart using Chartjs
    """
    def __init__(self, labels=[]):
        self.labels = labels
        self.datasets = []

    def set_labels(self, labels):
        self.labels = labels

    def add_dataset(self, chart_dataset):
        self.datasets.append(chart_dataset)

    def to_json(self):
        dct = dict(labels=self.labels, datasets=[])
        for dataset in self.datasets:
            dct['datasets'].append(dict(
                label=dataset.label,
                backgroundColor=dataset.background_color,
                borderColor=dataset.border_color,
                borderWidth=dataset.border_width,
                data=dataset.data,
            ))
        return json.dumps(dct)


class ChartDataset:
    """
    Chart dataset model to be used within ChartModel
    """
    def __init__(self, label=''):
        self.label = label
        self.background_color = []
        self.border_color = []
        self.border_width = 2
        self.data = []

    def set_label(self, label):
        self.label = label

    def add_data(self, data):
        self.data.append(data)

    def add_background_color(self, background_color):
        self.background_color.append(background_color)

    def add_border_color(self, border_color):
        self.border_color.append(border_color)

    def set_data(self, data):
        self.data = data

    def set_background_colors(self, background_colors):
        self.background_color = background_colors

    def set_border_colors(self, border_colors):
        self.border_color = border_colors

    def set_border_width(self, border_width):
        self.border_width = border_width
