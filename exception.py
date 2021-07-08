class ImageShapeError(Exception):
    def __init__(self):
        super().__init__('not valid image shape')
        