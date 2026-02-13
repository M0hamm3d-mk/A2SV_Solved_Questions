class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        for r in range(row):
            for c in range(col):
                if image[r][c] == 0:
                    image[r][c] = 1
                else:
                    image[r][c] = 0
            image[r] = image[r][::-1]
        return image
