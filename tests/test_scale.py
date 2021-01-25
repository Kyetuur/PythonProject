import ScaleBuilder


def test_C_major():
    scale = list(ScaleBuilder.build_major_scale_on_root('C'))
    assert scale == ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']


def test_G_major():
    scale = list(ScaleBuilder.build_major_scale_on_root('G'))
    assert scale == ['G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G']


def test_C_minor():
    scale = list(ScaleBuilder.build_minor_scale_on_root('C'))
    assert scale == ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#', 'C']


def test_G_minor():
    scale = list(ScaleBuilder.build_minor_scale_on_root('G'))
    assert scale == ['G', 'A', 'A#', 'C', 'D', 'D#', 'F', 'G']
