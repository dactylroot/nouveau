class Deframe(object):
    """check for uniform color boundaries on edges of input and crop them away"""

    def __init__(self, aggressive=False, maxPixelFrame=20):
        self.alpha = 0.1 if aggressive else 0.01
        self.maxPixelFrame = maxPixelFrame

    def _map2idx(self, frameMap):
        try:
            return frameMap.tolist().index(False)
        except ValueError:
            return self.maxPixelFrame

    def _Border(self, img: 'torch.Tensor'):
        """ take greyscale Tensor
            return left,right,top,bottom border size identified """
        import torch
        top = left = right = bottom = 0

        # expected image variance
        hvar, wvar = torch.mean(torch.var(img, dim=0)), torch.mean(torch.var(img, dim=1))

        # use image variance and alpha to identify too-uniform frame borders
        top = torch.var(img[:self.maxPixelFrame,:], dim=1) < wvar*(1+self.alpha)
        top = self._map2idx(top)

        bottom = torch.var(img[-self.maxPixelFrame:,:], dim=1) < wvar*(1+self.alpha)
        bottom = self._map2idx(bottom)

        left = torch.var(img[:,:self.maxPixelFrame], dim=0) < hvar*(1+self.alpha)
        left = self._map2idx(left)

        right = torch.var(img[:,-self.maxPixelFrame:], dim=0) < hvar*(1+self.alpha)
        right = self._map2idx(right)

        return (top, bottom, right, left)

    def __call__(self, img: 'torch.Tensor'):
        import torchvision
        top, bottom, right, left = self._Border(torchvision.transforms.Grayscale()(img)[0])

        height = img.shape[1]-(top+bottom)
        width  = img.shape[2]-(left+right)

        print(f"t{top} b{bottom} l{left} r{right}")

        return torchvision.transforms.functional.crop(img, top, left, height, width)
